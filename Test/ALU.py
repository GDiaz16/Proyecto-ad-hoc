
class ALU:

    def add(self, a,b):
        return a+b

    def substract(self,a,b):
        return a-b

    def divide(self,a,b):
        return a/b

    def multiply(self,a,b):
        return a*b

    def AND(self,a,b):
        return a and b

    def OR(self,a,b):
        return a or b

    def XOR(self,a,b):
        return not (a and b) and (a or b)

    def NOT(self,a):
        return not a
