import Token
from rules import keyTokens
from parser import parser
token = Token.Token()

def addAtomsToTable(tokens):
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
    # return subStatment[len(subStatment)].strip(" ()"), start, end

def findAllSubStatments(tokens):
    if len(tokens) == 0:
        return []

    subStatement, startIndex, endIndex = findSubStatment(tokens)
    subStatementList = []
    if endIndex > startIndex:
        # get any subStatement inside pf the already found substatement
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



def listToText(list):
    text = ""
    for item in list:
        text += " " + item
    return text[1:]


def getStatementAndAddToStatementKeys(string,context):
    statements = []
    translated = token.translate_statement_to_keys(string)
    ands = dealWith_A_keyToken_B(translated.split(" "), context)
    for statement in ands:
        statement = token.translate_keys_to_statement(statement)
        statements.append(statement)
    token.add_multiple_token(statements)

    for s in ands:
        s = token.translate_keys_to_statement(s)
        statements.append(s)

    return statements


def dealWithStatements(statement):
    s = []
    s += getStatementAndAddToStatementKeys(statement, ["and", "nand"])
    s += getStatementAndAddToStatementKeys(statement, ["or", "xor"])
    return s


def getAllStatements(iString):
    global token
    if iString == "":
        return [], []
    token = Token.Token()
    allStatements = [iString]
    inputTokens = iString.split(" ")
    variables = addAtomsToTable(inputTokens)
    subStatements = findAllSubStatments(inputTokens)
    token.add_multiple_token(subStatements)
    for statement in subStatements:
        count = 0
        for key,value in token.get_dict().items():
            if value in statement:
                count += 1

        if count > 1: #there is at least one subStatement in the statement
            for key,value in token.get_dict().items():
                if value in statement:
                    newStatement = statement.replace("( " + value + " )",key)
                    if newStatement not in token.get_keys():
                        statement = newStatement
            allStatements += dealWithStatements(statement)



    allStatements += subStatements
    allStatements += dealWithStatements(iString)

    allStatements = list(set(allStatements))

    variables.sort()
    allStatements.sort()
    allStatements.sort(key=len)

    return variables, allStatements
