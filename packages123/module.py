class Calsi:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    
class Math:
    def power(a,b):
        return a**b
    def isEven(n):
        if n%2==0:
            return "Even"
        return "Odd"
    
class Calsi1:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def __add__(self):
        return self.v1+self.v2
    def __mul__(self):
        return self.v1*self.v2