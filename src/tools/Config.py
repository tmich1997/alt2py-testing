

class Config:
    def __init__(
        self,
        constraints
    ):
        self._constraints = constraints

    def load(self,kwargs):
        self.check_constraints(kwargs)
        self.__dict__.update(**kwargs)

    def check_constraints(self,kwargs):
        print(kwargs)
        for con in self._constraints:
            if con["name"] in kwargs:
                if not isinstance(kwargs[con["name"]],con["type"]):
                    raise TypeError(f"{con['name']} must be of type: {str(con['type'])}")
            else:
                if "required" in con and con["required"]==True:
                    raise TypeError(f"{con['name']} is required!")
                else:
                    kwargs[con["name"]] = con["default"]

    def __str__(self):
        attributes = vars(self)
        out=""
        max_spacing = max([len(attr) for attr,_ in attributes.items()])

        for attribute, value in attributes.items():
            space = " "*(max_spacing - len(attribute))
            newline = '\n' if len(out) else ''
            out +=(f"{newline}{attribute}: {space}{{{value}}}")
        return out
