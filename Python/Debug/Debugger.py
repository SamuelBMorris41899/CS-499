class Debugger:
    def __init__(self,debugging = True):
        self.debug = debugging

    def log(self, *message, seperator = "\t", end_of_statement = "\n"):
        if self.debug:
            for m in message:
                print(m,end=seperator)
            print(end = end_of_statement)