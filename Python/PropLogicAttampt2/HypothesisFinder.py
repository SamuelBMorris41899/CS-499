from Python.Debug.Debugger import Debugger
from Python.Errors.InvalidExpression import InvalidExpression
from Python.PropLogicAttampt2.TokenList import TokenList


class HypothesisFinder:
    def __init__(self,statement = "",substatement_table = TokenList()):


        self.Debug = Debugger(debugging = False)

        self.statement_table = substatement_table
        self.Debug.log(substatement_table.to_string())
        self.statement = substatement_table.translate_statement_to_keys(statement,translate_down_to_single_statement=True)



    def find(self):
        split_by_impies = self.statement.split("=>")
        if len(split_by_impies) != 2:
            raise InvalidExpression
        hypos = self.first_part_hypos(split_by_impies[0]) + self.after_implies_hyps(split_by_impies[1])
        self.Debug.log("PROVEN")
        self.Debug.log(hypos)
        return hypos

        # split_by_ands  = statement.split("and")
        # self.Debug.log(split_by_ands)

    def first_part_hypos(self,statement):
        hyps =[i.strip() for i in statement.split("and")]
        #if needed, but if I can I will want to solve eveything in the "normalized" way
        # hyps =[self.substatement_table.translate_keys_to_statement(i) for i in statement.split("and")]
        self.Debug.log(hyps)
        return  hyps

    def after_implies_hyps(self,statement):
        hyps = []
        statement = self.statement_table.translate_keys_to_statement(statement)
        statement = self.statement_table.translate_statement_to_keys(statement).strip(" ()")

        self.Debug.log("SP", statement)
        if "=>" in statement:
            l = statement.split("=>")
            before = l[0].strip()
            self.Debug.log("before",before)
            after = l[1]
            hyps.append(before)
            hyps += self.after_implies_hyps(after)
            return  hyps

        return hyps