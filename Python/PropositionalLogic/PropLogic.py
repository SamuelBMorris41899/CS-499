'''
TO DO:
    all the rules
    what steps did I get that from?
        eg.
            1	hyp             	 A
            2	hyp             	 B => C
            3	hyp             	 B
            4	moden ponens    	 C
        should be
            1	hyp             	 A
            2	hyp             	 B => C
            3	hyp             	 B
            4	3,2 mp    	         C
'''

from parser import parser


def listToString(l):
    retVal = ""
    for item in l:
        retVal += item + " "
    retVal.strip()
    return  retVal

class PLogic:
    def __init__(self,statement,target):
        self.statement = statement
        self.parse = parser(statement)
        self.proven = []
        self.subs = []
        self.premise = []
        self.target = target

        self.steps = {}
        self.stepCount = 1

    def pretty_print_steps(self):
        for key,value in self.steps.items():
            print(key,end="\t")
            step_is_what = '{0:<15}'.format(value[1])
            print(step_is_what,"\t",value[0])

    def add_step(self,statement,step):
        key = "{}".format(self.stepCount)
        self.steps[key] = [statement,step]
        self.stepCount += 1



    '''
    Gets the hypotheses and adds them to the steps list
    '''
    def get_hypotheses(self):
        hyps = self.parse.get_hypotheses()

        for h in hyps:
            self.add_step(h,"hyp")

        self.proven = [h for h in hyps]

        return hyps



    '''
    looks for any statments that look like  S1 => S2, if S1 is proven, then S2 is proven
    '''
    def moden_ponens(self,statements):

        for s in statements:
            s = self.parse.subStatments.translate_statement_to_keys(s)

            if "=>" in s:
                sList = s.split("=>")
                part1 = self.parse.subStatments.translate_keys_to_statement(sList[0])
                part2 = self.parse.subStatments.translate_keys_to_statement(sList[1])

                if part1 in self.proven:
                    if part2 not in self.proven:
                        self.proven.append(part2)
                        self.add_step(part2,"moden ponens")

    '''
    A helper function for conn
    '''
    def hasEquivilent(self,list,s1,s2,token):
        for statement in list:
            t = "{} {} {}".format(s2, token, s1)
            if t in list:
                return True
        return False

    def conjunction(self,statements):
        newStatements = []
        for statementA in statements:
            for statementB in statements:
                if statementA != statementB:
                    newStatement = "( {} ) and ( {} )".format(statementA,statementB)
                    if newStatement not in self.proven and self.hasEquivilent(newStatements,statementA,statementB,"and") == False:
                        newStatements.append(newStatement)
                        # self.parse.subStatments.add_token(newStatement)

        for s in newStatements:
            self.add_step(s, "con")
            self.proven.append(s)

    def simplify(self,statement):
        statement = self.parse.subStatments.translate_keys_to_statement(statement)
        statement = statement.replace("not not", "")
        self.add_step(statement,"simplify")
        return statement

    def double_negation(self, statements):
        add_to_proven = []
        for statement in statements:
            if statement in self.proven:
                notnot = "not (  not ("
                if notnot in statement[:len(notnot)]:
                    statement = self.parse.subStatments.translate_keys_to_statement(statement[len(notnot):])
                    statement = "not ( not ( {} ) )".format(statement)
                    add_to_proven.append(statement)
                    self.parse.subStatments.add_token(statement)
                    self.add_step(statement, "rm notnot")
                    pass
                else:
                    statement = self.parse.subStatments.translate_keys_to_statement(statement)
                    statement = "not ( not ( {} ) )".format(statement)
                    add_to_proven.append(statement)
                    self.parse.subStatments.add_token(statement)
                    self.add_step(statement,"double negation")

        self.proven += add_to_proven

    def moden_tolens(self,statements):
        # print("\n\nmoden_tolens")
        # self.pretty_print_steps()
        for s in statements:
            s = self.parse.subStatments.translate_statement_to_keys(s)
            # print(s)
            if "=>" in s:
                sList = s.split("=>")
                part1 = self.parse.subStatments.translate_keys_to_statement(sList[0])
                part2 = self.parse.subStatments.translate_keys_to_statement(sList[1])
                print(part1)
                print(part2)
                s = "{} => {}".format(part1, part2)
                if s in self.proven:
                    if "not {}".format(part2) in self.proven or "not ( {} )".format(part2) in self.proven:
                        to_add = "not ( {} )".format(part1)
                        if to_add not in self.proven:
                            self.proven.append(to_add)
                            self.add_step(to_add,"mt")
        # print("\n\n-")
        # print("END MOLEN_TOLENS")



    def solve(self):
        statements = self.statement
        self.get_hypotheses()

        while self.target not in self.proven:

            self.double_negation(self.proven)
            if self.target in self.proven:
                break
            self.moden_ponens(self.proven)
            if self.target in self.proven:
                break
            self.conjunction(self.proven)
            if self.target in self.proven:
                break
            self.moden_tolens(self.proven)
            if self.target in self.proven:
                break

            # print("after MT")
            self.pretty_print_steps()
            print("\n\n\n")
        # print("TARGET",self.target)
        if self.target in self.proven:
            # self.parse.subStatments.print_values()
            return True
        return False

