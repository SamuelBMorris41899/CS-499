class InvalidExpression(Exception):
    def __init__(self):
        super()
        self.message = "Invalid Expression"

    def __str__(self):
        return f'{self.message}'