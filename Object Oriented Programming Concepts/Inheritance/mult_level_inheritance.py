# Class A is Parent class , Class B is derived from class A and Class c is derived from class b which is multi-level-Inheritance
class A:
    def feature1(self):
        print("Feature 1 of class A")
    def feature2(self):
        print("Feature 2 of class A")
        
class B(A):
    def feature3(self):
        print("Feature 3 of class B")
    def feature4(self):
        print("Feature 4 of class B")

class C(B):
    def feature5(self):
        print("Feature 5 of class C")
    
        
        
c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()