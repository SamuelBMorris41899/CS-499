from Token import Token

class parser:
    key_tokens = ["or","and","(",")","not","nor","nand","xor","=>","="]


    def __init__(self):
        self.hyps = Token()
        self.subStatments = Token()

    def get_high_level_substatements(this,statement):
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


        return sub_statements

    def get_atoms(self, statement):
        statement = self.hyps.translate_statement_to_keys(statement)
        removed_key_tokens = statement
        for key_token in self.key_tokens:
            if key_token in removed_key_tokens:
                removed_key_tokens = removed_key_tokens.replace(key_token,"")
        for key in self.hyps.get_keys():
            if key in removed_key_tokens:
                removed_key_tokens = removed_key_tokens.replace(key,"")
        removed_key_tokens = removed_key_tokens.replace(" ", "")

        variables = list(set([i for i in removed_key_tokens]))

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

    def deductionMethod(self,statement):
        if "=>" in statement:
            end = statement.find("=>")
            lookAt = statement.strip()
            sub_parse = parser()
            return sub_parse.get_Hypotheses(lookAt)
        return []

    def get_Hypotheses(self, statement):
        subs = self.get_high_level_substatements(statement)
        self.subStatments.add_multiple_token(subs)

        translate = self.subStatments.translate_statement_to_keys(statement)
        get_from = ""
        add=[]
        if "=>" in translate:
            get_from = translate.split("=>")[0]

            for key in get_from.split(" "):
                if key in self.subStatments.get_keys():
                    self.hyps.add_token(self.subStatments.get_token(key))

            get_to = translate.split("=>")[1]
            get_to = self.subStatments.translate_keys_to_statement(get_to)
            add = self.deductionMethod(get_to)
        else:
            get_from = translate



        a = get_from.split("and")
        return [self.hyps.translate_keys_to_statement(i) for i in a] + add
