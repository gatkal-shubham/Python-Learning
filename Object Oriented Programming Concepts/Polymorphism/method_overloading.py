# Python does not directly support method overloading but we can implement it inderectly
class Operations:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a !=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
op1=Operations()
print(op1.sum(1,2,10)) 
print(op1.sum(1)) 
print(op1.sum(1,2)) 
print(op1.sum())