from parser import parse
proven = []
subs = []
def simplifySubStatment(statement):
    vars, stats = parse(statement)
    print(vars)
    print(stats)
