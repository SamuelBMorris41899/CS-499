from Token import Token

class parser:
    key_tokens = ["or","and","(",")","not","nor","nand","xor","=>","="]

    hyps = Token()


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

    def get_lone_variables(self, statement):

        statement = self.hyps.translate_statement_to_keys(statement)

        removed_key_tokens = statement

        for key_token in self.key_tokens:
            if key_token in removed_key_tokens:
                removed_key_tokens = removed_key_tokens.replace(key_token,"")
        for key in self.hyps.get_keys():
            if key in removed_key_tokens:
                removed_key_tokens = removed_key_tokens.replace(key,"")

        removed_key_tokens = removed_key_tokens.replace(" ", "")
        print(removed_key_tokens)

        variables = [i for i in removed_key_tokens]
        return variables




    def get_Hypotheses_Simple(this,statement):
        subs = this.get_high_level_substatements(statement)
        this.hyps.add_multiple_token(subs)          #add high level subStatments

        lone_variable = this.get_lone_variables(statement)
        this.hyps.add_multiple_token(lone_variable)  # add high level subStatments

        print(this.hyps.print_values())

        # print(subs)

        return list(this.hyps.get_values())
