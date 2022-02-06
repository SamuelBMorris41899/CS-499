from PropLogic import *

class test_hypothesis:
    def __init__(self,name,problem,expected):
        self.name = name
        self.problem = problem
        self.expected = expected

    def runTest(self):
        #runFunction for Test
        logic = PLogic()
        hyps = logic.get_hypotheses(self.problem)
        difference = [i for i in self.expected if i not in hyps] + [i for i in hyps if i not in self.expected]

        if difference == [] :
            print("{} passed".format(self.name))
        else:
            print("{} FAILED".format(self.name))
            print("\tInput = {}".format(self.problem))
            print("\tGot = {}".format(hyps))
            print("\tEXPECTED = {}".format(self.expected))

        return difference == []


#Examples   11-17
#practice   9,11,12,13
#HW         9-42

test_hypothesis("hyp_hw_09","A and ( B => C ) => ( B => ( A and C ) )" , ["A","B => C","B"]).runTest() #final B is deduction method???
test_hypothesis("hyp_hw_10","B and ( ( B and C ) => not A ) and ( B => C ) => not A" , ["B","( B and C ) => not A","B => C"]).runTest() #final B is deduction method
test_hypothesis("hyp_hw_11","( A => ( B or C ) ) and not B and not C => not A" , ["not B","not C","A => ( B or C )"]).runTest() #final B is deduction method
test_hypothesis("hyp_hw_12","not A and B and ( B => ( A or C ) ) => C" , ["not A","B","B => ( A or C )"]).runTest() #final B is deduction method
test_hypothesis("hyp_hw_13","not ( A or not B ) and ( B => C ) => ( not A and C )" , ["not ( A or not B )", "B => C"]).runTest() #final B is deduction method
test_hypothesis("hyp_hw_14","not A and ( B => A ) => not B" , ["not A","B => A"]).runTest()
test_hypothesis("hyp_hw_15","( A => B ) and ( A => ( B => C ) ) => ( A => C )" , ["A => B","A => ( B => C )","A"]).runTest()
test_hypothesis("hyp_hw_16","( ( C => D ) => C ) => ( ( C => D ) => D )" , ["( C => D ) => C","C => D"]).runTest()
test_hypothesis("hyp_hw_17","not A and ( A or B ) => B" , ["not A","A or B"]).runTest()
test_hypothesis("hyp_hw_18","( A => ( B => C ) ) and ( A or not D ) and B => ( D => C )" , ["A => ( B => C )", "A or not D","B","D"]).runTest()
test_hypothesis("hyp_hw_19","( not A => not B ) and B and ( A => C ) => C" , ["not A => not B","B","A => C"]).runTest()

class test_prover:
    def __init__(self,name,statement):
        self.name = name
        self.statement = statement

    def runTest(self):
        logic = PLogic()
        solved = logic.solve(self.statement)

test_prover("NEW_TEST","A and ( B => C ) => ( B => ( A and C ) )").runTest() #final B is deduction method???
