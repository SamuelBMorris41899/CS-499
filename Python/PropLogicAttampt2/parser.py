from Python.Debug.Debugger import Debugger
from Python.PropLogicAttampt2.Token import Token
from Python.PropLogicAttampt2.TokenList import TokenList
import Python.General.Rules as Rules


class Parse:
    def __init__(self,statement):

        self.Debug = Debugger(debugging=True)
        self.substatements = self.get_substatements(statement)

        for substatement in self.substatements.tokens.values():
            self.Debug.log("EQUIVILENT STATEMENTS")
            self.Debug.log(substatement.value)
            for equiv in substatement.equivilent_values:
                self.Debug.log(f"\t{equiv}")

    def get_substatements(self,statement):

        all_substatements = TokenList()
        subStatement = Token()

        parens = 0
        for token in statement.split(" "):

            if token in Rules.close_brackets:
                parens -= 1

            if parens != 0:
                subStatement.add(token)

            if token in Rules.open_brackets:
                parens += 1


            if parens == 0 and not subStatement.is_empty():
                subStatement.finalize()

                if subStatement.has_substatement():
                    all_substatements.add_all_tokens_from_token_list(self.get_substatements(subStatement.value))



                all_substatements.add_token(subStatement)
                subStatement = Token()

        self.Debug.log(f"all substatements in: {statement}")
        self.Debug.log(all_substatements.to_string())

        return all_substatements

