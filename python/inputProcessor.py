keyTokens = {
    "or": "or",
    "and": "and",
    "(": "(",
    ")": ")"
}

def addVariablesToTable(tokens):
    print(tokens)
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
        if char == "(":
            if subStatmentNum == 0:
                start = index
                subStatmentFound = True

            subStatmentNum += 1

        if subStatmentNum != 0:
            subStatment += char + " "

        if char == ")":
            end = index + 1
            subStatmentNum -= 1

        if subStatmentNum == 0 and subStatmentFound:
            break
    #
    # if subStatment != "":
    #     subStatment += ")"

    return subStatment, start, end


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
def getSubStatementBack(inputString, tokens, pos):

    return ""
def getSubStatementFord(inputString, tokens, pos):

    return ""

def combineAndStatements(inputString, tokens, statements, inputVars):
    for pos in range(1, len(tokens) - 1):
        prevToken = tokens[pos - 1]
        currToken = tokens[pos]
        nextToken = tokens[pos + 1]

        if currToken == "and":

            if prevToken in inputVars:
                statement = prevToken
            elif prevToken == ")":
                statement = getSubStatementBack(inputString, tokens, pos)

            statement += currToken

            if nextToken in inputVars:
                statement += nextToken
            elif nextToken == "(":
                statement = getSubStatementFord(inputString, tokens, pos)

    return []


testString = "a and ( p and ( a or c ) and ( c or d ) ) and ( c or d ) "
inputTokens = testString.split(" ")

variables = addVariablesToTable(inputTokens)
subStatements = findAllSubStatments(inputTokens)

combineAndStatements(testString, inputTokens, subStatements, variables)
