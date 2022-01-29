import recursion
class test:
    given = {}
    function = ""
    def __init__(self,givens,f,n):
        self.given = givens
        self.function = f
        self.n = n
    def runTest(self,expected):
        recursion.evaluateRecursive(self.function, self.given, self.n)
        if(expected != recursion.getValues()):
            print ("Failed")
            return False
        print("Passed")
        return True

test_example1 = test(
    {"S(1)":2},
    "2 * S(n-1)",
    5
)
test_example1.runTest([2,4,8,16,32])

test_practice2 = test(
    {"S(1)":1,
     "S(2)":1},
    "S(n-1) + S(n-2)",
    6
)
test_practice2.runTest([1,1,2,3,5,8])


test1 = test(
    {"S(1)":10},
    "S(n-1) + 10",
    6
)

# test1.runTest([10,20,30,40,50,60])