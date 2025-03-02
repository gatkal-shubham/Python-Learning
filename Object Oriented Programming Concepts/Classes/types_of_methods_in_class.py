""" Types of Methods in Class:
        1. Instance Method
        2. Class Method
        3. Static Method
"""
# Example: 
class Student:
    school="Telusko" # this is class Variable(because we decalred it outside the constructor)
    
    def __init__(self,m1,m2,m3):
        self.m1=m1 # this is Instance Variable(because we decalred it inside the constructor)
        self.m2=m2 # Instance Variable
        self.m3=m3 # Instance Variable
        
    # Instance method Example(which works with instance variables)
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)
    # Class Method Example(which make use of class variables)
    @classmethod
    def get_school_name(cls):
        return cls.school
    # Static Method Example(Which does not make use of Instance variables or class Varialbes)
    @staticmethod
    def static_method_example():
        print("This is Static Method because This does not make use of Instance variables or class Varialbes")
stud1=Student(34,45,69)
stud2=Student(55,56,89)

print(stud1.avg())
print(stud2.avg())
print(Student.get_school_name()) #calling class Method (we call it using class Name)
print(stud1.get_school_name())
print(stud1.static_method_example())
