from Python.PropositionalLogic.rules import keyTokens

class Token:
    def __init__(self):
        self.value = ""
        self.equivilent_values = []

    def add(self,value):
        newValue = self
        if newValue.value != "":
            newValue.value += " "
        newValue.value += value

        for pos in range(len(newValue.equivilent_values)):
            v = newValue.equivilent_values[pos]
            if value not in keyTokens and value[0] != "(" and value[len(value)-1] != ")":
                v += "( {} )".format(value)
            newValue.equivilent_values[pos] = v

        return newValue         #done so you can do the java ish thing of token.add("A").add("and").add("B")




    def get_value(self):
        return self.value

    def is_same_value(self,compare_value):
        return compare_value in self.equivilent_values