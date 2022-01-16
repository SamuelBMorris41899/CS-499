import ttg


# inputString = "( a and c ) or p or q->q'"
# #inputString = "p or q->q'"
# statmentSplit = inputString.split("->")
# predicate = statmentSplit[0]


# def parentheses(string):
#     newTokens = []

#     if(string == ""):
#         return newTokens

#     token = ""
#     inParens = False
#     for charLocation in range(len(string)):
#         char = string[charLocation]
#         # if(char == "(" and inParens): #(a or (b or c)) LATER
#         #     newTokens += parentheses(string[charLocation:])
#         #     continue
        
#         if(inParens):
#             token = token + char

#         if(char == "("):
#             token = token + char
#             inParens = True
#         if(char == ")"):
#             newTokens.append(token)
#             token = ""
#             inParens = False
#     return newTokens


# predicateTokensRaw = predicate.split(' ')
# statments = getToken(predicateTokensRaw)


# #statments = parentheses(predicate)
# print(statments)




print(ttg.Truths(["a","p","( a and p )"]))