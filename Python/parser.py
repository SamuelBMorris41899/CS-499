from Token import Token
import re

class parser:
    key_tokens = ["or","and","(",")","not","nor","nand","xor","=>","="]

    def __init__(self,statement):
        self.statement=statement
        self.hyps = Token()#move to prop logic

        self.subStatments = Token()
        subs = self.get_sub_statements(statement)
        self.subStatments.add_multiple_token(subs)

    def get_sub_statements(this, statement):
        sub_statements = []
        sub_statement = ""
        parens = 0
        for char_position in range(len(statement)):
            char = statement[char_position]
            if char == "(":
                parens += 1
            elif char == ")":
                parens -= 1

            if parens != 0:
                sub_statement += char

            if sub_statement != "" and parens == 0:
                sub_statement = sub_statement[1:]
                sub_statement = sub_statement.strip()
                sub_statements.append(sub_statement)
                sub_statement = ""


        for sub in sub_statements:
            if "(" in sub and ")" in sub:
                sub_statements += this.get_sub_statements(sub)

        return sub_statements

    def get_atoms(self, statement):
        statement = self.subStatments.translate_statement_to_keys(statement)
        variables = re.split('and',statement)
        # variables = statement.split("and")
        variables = list(set(variables))
        for pos in range(len(variables)):
            v = variables[pos]
            v = self.subStatments.translate_keys_to_statement(v)
            variables[pos] = v

        return variables

    def dealWith_A_keyToken_B (self,tokens, context):

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
            if c in tokens:
                index = tokens.index(c)
                if (lowestIndex < index):
                    lowestIndex = index

        if (index == -1):
            return []

        index = lowestIndex
        token = tokens[lowestIndex]
        last = tokens.pop(index - 1)
        next = tokens.pop(index)

        newToken = last + " " + token + " " + next
        returnValue.append(newToken)
        tokens[index - 1] = newToken

        tokenToAdd = self.dealWith_A_keyToken_B(tokens, context)
        returnValue += tokenToAdd
        return returnValue














    '''
    move to prop logic
    '''
    def deductionMethod(self,statement):
        if "=>" in statement:
            end = statement.find("=>")
            lookAt = statement.strip()
            sub_parse = parser(lookAt)
            return sub_parse.get_hypotheses()
        return []

    def get_hypotheses(self):
        translate = self.subStatments.translate_statement_to_keys(self.statement)
        get_from = ""
        add=[]
        if "=>" in translate:
            get_from = translate.split("=>")[0]
            atoms = self.get_atoms(get_from)  # hypos!, in their most basic form
            for key in get_from.split(" "):
                if key in self.subStatments.get_keys():
                    self.hyps.add_token(self.subStatments.get_token(key))

            get_to = translate.split("=>")[1]
            get_to = self.subStatments.translate_keys_to_statement(get_to)
            add = self.deductionMethod(get_to)
        else:
            get_from = translate

        retValue = [i for i in atoms] + add
        return retValue
