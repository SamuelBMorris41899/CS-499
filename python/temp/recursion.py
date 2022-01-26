'''
11:18 AM - 11:33 AM

'''
steps = []
given = {
    "S(1)":1,
    "S(2)":1,
}
function = "S(n-1)+S(n-2)"
maxN = 10
minN = 2
letter = list(given.keys())[0][0]


def getFunctions(statement,index = 0):
    if letter not in statement:
        return []
    index = statement.find(letter)
    endIndex = statement.find(")", index)
    return [statement[index + 1:endIndex + 1]] + getFunctions(statement[endIndex:], endIndex)

functions = getFunctions(function)


print(functions)


n = 3
step = "S({})".format(n)


def addValueToGiven(n,function,function_of_N):
    newValue = 0
    if(n < 0):
        print("ERROR: invalid n given")
        return 0

    for f in functions:
        fValue = eval(f)
        key = letter + "(" + str(fValue) + ")"
        if key not in given.keys():
            print("no key")
            k = letter + "(" + str(fValue) + ")"
            given[k] = addValueToGiven(fValue,function,functions)
        else:
            print(key + " = ", fValue)
            newValue += given[key]
    print("new value is ",newValue)


    return  newValue

print("final",addValueToGiven(6,function,functions))
print(given)