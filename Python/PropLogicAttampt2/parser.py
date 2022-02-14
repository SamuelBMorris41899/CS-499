from Python.Debug.Debugger import Debugger
from Python.PropLogicAttampt2.Token import Token
from Python.PropLogicAttampt2.TokenList import TokenList
import Python.General.Rules as Rules

class Parse:
    def __init__(self,statement):

        self.Debug = Debugger(debugging=True)
        self.substatements = self.get_substatements(statement)
        return
        for substatement in self.substatements.tokens.values():
            self.Debug.log("EQUIVILENT STATEMENTS")
            self.Debug.log(substatement.value)
            for equiv in substatement.equivilent_values:
                self.Debug.log(f"\t{equiv}")

    def normalize(self,statement):
        new_statement = ""
        for char in statement:
            if char in Rules.open_brackets:
                new_statement += "("
            elif char in Rules.close_brackets:
                new_statement += ")"
            else:
                new_statement += char

        return new_statement

    def get_substatements(self,statement):
        self.Debug.log("statement\t" , statement)
        all_substatements = TokenList()
        subStatement = Token()

        start = statement.find("(")
        end = statement.find(")") + 1       #to include the paren
        sub_statement = statement[start:end]
        print(sub_statement)
        sub_sub_statement_count = sub_statement.count("(") - 1
        print(sub_sub_statement_count)
        for i in range(sub_sub_statement_count):
            end = statement.find(")",end) + 1
        sub_statement = statement[start:end]
        print(sub_statement)

        return all_substatements

