import recursion
class test:
    given = {}
    function = ""
    def __init__(self,givens,f,n,expected):
        self.given = givens
        self.function = f
        self.n = n
        self.expected = expected

    def runTest(self):
        recursion.evaluateRecursive(self.function, self.given, self.n)
        if self.expected != recursion.getValues():
            print ("Failed")
            print("Values found    ", recursion.getValues())
            print("Values expected ", self.expected)
            return False
        print("Passed")
        return True

test_example1 = test(
    {"S(1)":2},
    "2 * S(n-1)",
    5,
[2,4,8,16,32]
)
test_example1.runTest()

test_practice2 = test(
    {"S(1)":1,
     "S(2)":1},
    "S(n-1) + S(n-2)",
    6,
[1,1,2,3,5,8]
)
test_practice2.runTest()

tests = [
    test(
        {"S(1)":10},
        "S(n-1) + 10",
        6,
        [10,20,30,40,50,60]
    ),
    test(
        {"C(1)":5},
        "2*C(n-1) + 5",
        6,
        [5,15,35,75,155,315]
    ),

    test(                                                       #MIGHT BE WRONG?
        {"A(1)":2},
        "1/(A(n-1))",
        6,
        [2, 0.5, 2.0, 0.5, 2.0, 0.5]
    ),


]

for t in tests:
    t.runTest()
# test1.runTest([10,20,30,40,50,60])