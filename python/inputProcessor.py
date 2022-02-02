keyTokens = {
    "or": "or",
    "and": "and",
    "(": "(",
    ")": ")",
    "not":"not",
    "nor":"nor",
    "nand":"nand",
    "xor":"xor",
    "=>":"=>",
    "=":"="
}

keyTokensOrder = [["not"],["and","nand"],["or","xor","nor"],["=>","="]]


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

    for index in range(0, len(tokens) - 1):
        char = tokens[index]

        if char == "(":
            if subStatmentNum == 0:
                start = index
                subStatmentFound = True
            subStatmentNum += 1
        if char == ")":
            end = index + 1
            subStatmentNum -= 1

        if subStatmentNum != 0:
            subStatment += " " + char

        if subStatmentNum == 0 and subStatmentFound:
            break

    return subStatment[2:len(subStatment)].strip(), start, end

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
        nextPart = tokens[endIndex :]
        sList = findAllSubStatments(nextPart)
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

def translateKeysToStatement(statement):
    for key in statementKeys.keys():
        if key in statement:
            statement = statement.replace(key, "( " + statementKeys[key] + " )")
    return statement


def translateStatementToKeys(statement):
    returnVal = statement

    for key,value in statementKeys.items():
        if value in statement:
            returnVal = statement.replace(value,key)
            returnVal = returnVal.replace("( " + key + " )",key) #in case there are ()

    if returnVal != statement:
        returnVal = translateStatementToKeys(returnVal)
    return returnVal

def dealWith_keyToken_A(string, context):
    string = translateStatementToKeys(string)
    print(string)

    return []
    tokens = string.split(" ")
    print(tokens)
    if context not in tokens:
        return []
    index = tokens.index(context)
    nextToken = tokens.pop(index + 1)
    tokens[index] = context + " " + nextToken
    tokens = dealWith_keyToken_A(tokens, context)
    return tokens

def dealWith_A_keyToken_B(tokens, context):

    returnValue = []

    contextTokens = 0
    for c in context:
        if c in tokens:
            contextTokens += 1
    if contextTokens == 0:
        return []

    lowestIndex = -1
    index = -1
    for c in context:
        if(c in tokens):
            index = tokens.index(c)
            if(lowestIndex < index):
                lowestIndex = index
    if(index == -1):
        print("negative index")
        return []
    index = lowestIndex
    token = tokens[lowestIndex]
    last = tokens.pop(index - 1)
    next = tokens.pop(index)

    newToken = last + " " + token + " " + next
    returnValue.append(newToken)
    tokens[index - 1] = newToken


    tokenToAdd = dealWith_A_keyToken_B(tokens, context)
    returnValue += tokenToAdd
    return returnValue


def dealWithConditionals(string,context): ###############################################################
    context = context[0]
    print("inCOnditionals", string)
    return []
    string = translateStatementToKeys(string)

    if context in string:
        addToStatementKeys(string)
        return dealWithConditionals(string,context) + [string]
    return []


def listToText(list):
    text = ""
    for item in list:
        text += " " + item
    return text[1:]

def getStatementAndAddToStatementKeys(string,context):
    statements = []
    translated = translateStatementToKeys(string)
    ands = dealWith_A_keyToken_B(translated.split(" "), context)
    for statement in ands:
        statement = translateKeysToStatement(statement)
        statements.append(statement)
    addToStatementKeys(statements)

    for s in ands:
        s = translateKeysToStatement(s)
        statements.append(s)

    return  statements

def dealWithStatements(statement):
    s = []
    # s += dealWith_keyToken_A(statement, "not") Not needed due to substatement
    s += getStatementAndAddToStatementKeys(statement, ["and", "nand"])
    s += getStatementAndAddToStatementKeys(statement, ["or", "xor"])
    s += dealWithConditionals(statement,["=>","="])
    return s
def getAllStatements(iString):
    if iString == "":
        return [],[]
    statementKeys.clear()
    allStatements = [iString]

    inputTokens = iString.split(" ")

    variables = addVariablesToTable(inputTokens)

    subStatements = findAllSubStatments(inputTokens)
    addToStatementKeys(subStatements)
    #deal with ands in subStatments



    
    for statement in subStatements:
        count = 0
        for key,value in statementKeys.items():
            if value in statement:
                count += 1

        if count > 1: #there is at least one subStatement in the statement
            for key,value in statementKeys.items():
                if value in statement:
                    newStatement = statement.replace("( " + value + " )",key)
                    if newStatement not in statementKeys.keys():
                        statement = newStatement
            allStatements += dealWithStatements(statement)



    allStatements += subStatements
    allStatements += dealWithStatements(iString)

    allStatements = list(set(allStatements))

    variables.sort()
    allStatements.sort()
    allStatements.sort(key=len)

    return (variables,allStatements)