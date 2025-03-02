class A:
    def show(self):
        print("Inside shpw method of class A")
    
class B(A):
    def show(self):
        print("Inside Show method of class B")
        
b1=B()
b1.show()