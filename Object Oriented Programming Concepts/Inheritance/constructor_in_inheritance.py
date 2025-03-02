""" 1. If you create an object of Sub class, it will first try to find the init of sub class
       if it is not found then it will call init of super class 
    2. (for single level inheritance) if both class has there own constructors and if we create an object of sub class 
        then by default it will call constructor of sub class but if you want to call constructor of parent/super class 
        then we make use of "super" keyword(i.e. super().__init__())  
    3. (for multiple inheritance) if we use super keyword then it will follow "Method resolution Order"(i.e left to right) 
        if we define it as " class C(A,B): " and if we use "super keyword init of class c then it will call constructor of class A because 
        while defineing A is on leftmost side
        or if we define it as " class C(B,A): " and if we use "super keyword init of class c then it will call constructor of class B because 
        while defining B is on leftmost side    
"""

# class A:
    
#     def __init__(self):
#         print("class A init")
        
#     def feature1(self):
#         print ("Feature 1 of class A")
#     def feature2(self):
#         print ("Feature 2 of class A")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Class B init")
        
#     def feature3(self):
#         print ("Feature 3 of class B")
#     def feature4(self):
#         print ("Feature 4 of class B")
        
# b1=B()

class A:
    
    def __init__(self):
        print("class A init")
        
    def feature1(self):
        print ("Feature 1 of class A")
    def feature2(self):
        print ("Feature 2 of class A")

class B:
    def __init__(self):
        print("Class B init")
        
    def feature3(self):
        print ("Feature 3 of class B")
    def feature4(self):
        print ("Feature 4 of class B")
        
class C(B,A):
    def __init__(self):
        super().__init__()
        print("Class c init")
        
    def feature5(self):
        print("feature 5 of class C")
        
c1=C()