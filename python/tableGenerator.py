
from inputProcessor import getAllStatements
import ttg
def generateTruthTable(statement):
    v,s = getAllStatements(statement)
    truthTable = ttg.Truths(list(set(v)),s)
    return (truthTable,truthTable.valuation())

# table,blah = generateTruthTable("b or a and ( p and ( a or c ) and ( c or d ) ) or e")
# table,blah = generateTruthTable("( a and b ) nand c xor ( not ( d or c ) )")
table,blah = generateTruthTable("( b => c ) => ( c and d or b )")
print(blah,"\n",table)
'''
TODO:
if Taut or Contra

FIX Nots!
not,        not
nor,        nor
xor,        exclusive or
nand        nand
=           biconditional
#27,28
'''
