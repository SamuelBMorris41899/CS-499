from Python.PropLogicAttampt2.HypothesisFinder import HypothesisFinder
from Python.PropLogicAttampt2.PropositionalLogic import PropositionalLogic
from Python.PropLogicAttampt2.TokenList import TokenList
from Python.PropLogicAttampt2.parser import Parse

class TestHypothesis:
    def __init__(self,name,problem,expected):
        self.name = name
        self.statement = problem
        self.expected = expected




    def runTest(self):
        parser = Parse(self.statement)
        table = parser.sub_statements
        hyps = HypothesisFinder(self.statement, table).find()
        result = [table.translate_keys_to_statement(h) for h in hyps]
        r = list(set(result) - set(self.expected))
        if len(r) != 0:
            print(f"{self.name} FAILED")
            print(f"GOT:        {result}")
            print(f"EXPECTED:   {self.expected}")
            print(f"DIFFERENCE: {r}")
            return False
        else:
            print("",end="")
            # print(f"{self.name} passed!")

        return True


#Examples   11-17
#practice   9,11,12,13
#HW         9-42
#

TestHypothesis("hyp_hw_09","A and ( B => C ) => ( B => ( A and C ) )" , ["A","( B => C )","B"]).runTest()
TestHypothesis("hyp_hw_10","B and ( ( B and C ) => A' ) and ( B => C ) => A'" , ["B","( ( B and C ) => A' )","( B => C )"]).runTest()
TestHypothesis("hyp_hw_11","( A => ( B or C ) ) and B' and C' => A'" , ["B'","C'","( A => ( B or C ) )"]).runTest()
TestHypothesis("hyp_hw_12","A' and B and ( B => ( A or C ) ) => C" , ["A'","B","( B => ( A or C ) )"]).runTest()
TestHypothesis("hyp_hw_13","( A or B' )' and ( B => C ) => ( A' and C )" , ["( A or B' )'", "( B => C )"]).runTest()
TestHypothesis("hyp_hw_14","A' and ( B => A ) => B'" , ["A'","( B => A )"]).runTest()
TestHypothesis("hyp_hw_15","( A => B ) and ( A => ( B => C ) ) => ( A => C )" , ["( A => B )","( A => ( B => C ) )","A"]).runTest()
TestHypothesis("hyp_hw_16","( ( C => D ) => C ) => ( ( C => D ) => D )" , ["( ( C => D ) => C )","( C => D )"]).runTest()
TestHypothesis("hyp_hw_17","A' and ( A or B ) => B" , ["A'","( A or B )"]).runTest()
TestHypothesis("hyp_hw_18","( A => ( B => C ) ) and ( A or D' ) and B => ( D => C )" , ["( A => ( B => C ) )", "( A or D' )","B","D"]).runTest()
TestHypothesis("hyp_hw_19","( A' => B' ) and B and ( A => C ) => C" , ["( A' => B' )","B","( A => C )"]).runTest()

class test_prover:
    def __init__(self,name,statement,target,print_steps = False):
        self.name = name
        self.statement = statement
        self.tar = target
        self.print_steps = print_steps

    def runTest(self):
        parser = Parse(self.statement)
        table = parser.sub_statements
        hyps = HypothesisFinder(self.statement, table).find()
        logic = PropositionalLogic(statement = self.statement,hypothesis=hyps,target=self.tar)
        res = logic.solve()
        if res:
            print("PASSED!")

tests_for_prover = [
    test_prover(name = "hw9",target="( A and C )",statement="A and ( B => C ) => ( B => ( A and C ) )",print_steps=False),


    # test_prover(name = "hw10",target="A'",statement="B and ( ( B and C ) => A' ) and ( B => C ) => A'"),

    # test_prover(name = "hw15",target="C",statement="( A => B ) and ( A => ( B => C ) ) => ( A => C )"),
    # test_prover(name="hw14", target="not ( B )", statement="not ( A ) and ( B => A ) => not B"),

    # test_prover(name="hw19", target="C", statement="( not ( A ) => not ( B ) ) and B and ( A => C ) => C",
    #             print_steps=True),

]

for test in tests_for_prover:
    test.runTest()