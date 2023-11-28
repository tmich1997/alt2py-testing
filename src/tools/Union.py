import pandas as pd;

class Union:
    def __init__(self,xml=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif xml:
            self.load_xml(xml)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);


    def load_json(self,json):
        c = self.config;

    def load_xml(self,xml):
        c = self.config;

        mode_names = {"ByName":"name","ByPos":"position","Manual":"manual","ManualDelayed":"manual"}
        c.mode = mode_names[xml.find(".//Configuration//Mode").text]
        c.subset = xml.find(".//Configuration//ByName_OutputMode").text=="Subset"

        order_changed = xml.find(".//Configuration//SetOutputOrder").get("value")=="True"

        if order_changed:
            c.order = [con.text for con in xml.find(".//Configuration//OutputOrder")]

        if c.mode == "manual":
            c.manual = []
            for meta_info in xml.find(".//Configuration//MultiMetaInfo"):
                c.manual.append([f.get("name") for f in meta_info.find("RecordInfo")])


    def union_by_manual(self,dfs):
        c = self.config;

        renamed_dfs = []
        print(c.manual)
        for i,df in enumerate(dfs):
            if i==0:
                renamed_dfs.append(df[c.manual[0]])
            else:
                new_df = df[c.manual[i]]
                renames = {}
                for j,old_name in enumerate(new_df.columns.tolist()):
                    renames[old_name] = c.manual[0][j]
                new_df.rename(columns=renames,inplace=True);
                renamed_dfs.append(new_df)
        merged = pd.concat(renamed_dfs,axis=0)
        return merged

    def union_by_pos(self,dfs):
        c = self.config;

        names = dfs[0].columns.tolist()
        for df in dfs[1:]:
            renames = {}
            for i,col in enumerate(df.columns):
                if i<len(names):
                    renames[col] = names[i]
                else:
                    names.append(df.columns[i])
            df.rename(columns=renames,inplace=True)

        merged = pd.concat(dfs,axis=0)
        if c.subset:
            length = min([len(df.columns) for df in dfs])
            merged = merged.iloc[:, :length]
        return merged

    def union_by_name(self,dfs):
        c = self.config;

        matched_names = [];
        unmatched_names = [];

        if c.subset:
            matched_names = []
            for name in dfs[0].columns:
                matched = True
                for df in dfs[1:]:
                    matched = matched and (name in df.columns)
                if matched:
                    matched_names.append(name)

            dfs = [df[matched_names] for df in dfs]

            merged = pd.concat(dfs,axis=0)
            return merged
        else:
            matched_names = dfs[0].columns.tolist()
            for df in dfs[1:]:
                for col in df.columns:
                    if col not in matched_names:
                        matched_names.append(col)
            new_dfs = []
            for df in dfs:
                for name in matched_names:
                    if name not in df.columns:
                        df[name] = pd.NA
                new_dfs.append(df[matched_names])

            merged = pd.concat(new_dfs,axis=0)
            return merged


    def execute(self,input_datasources):
        c = self.config;

        dfs = None;
        if isinstance(input_datasources[0],dict):
            dfs = {df["name"]:df["data"].copy() for df in input_datasources}
            if len(c.order)>0:
                dfs = [dfs[n] for n in c.order]
            else:
                dfs = list(dfs.values())
        else:
            dfs = [df.copy() for df in input_datasources]

        print(c.order)
        
        if c.mode == "name":
            new_df = self.union_by_name(dfs)
        elif c.mode == "position":
            new_df = self.union_by_pos(dfs)
        elif c.mode == "manual":
            new_df = self.union_by_manual(dfs)
        else:
            raise Exception("Invalid mode. Valid modes are: 'name','position' or 'manual'")


        for i,dtype in enumerate(new_df.dtypes):
            if dtype=="object":
                new_df[new_df.columns[i]] = new_df[new_df.columns[i]].astype(pd.StringDtype())

        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.mode = "position"#|name|manual
            self.subset = True;
            self.manual = [];
            self.order = [];

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
