class test:
    given = [
        ("S1",10)
    ]
    function = "S(n-1) + 10"
    def __init__(self,givens,f):
        self.given = givens
        self.function = f

test1 = test(
    [("S1",10)],
    "S(n-1) + 10"
)
