'''
11:18 AM - 11:33 AM
1 hour
4:05 PM - 4:30 PM

12:07 PM -
'''

steps = []
given = {}
letter = ""

def getFunctions(statement):
    if letter not in statement:
        return []
    index = statement.find(letter)
    endIndex = statement.find(")", index)
    return [statement[index + 1:endIndex + 1]] + getFunctions(statement[endIndex:])


def addValueToGiven(n,function,functions):
    step = ""
    if n < 0:
        print("ERROR: bad recursion level")
        return 0

    newF = function
    functionWithValue = function

    for f in functions:
        fValue = eval(f)

        key = letter + "(" + str(fValue) + ")"

        if key not in given.keys():
            given[key] = addValueToGiven(fValue,function,functions)

        toRepalce = letter + f
        newF = newF.replace(toRepalce,str(given[key]) )
        functionWithValue = functionWithValue.replace(toRepalce,key)
    finalValue = eval(newF)
    k = letter + "("+str(n)+")"
    if k not in given.keys():
        step += "\n\ngiven we know : \n"
        for key,value in given.items():
            step += key + " =\t" + str(value) + "\n"
        step += "and n = {}. the function {} or ({}), we know S({}) = {}".format(n,function,functionWithValue,n,finalValue)
        given[k] = finalValue
    steps.append(step)
    return  finalValue

def evaluateRecursive(function,g,n):
    global given,steps,letter

    given = g
    steps = []
    letter = list(given.keys())[0][0]
    functions = getFunctions(function)
    print("final", addValueToGiven(n, function, functions))
    print(given)

def getSteps(base_function, given_Values, go_to_n):
    # evaluateRecursive(base_function, given_Values, go_to_n)
    for pos in range(len(steps)):
        step = steps[pos]
        step = "STEP {}\n".format(pos + 1) + step
        steps[pos] = step
    return steps

def getValues():
    l = list(given.values())
    print(l)
    return l