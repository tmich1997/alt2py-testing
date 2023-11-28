

class Config:
    def __init__(
        self,
        **kwargs
    ):
        self.__dict__.update(**kwargs)

    def load_config(self):
        print("load")

    def __str__(self):
        attributes = vars(self)
        out=""
        max_spacing = max([len(attr) for attr,_ in attributes.items()])

        for attribute, value in attributes.items():
            space = " "*(max_spacing - len(attribute))
            newline = '\n' if len(out) else ''
            out +=(f"{newline}{attribute}: {space}{{{value}}}")
        return out
