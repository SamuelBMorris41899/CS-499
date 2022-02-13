class ParenError(Exception):
    def __init__(self,o,c):
        super()
        self.message = "bad number of parens"
        self.message += f"\n\topen   = {o}"
        self.message += f"\n\tclosed = {c}"

    def __str__(self):
        return f'{self.message}'