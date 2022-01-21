keyTokens = {
    "or": "or",
    "and": "and",
    "(": "(",
    ")": ")"
}

def addVariablesToTable(tokens):
    vars = []
    for token in tokens:
        if token not in keyTokens and token not in vars and token != "":
            vars.append(token)
    return vars

def findSubStatment(tokens):
    subStatmentNum = 0
    subStatment = ""
    start = -1
    end = -1
    subStatmentFound = False

    for index in range(0, len(tokens)-1):
        char = tokens[index]

        if subStatmentNum != 0:
            subStatment += " " + char

        if char == "(":
            if subStatmentNum == 0:
                start = index
                subStatmentFound = True
            subStatmentNum += 1
        if char == ")":
            end = index + 1
            subStatmentNum -= 1

        if subStatmentNum == 0 and subStatmentFound:
            break

    return subStatment[1:len(subStatment)-2], start, end

def findAllSubStatments(tokens):
    if len(tokens) == 0:
        return []

    subStatement, startIndex, endIndex = findSubStatment(tokens)

    subStatementList = []
    if endIndex > startIndex:
        subStatementList = findAllSubStatments(tokens[startIndex + 1:endIndex])

    if subStatement != "" and subStatement not in subStatementList:
        subStatementList += [subStatement]

    if endIndex > 0:
        sList = findAllSubStatments(tokens[endIndex:])
        for elem in sList:
            if elem not in subStatementList:
                subStatementList.append(elem)

    return subStatementList


statementKeys = {

}

def addToStatementKeys(list):
    kList = []
    for item in list:
        if item not in statementKeys.values():
            k = "S" + str(len(statementKeys.values()) + 1)
            kList.append(k)
            statementKeys[k] = item
    return kList

def translateKeysToStatement(statement):
    for key in statementKeys.keys():
        if key in statement:
            statement = statement.replace(key, "( " + statementKeys[key] + " )")
    return statement


def translateStatementToKeys(statement):
    returnVal = statement
    for key in statementKeys.keys():
        value = statementKeys[key]
        if value in statement:
            newStatement = statement.replace(value, key)
            newStatement = newStatement.replace("( ","")
            newStatement = newStatement.replace(" )", "")
            if len(returnVal) > len(newStatement):
                returnVal = newStatement
    return returnVal

def dealWithAnd(tokens,context):
    returnValue = []
    if context not in tokens:
        return []
    
    index = tokens.index(context)
    last = tokens.pop(index - 1)
    next = tokens.pop(index)

    newToken = last + " " + context + " " + next
    returnValue.append(newToken)
    tokens[index - 1] = newToken


    tokenToAdd = dealWithAnd(tokens,context)
    returnValue += tokenToAdd
    return returnValue

def dealWithAnds(statements,context):
    returnVal = []
    for statement in statements:
        statement = translateStatementToKeys(statement)
        statement = statement.split(" ")
        returnVal += dealWithAnd(statement, "and")

    return  returnVal


def listToText(list):
    text = ""
    for item in list:
        text += " " + item
    return text[1:]

testString = "b or a and ( p and ( a or c ) and ( c and d ) ) or ( c or d ) "
inputTokens = testString.split(" ")

variables = addVariablesToTable(inputTokens)
subStatements = findAllSubStatments(inputTokens)
addToStatementKeys(subStatements)

andStatements = dealWithAnds(subStatements,"and")

for statement in andStatements:
    statement = translateKeysToStatement(statement)
    if statement not in subStatements:
        subStatements.append((statement))
# print(subStatements)
addToStatementKeys(subStatements)
tString = translateStatementToKeys(testString)
print(tString.split(" "))
exit()
andStatements = dealWithAnds(subStatements,"and")
for statement in andStatements:
    statement = translateKeysToStatement(statement)
    if statement not in subStatements:
        subStatements.append((statement))

print(statementKeys)

exit()

