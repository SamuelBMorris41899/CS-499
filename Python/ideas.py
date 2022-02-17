class Ideas:
    def smart_conjenction(self, token):
        statement = ""
        # are all atoms of the target proven?
        all_proven = True
        for t in self.target_atoms:
            if t not in self.proven:
                all_proven = False
                break

        if all_proven:
            for t in self.target_atoms:
                statement = f" {token} ".join(self.target_atoms).strip()
                statement = f"( {statement} )"
                self.add(statement)

        # so we can't just "add" our way to victory? what now
        # can we find a way to set up mp?
        for statement in self.translated_proven:
            statement = self.lookup_table.translate_statement_to_keys(statement).strip(" ()")
            print("proven statements", statement)
            if "=>" in statement and self.target in statement:
                # try to prove part 1.
                before = statement.split("=>")[0]
                before = self.lookup_table.translate_keys_to_statement(before)
                before = before[1:len(before) - 1].strip()
                before = before.split(" and ")
                size = len(before)
                if size == 2:
                    print("IN HERE!")
                    all_proven = False
                    for token in before:
                        if token not in self.proven and token not in Rules.keyTokens:
                            print("something not proven!")
                            all_proven = False
                    if all_proven:
                        statement = f" {token} ".join(self.target_atoms).strip()
                        statement = f"the statement we are adding is: ( {statement} )"
                        print(statement)
                        self.add(statement)

