class TokenList:
    def __init__(self):
        self.tokens = {}

    def add_token(self,token_to_add):

        if token_to_add not in self.tokens.values():
            key = f"S-{len(self.tokens.items())}"
            self.tokens[key] = token_to_add
        self.fix_tokens()

    def fix_tokens(self):

        for key,value in self.tokens.items():
            value = self.translate_statement_to_keys(value)
            self.tokens[key] = value

    def add_all_tokens(self,tokens_to_add):
        for token in tokens_to_add:
            self.add_token(token)

    def add_all_tokens_from_token_list(self,token_list_merge):
        tokens_to_add = []
        for token in list(token_list_merge.tokens.values()):
            to_add = token_list_merge.translate_keys_to_statement(token)
            tokens_to_add.append(to_add)
        self.add_all_tokens(tokens_to_add)


    '''
        expects a string input
    '''
    def translate_keys_to_statement(self,statement):
        for key in self.tokens.keys():
            if key in statement:
                replaceWith = self.tokens[key]

                newStatement = statement.replace(key, replaceWith).strip()

                if newStatement == replaceWith:
                    statement = statement.replace(key, self.tokens[key])
                else:
                    statement = newStatement
        return statement.strip()

    def translate_statement_to_keys(self,statement,translate_down_to_single_statement = False):
        return_value = statement
        last_return_value = statement
        for key, value in self.tokens.items():

            if value in statement:
                return_value = statement.replace(value, key)
                return_value = return_value.replace("( " + key + " )", key)  # in case there are ()

            if not translate_down_to_single_statement:
                #if this is converted into a simple key revert it...
                if return_value in self.tokens.keys():
                    return_value = last_return_value

            last_return_value = return_value

        if return_value != statement:
            return_value = self.translate_statement_to_keys(return_value)


        return return_value


    '''
        makes a string of all entries in the tokens list
    '''
    def to_string(self):
        string = ""
        for key,value in self.tokens.items():
            string += "{:<5}\t{}\n".format(key,value)

        return string
