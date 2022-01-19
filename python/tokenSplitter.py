keyTokens = {
    "V": "or",
    "N": "and",
    "or": "or",
    "and": "and",
    "(": "(",
    ")": ")"
}

wffsFound = {

}

def addStatmentsToTable (statments):
    count = 0
    for s in statments:
        count += 1
        tag = "S" + count
        wffsFound[tag] = s

def replaceSubStatmentsWithTags(inputString):
    for key,value in wffsFound:
        inputString = inputString.replace(value, key)
    return inputString

def __tokenIsParens__(token):
    return token == "(" or token == ")"


def __buildSubStatments__(tokens):
    subStatments = []
    subStatment = ""
    numSubStatment = 0

    for token in tokens:
        if token == "(":
            numSubStatment -= 1
        if token == ")":
            numSubStatment += 1
        if numSubStatment != 0:
            subStatment += " " + token
        if numSubStatment == 0 and subStatment != "":
            final = subStatment[3:]
            subStatments.append(final)  # remove leading space
            subStatment = ""
    addStatmentsToTable(subStatments)
    return subStatments


def __getSubStatments__(tokens):
    subStatments = __buildSubStatments__(tokens)

    # recursion to get statments inside of the substatment
    returnValue = []
    for statment in subStatments:
        finalStatment = statment
        statments = statment.split(' ')
        recursive = __getSubStatments__(statments)
        returnValue += [finalStatment] + recursive
    return returnValue


def __connectSubSetandWff__(tokens, index, direction):
    subStatment = []
    parensCount = 0
    # this will determine which way the function is looking.
    list = []
    if (direction < 0):
        # if backward
        list = range(index + direction, 0, direction)
    else:
        # if forward
        list = range(index + direction, len(tokens), direction)

    for i in list:
        token = tokens[i]
        if token == "(":
            parensCount -= 1
        if token == ")":
            parensCount += 1
        if parensCount == 0:
            break
        else:
            subStatment.append(token)

    # read the parens from the statment
    # since it losses one depending on the direction
    # this could be fixed depending on a refactor

    final = ""
    if direction < 0:
        final = "("
    for s in subStatment[::direction]:
        final += " " + s
    if direction > 0:
        final += " )"
    return final


def __connectSubSetAndWffBefore__(sub, token, post):
    return sub + " " + token + " " + post


def __connectSubSetAndWffAfter__(sub, token, pre):
    return pre + " " + token + " " + sub


def sortStatments(statments):
    statments.sort()
    statments.sort(key=len)


def getStatments(input):
    params = []
    statmentTokens = input.split(" ")

    statments = __getSubStatments__(statmentTokens)
    input = replaceSubStatmentsWithTags(input)

    print(input)

    for pos in range(1, len(statmentTokens) - 1):

        # get the token from the statment
        token = statmentTokens[pos]
        lastToken = statmentTokens[pos - 1]
        nextToken = statmentTokens[pos + 1]
        # if the token is a variable
        if (token not in keyTokens):
            params.append(token)

        # if the token is a key value such as "and" or "or"
        if (token in keyTokens and (token != "(" and token != ")")):
            # the "and" case e.g q and p
            if not __tokenIsParens__(lastToken) and not __tokenIsParens__(nextToken) and token == "and":
                newStatment = lastToken + " " + token + " " + nextToken
                statments.append(newStatment)

            if __tokenIsParens__(lastToken) and __tokenIsParens__(nextToken):
                prev = __connectSubSetandWff__(statmentTokens, pos, -1)
                next = __connectSubSetandWff__(statmentTokens, pos, 1)
                subStatmentToAdd = __connectSubSetAndWffBefore__(prev, token, next)
                statments.append(subStatmentToAdd)

            elif lastToken == ")":
                # get the subStatment
                subStatmentToAdd = __connectSubSetandWff__(statmentTokens, pos, -1)
                subStatmentToAdd = __connectSubSetAndWffBefore__(subStatmentToAdd, token, nextToken)
                statments.append(subStatmentToAdd)

            elif nextToken == "(":
                subStatmentToAdd = __connectSubSetandWff__(statmentTokens, pos, 1)
                subStatmentToAdd = __connectSubSetAndWffAfter__(subStatmentToAdd, token, lastToken)
                statments.append(subStatmentToAdd)

    returnValue = []
    for statment in statments:
        if statment not in returnValue:
            returnValue.append(statment)

    sortStatments(returnValue)

    return [params, returnValue]

