from Python.Debug.Debugger import Debugger
from Python.PropLogicAttampt2.TokenList import TokenList
import Python.General.Rules as Rules

class Parse:
    def __init__(self,statement):

        self.Debug = Debugger(debugging=False)
        self.sub_statements = self.get_substatements(statement)
        self.sub_statements.add_token(statement)
        self.Debug.log("final")
        self.Debug.log(self.sub_statements.to_string())




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

        all_substatements = TokenList()

        if not Rules.has_open_brackets(statement):
            return all_substatements

        start = statement.find("(")
        end = statement.find(")") + 1       #to include the paren
        sub_statement = statement[start:end]


        # look at the rest of the string


        sub_sub_statement_count = sub_statement.count("(") - 1

        # find the real ending of the sub statement!
        for i in range(sub_sub_statement_count):
            end = statement.find(")",end) + 1

        sub_statement = statement[start:end]
        all_substatements.add_token(sub_statement)

        # all_substatements.add_all_tokens(self.get_substatements(sub_statement[end + 3:]))

        #get the sub statements inside this substatement
        sub_sub_statement = statement[start+1:end-1].strip()
        if Rules.has_open_brackets(sub_sub_statement) and Rules.has_closed_brackets(sub_sub_statement):
            all_substatements.add_all_tokens_from_token_list(self.get_substatements(sub_sub_statement))

        all_substatements.add_all_tokens_from_token_list(self.get_substatements(statement[end:]))

        return all_substatements

