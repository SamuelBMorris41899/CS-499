from PropLogic import *
class test:
    def __init__(self,problem,expected):
        self.problem = problem
        self.expected = expected
    def runTest(self):
        #runFunction for Test
        simplifySubStatment(self.problem)
        result = ""
        return result == self.expected


#Examples   11-17
#practice   9,11,12,13
#HW         9-42

test("( not A ) or ( not B ) or C or D and Q" , " ( A and B ) => C").runTest() #want steps     1. hyp. 2.  1,DeMorgan  3. 2,imp

