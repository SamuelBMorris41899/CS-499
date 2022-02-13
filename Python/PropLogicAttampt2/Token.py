import Python.General.Rules as Rules
from Python.Errors.ParenError import ParenError


class Token:
    def __init__(self):
        self.value = ""
        self.equivilent_values = []
        self.tokens = []

    def add(self,value):
        if self.value != "":
            self.value += " "
        self.value += value
        self.tokens += [value]

    def add_equivs(self):
        for token in self.tokens:
            if token not in Rules.keyTokens:
                pass
        print(self.tokens)


    def finalize(self):
        o = 0
        c = 0
        for open_bracket in Rules.open_brackets:
            o += self.value.count(open_bracket)

        for close_bracket in Rules.close_brackets:
            c += self.value.count(close_bracket)

        total = o - c
        if total != 0:
            raise ParenError(o,c)
        self.add_equivs()

    def get_value(self):
        return self.value

    def is_equivilent(self, compare_value):
        return compare_value == self.value or compare_value in self.equivilent_values




    def is_empty(self):
        return self.value == ""

    def has_substatement(self):
        o = 0
        for open_bracket in Rules.open_brackets:
            o += self.value.count(open_bracket)

        if o > 0:
            return True
        else:
            return False