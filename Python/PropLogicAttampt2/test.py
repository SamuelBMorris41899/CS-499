from Python.PropLogicAttampt2.parser import Parse

parser = Parse("A and ( B or ( C and Q ) )")


exit()
class TestHypothesis:
    def __init__(self,name,problem,expected):
        self.name = name
        self.problem = problem
        self.expected = expected

    def runTest(self):
        #runFunction for Test
        logic = PLogic(self.problem,"Not needed for this test")
        hyps = logic.get_hypotheses()
        difference = [i for i in self.expected if i not in hyps] + [i for i in hyps if i not in self.expected]

        if difference == [] :
            # print("{} passed".format(self.name))
            print("",end="")
        else:
            print("{} FAILED".format(self.name))
            print("\tInput = {}".format(self.problem))
            print("\tGot = {}".format(hyps))
            print("\tEXPECTED = {}".format(self.expected))

        return difference == []


#Examples   11-17
#practice   9,11,12,13
#HW         9-42
#
print("fizz")
TestHypothesis("hyp_hw_09","A and ( B => C ) => ( B => ( A and C ) )" , ["A","B => C","B"]).runTest() #final B is deduction method???
TestHypothesis("hyp_hw_10","B and ( ( B and C ) => ( not ( A ) ) ) and ( B => C ) => ( not ( A ) )" , ["B","( B and C ) => ( not ( A ) )","B => C"]).runTest() #final B is deduction method
TestHypothesis("hyp_hw_11","( A => ( B or C ) ) and not B and not C => not A" , ["not B","not C","A => ( B or C )"]).runTest() #final B is deduction method
TestHypothesis("hyp_hw_12","not A and B and ( B => ( A or C ) ) => C" , ["not A","B","B => ( A or C )"]).runTest() #final B is deduction method
TestHypothesis("hyp_hw_13","not ( A or not B ) and ( B => C ) => ( not A and C )" , ["not ( A or not B )", "B => C"]).runTest() #final B is deduction method
TestHypothesis("hyp_hw_14","not A and ( B => A ) => not B" , ["not A","B => A"]).runTest()
TestHypothesis("hyp_hw_15","( A => B ) and ( A => ( B => C ) ) => ( A => C )" , ["A => B","A => ( B => C )","A"]).runTest()
TestHypothesis("hyp_hw_16","( ( C => D ) => C ) => ( ( C => D ) => D )" , ["( C => D ) => C","C => D"]).runTest()
TestHypothesis("hyp_hw_17","not A and ( A or B ) => B" , ["not A","A or B"]).runTest()
TestHypothesis("hyp_hw_18","( A => ( B => C ) ) and ( A or not D ) and B => ( D => C )" , ["A => ( B => C )", "A or not D","B","D"]).runTest()
TestHypothesis("hyp_hw_19","( not A => not B ) and B and ( A => C ) => C" , ["not A => not B","B","A => C"]).runTest()

exit()

class test_prover:
    def __init__(self,name,statement,target,print_steps = False):
        self.name = name
        self.statement = statement
        self.tar = target
        self.print_steps = print_steps

    def runTest(self):
        logic = PLogic(self.statement,self.tar)
        solved = logic.solve()

        if self.print_steps:
            print('printing steps')
            logic.pretty_print_steps()

        if solved:
            # print("{} passed".format(self.name))
            print("", end="")
        else:
            print("{} failed".format(self.name))

tests_for_prover = [
    test_prover(name = "hw9",target="( A ) and ( C )",statement="A and ( B => C ) => ( B => ( A and C ) )",print_steps=False),
    # test_prover(name = "hw10",target="not ( A )",statement="B and ( ( B and C ) => ( not ( A ) ) ) and ( B => C ) => ( not ( A ) )"),
    # test_prover(name = "hw15",target="C",statement="( A => B ) and ( A => ( B => C ) ) => ( A => C )"),
    # test_prover(name="hw14", target="not ( B )", statement="not ( A ) and ( B => A ) => not B"),

    # test_prover(name="hw19", target="C", statement="( not ( A ) => not ( B ) ) and B and ( A => C ) => C",
    #             print_steps=True),

]

for test in tests_for_prover:
    test.runTest()