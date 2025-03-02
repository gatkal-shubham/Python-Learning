x=3+4
print(x)
print(int.__add__(3,4))

# .whenever we use +,-,* / behind the seen it calls inbuilt functions/methods like int.__add__(3,4),int.__sub__(3,4),int.__mul__(3,4) 
# because all these methods are already defined for int,float etc datatypes

# in below code when we write stud3=stud1 + stud2 it will give error (i.e. unsupported operand type(s) for +: 'Student' and 'Student')
# because we haven't defined .__add__(self,other) for Student dataype/class  
# to avoid this problem we can define(overload) the .__add__(self,other) method in Student class
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): # operator overloading
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        stud3=Student(m1,m2)
        return stud3
    def __gt__(self,other):
        stud1=self.m1+self.m2
        stud2=other.m1+other.m2
        if stud1>stud2:
            return True
        else:
            return False
    
stud1=Student(34,54)
stud2=Student(89,90)

stud3=stud1 + stud2 # this will give error (i.e. unsupported operand type(s) for +: 'Student' and 'Student')
print(stud3.m1)

if stud1 > stud2:
    print("Student 1 wins")