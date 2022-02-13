class Debugger:
    def __init__(self,debugging = True):
        self.debug = debugging

    def log(self,message):
        if self.debug:
            print(message)