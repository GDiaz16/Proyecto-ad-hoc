import random


class Pack:
    def __init__(self, header, data, target, origin = "", path = "N", check = -1):
        self.path = path
        self.header = header
        self.data = data
        self.target = target
        self.origin = origin
        if check >= 0 :
            self.check = check
        else:
            self.check = random.uniform(0,10)




