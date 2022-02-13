class TokenList:
    tokens = {

    }

    def __init__(self):
        self.tokens = {}

    def add_token(this,new_token):
        for tokenValue in this.tokens.values():
            if not tokenValue.is_equivilent(new_token):
                key = "S-" + str(len(this.tokens))
                this.tokens[key] = new_token

        for key,value in this.tokens.items():
            value = this.translate_statement_to_keys(value)
            this.tokens[key] = value



    def add_multiple_token(this,new_token_list):
        for token in new_token_list:
            this.add_token(token)

    def get_token(this,key):
        return this.tokens[key]

    def get_dict(self):
        return self.tokens

    def get_keys(self):
        return self.tokens.keys()

    def get_values(self):
        return self.tokens.values()

    def print_values(self):
        for key,value in self.tokens.items():
            print(key,"\t",value)

    def translate_keys_to_statement(self,statement):
        for key in self.tokens.keys():
            if key in statement:
                replaceWith = "( " + self.tokens[key] + " )"

                newStatement = statement.replace(key, replaceWith).strip()

                if newStatement == replaceWith:
                    statement = statement.replace(key, self.tokens[key])
                else:
                    statement = newStatement
        return statement.strip()

    def translate_statement_to_keys(self,statement):
        return_value = statement
        last_return_value = statement
        for key, value in self.tokens.items():

            if value in statement:
                return_value = statement.replace(value, key)
                return_value = return_value.replace("( " + key + " )", key)  # in case there are ()

            #if this is converted into a simple key revert it...
            if return_value in self.tokens.keys():
                return_value = last_return_value

            last_return_value = return_value

        if return_value != statement:
            return_value = self.translate_statement_to_keys(return_value)


        return return_value
