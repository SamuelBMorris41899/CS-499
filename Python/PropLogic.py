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
class PLogic:
    def __init__(self,target):
        self.parse = parser()
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
    def get_hypotheses(self,statement):
        hyps = self.parse.get_Hypotheses(statement)
        for h in hyps:
            self.add_step(h,"hyp")
        self.proven = [h for h in hyps]
        return hyps

    '''
    looks for any statments that look like  S1 => S2, if S1 is proven, then S2 is proven
    '''
    def moden_ponens(self,statements):
        for s in statements:
            # s = self.parse.subStatments.translate_statement_to_keys(s)
            if "=>" in s:
                sList = s.split("=>")
                part1 = self.parse.subStatments.translate_keys_to_statement(sList[0])
                part2 = sList[1].strip()
                if part1 in self.proven:
                    if part2 not in self.proven:
                        self.proven.append(part2)
                        self.add_step(part2,"moden ponens")

        return
    '''
    A helper function for conn
    '''
    def hasEquivilent(self,list,s1,s2,token):
        for statement in list:
            t = "{} {} {}".format(s2, token, s1)
            if t in list:
                return True
        return False

    def conjunction(self):
        newStatements = []
        for statementA in self.proven:
            for statementB in self.proven:
                if statementA != statementB:
                    newStatement = "{} and {}".format(statementA,statementB)
                    if newStatement not in self.proven and self.hasEquivilent(newStatements,statementA,statementB,"and") == False:
                        newStatements.append(newStatement)
        for s in newStatements:
            self.add_step(s, "con")
            self.proven.append(s)

    def solve(self,statements):
        self.get_hypotheses(statements)
        while self.target not in self.proven:
            self.moden_ponens(self.proven)
            self.conjunction()

            self.pretty_print_steps()
            print("TARGET",self.target)
            if self.target in self.proven:
                print("TARGET FOUND!!!")
                return True
        return False

