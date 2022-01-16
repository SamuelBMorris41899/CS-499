#get sub statments
keyTokens = {
    "V":"or",
    "N":"and",

    "or":"or",
    "and":"and",
    "(":"",
    ")":"",
}

def tokenIsParens(token):
    return (token == "(" or token == ")")
def buildSubStatments(tokens):
    subStatments = []
    subStatment = ""
    numSubStatment = 0

    for token in tokens:

        if(token == "("):
            numSubStatment -= 1 
        
        if(token == ")"):
            numSubStatment += 1
        
        if(numSubStatment != 0):
            subStatment += " " + token

        if (numSubStatment == 0 and subStatment != ""):
            final = subStatment[3:]
            subStatments.append(final) #remove leading space
            subStatment = ""
    return subStatments
def getSubStatments(tokens):
    print("Tokens given")
    print(tokens)
    subStatments = buildSubStatments(tokens)
    
    #recursion to get statments inside of the substatment
    returnValue = []
    for statment in subStatments:
        finalStatment = statment
        statments = statment.split(' ')
        recursive = getSubStatments(statments)
        returnValue +=  [finalStatment] + recursive
        
    return returnValue
    
def connectSubSetandWff(tokens,index,direction):

    subStatment = []
    parensCount = 0
    #this will determine which way the function is looking.
    list = []
    if(direction < 0):
        #if backward
        list = range(index + direction,0,direction)
    else:
        #if forward
        list = range(index+direction,len(tokens),direction)

    for i in list:
        token = tokens[i]
        print(token)
        if(token == "("):
            parensCount -= 1
        if(token == ")"):
            parensCount += 1

        if(parensCount == 0):
            print("parensCount " + str(parensCount))
            break
        else:
            subStatment.append(token)
            print(subStatment)
    
    #readd the parens from the statment
    #since it losses one depending on the direction
    #this could be fixed depending on a refactor
    final = ""
    if(direction < 0):
        final = "("
    for s in subStatment[::direction]:
        final += " " + s
    if(direction > 0):
        final += " )"    
    return final

def connectSubSetAndWffBefore(sub,token,post):
    return sub + " " + token + " " + post

def connectSubSetAndWffAfter(sub,token,pre):
    return pre + " " + token + " " + sub
    

def getStatments(input,statmentTokens):
    
    statments = getSubStatments(statmentTokens)

    for pos in range(1,len(statmentTokens)-1):
        
        #get the token from the statment
        token = statmentTokens[pos]
        lastToken = statmentTokens[pos - 1]
        nextToken = statmentTokens[pos + 1]
        #if the token is a variable
        if(token not in keyTokens):
            statments.append(token)

        #if the token is a key value such as "and" or "or"
        if(token in keyTokens and (token != "(" and token != ")")):
            #the "and" case e.g q and p
            if ( not(tokenIsParens(lastToken)) and not(tokenIsParens(nextToken)) and token == "and"):
                newStatment = lastToken + " " + token + " " + nextToken
                statments.append(newStatment)

            if (lastToken == ")"):

                #get the subStatment
                subStatmentToAdd = connectSubSetandWff(statmentTokens,pos,-1)
                subStatmentToAdd = connectSubSetAndWffBefore(subStatmentToAdd,token,nextToken)
                statments.append(subStatmentToAdd)

            if (nextToken == "("):
                subStatmentToAdd = connectSubSetandWff(statmentTokens,pos,1)
                subStatmentToAdd = connectSubSetAndWffAfter(subStatmentToAdd,token,lastToken)
                statments.append(subStatmentToAdd)
    returnValue = [] 
    for statment in statments:
        if statment not in returnValue:
            returnValue.append(statment)
    return returnValue

inputString = "( ( a or c ) and d ) or p and q"

# inputString = "q and p or ( a or c )"

print(getStatments(inputString,inputString.split(" ")))