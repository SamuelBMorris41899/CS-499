class Token:
    tokens = {

    }

    def __init__(self):
        self.tokens = {}

    def add_token(this,new_token):
        key = "statement_" + str(len(this.tokens))
        this.tokens[key] = new_token

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
                statement = statement.replace(key, "( " + self.tokens[key] + " )")

        return statement

    def translate_statement_to_keys(self,statement):
        return_value = statement

        for key, value in self.tokens.items():
            if value in statement:
                return_value = statement.replace(value, key)
                return_value = return_value.replace("( " + key + " )", key)  # in case there are ()

        if return_value != statement:
            return_value = self.translate_statement_to_keys(return_value)
        return return_value
