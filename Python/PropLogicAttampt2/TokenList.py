class TokenList:
    def __init__(self):
        self.tokens = {}

    def add_token(self,token_to_add):
        key = f"S-{len(self.tokens.items())}"
        self.tokens[key] = token_to_add

    def add_all_tokens(self,tokens_to_add):
        for token in tokens_to_add:
            self.add_token(token)

    def add_all_tokens_from_token_list(self,token_list_merge):
        self.add_all_tokens(list(token_list_merge.tokens.values()))

    '''
        makes a string of all entries in the tokens list
    '''
    def to_string(self):
        string = ""
        for key,value in self.tokens.items():
            string += f"{key}\t{value.value}\n"

        return string
