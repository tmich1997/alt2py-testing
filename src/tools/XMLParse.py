import pandas as pd;
import xml.etree.ElementTree as ET;

class XMLParse:
    def __init__(self,yxdb_tool=None,json=None,config=None,**kwargs):
        self.config = self.Config();
        if config:
            self.config = config
        elif yxdb_tool:
            self.load_yxdb_tool(yxdb_tool)
        elif json:
            self.load_json(json);
        elif kwargs:
            self.load_json(kwargs);

    def load_json(self,json):
        c = self.config;

    def load_yxdb_tool(self,tool,execute=True):
        c = self.config;
        xml = tool.xml;

        c.field = xml.find(".//Configuration//XMLField").text
        c.parse_children = xml.find(".//Configuration//ChildValues").get("value")=="True"
        c.return_outer = xml.find(".//Configuration//OuterXML").get("value")=="True"
        c.ignore = xml.find(".//Configuration//IgnoreErrors").get("value")=="True"
        c.keep = xml.find(".//Configuration//IncludeInOutput").get("value")=="True"

        c.root = xml.find(".//Configuration//XMLElement").text
        if xml.find(".//Configuration//ParseRoot").get("value")=="True":
            c.root=True
        elif c.root=="":
            c.root=None;

        if execute:
            df = tool.get_input("Input")
            next_df = self.execute(df)
            tool.data["Output"] = next_df

    def autodetect_root(self,df):
        c = self.config;
        series = df.iloc[0]

        tree = ET.fromstring(series[c.field])

        elmts = {}

        nodes_to_check = [{"node":n,"prefix":tree.tag} for n in tree]
        depth = 1;
        while len(nodes_to_check)>0:
            next_checks = []
            for n in nodes_to_check:
                node = n["node"]
                prefix = n["prefix"]
                next_checks += [{"node":n2,"prefix":f"{prefix}.{n2.tag}"} for n2 in node]
                tag = prefix + "." + node.tag
                if tag in elmts:
                    elmts[tag]["count"]+=1
                else:
                    elmts[tag] = {
                        "depth":depth,
                        "count":1
                    }
            depth+=1
            nodes_to_check = next_checks
        max_count = 0
        selected_node = None
        for k in elmts:
            if elmts[k]["count"]>max_count:
                selected_node = k.split('.')[-1]
                max_count = elmts[k]["count"]
        c.root = selected_node

    def applier(self,series):
        c = self.config;

        tree = ET.fromstring(series[c.field])

        if c.root is None:
            trees = [tree]
        elif c.root == True and isinstance(c.root, bool):
            trees = [tree]
        else:
            trees = tree.findall(".//"+c.root)

        if tree is None or len(trees)==0:
            return series.to_frame().T

        series_list = []
        for tree in trees:
            s = series.copy()
            s[tree.tag] = tree.text.strip()
            for attr in tree.attrib:
                s[attr] = tree.attrib[attr]

            if c.return_outer:
                s[tree.tag+"_OuterXML"] = ET.tostring(tree, encoding='utf-8').decode('utf-8').strip()

            if c.parse_children:
                for node in tree:
                    s[node.tag] = node.text.strip()
                    for attr in node.attrib:
                        s[node.tag + "_" +attr] = node.attrib[attr]

                    if c.return_outer:
                        s[node.tag+"_OuterXML"] = ET.tostring(node, encoding='utf-8').decode('utf-8').strip()
            series_list.append(s)

        out = pd.DataFrame(series_list)
        return out

    def execute(self,input_datasource):
        c = self.config;
        new_df = input_datasource.copy();

        if c.root is None:
            self.autodetect_root(new_df)

        df_series = new_df.apply(
            self.applier,
            axis=1
        )

        df_list = [df for df in df_series if not df.empty] #prevents unwanted unit conversions
        new_df = pd.concat(df_list, ignore_index=True)

        return new_df.reset_index(drop=True)

    class Config:
        def __init__(
            self
        ):
            self.field = None
            self.root = None
            self.parse_children = False
            self.return_outer = False
            self.ignore = False
            self.keep = False

        def __str__(self):
            attributes = vars(self)
            out=""
            max_spacing = max([len(attr) for attr,_ in attributes.items()])

            for attribute, value in attributes.items():
                space = " "*(max_spacing - len(attribute))
                newline = '\n' if len(out) else ''
                out +=(f"{newline}{attribute}: {space}{{{value}}}")
            return out
