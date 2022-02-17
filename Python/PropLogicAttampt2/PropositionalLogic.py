from Python.Debug.Debugger import Debugger
from Python.General import Rules
from Python.PropLogicAttampt2.TokenList import TokenList
from Python.PropLogicAttampt2.parser import Parse


class PropositionalLogic:
    max = 11

    def __init__(self,statement="",hypothesis = [],target = ""):
        self.Debug = Debugger(debugging=True)

        self.parser = Parse(statement)
        self.lookup_table = self.parser.sub_statements
        self.proven = hypothesis

        self.translated_proven = [self.lookup_table.translate_keys_to_statement(statement) for statement in self.proven]
        self.target = target

        if Rules.has_open_brackets(target):
            self.target_atoms = [a[1:len(a)-1].strip() for a in target.split("and")]
        else:
            self.target_atoms = [target]

        print("target atoms",self.target_atoms)

        self.steps = {}


    def findRule(self,A,B):
        A = self.lookup_table.translate_statement_to_keys(A)
        B = self.lookup_table.translate_statement_to_keys(B)
        #let A = P


    def add(self,Q):
        self.lookup_table.add_token(Q)
        self.proven.append(self.lookup_table.translate_statement_to_keys(Q))
        self.translated_proven.append(self.lookup_table.translate_keys_to_statement(Q))

    def moden_ponens(self,A):
        A = self.lookup_table.translate_keys_to_statement(A)
        A = self.lookup_table.translate_statement_to_keys(A)
        print("mp",A)
        if "=>" in A:
            list = A.split("=>")
            if len(list) != 2:
                self.Debug.log("ERROR, bad list.... work on translationg table")
                return
            P = list[0].strip()[1:]
            Q = list[1].strip()
            Q = Q[:len(Q) - 1].strip()
            P = self.lookup_table.translate_keys_to_statement(P)
            Q = self.lookup_table.translate_keys_to_statement(Q)
            if P in self.translated_proven and Q not in self.translated_proven:
                self.add(Q)

    def conjunction(self,l,token="and"):
        for A in l:
            A = self.lookup_table.translate_keys_to_statement(A)
            if "=>" in A or "and" in A or "or" in A :
                continue
            for B in l:
                B = self.lookup_table.translate_keys_to_statement(B)
                if A == B:
                    continue
                #rules where we just do not need to do this...
                if "=>" in B or "and" in B or "or" in B:
                    continue

                statement = f"( {A} {token} {B} )"
                if statement not in self.translated_proven:
                    self.add(statement)


        pass

    def solve(self):
        self.max -= 1
        if self.max < 0:
            return False
        inital_proven = self.proven.copy()
        for A in inital_proven:
            self.moden_ponens(A)
        self.conjunction(inital_proven)

        self.Debug.log("proven",self.translated_proven)
        if self.target in self.translated_proven:
            print("EYYYYYYYYYYYYYYYY!")
            return True
        else:
            self.solve()

'''
['B', "( ( B and C ) => A' )",
'( B => C )', "B and ( ( B and C ) => A' )", 
'C', 
'B and ( B => C )', "( ( B and C ) => A' ) and B",
"( ( B and C ) => A' ) and ( B => C )", 
'( B => C ) and B', 
"( B => C ) and ( ( B and C ) => A' )"
]	



'''