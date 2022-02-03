from parser import parser

parse = parser()
proven = []
subs = []

premise = []


def simplifySubStatment(statement):
    hyps = parse.get_Hypotheses_Simple(statement)
    print(hyps)

