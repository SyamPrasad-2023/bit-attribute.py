class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1:",self.var1)
        print("var2:",self.var2)
n1=int(input("enter n1:"))
n2=float(input("enter n2:"))
o=abc(n1,n2)
print("onject.__dict__",o.__dict__)
print("object.__doc__",o.__doc__)
print("class.__name__",abc.__name__)
print("object.__module__",o.__module__)
print("class.__base__",abc.__base__)