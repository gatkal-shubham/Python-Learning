class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap1=self.Laptop()
        
    def show(self):
        print("name: ",self.name,"rollno: ",self.rollno)
        
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
            
        def show(self):
            print("brand: ",self.brand,"CPU: ",self.cpu,"RAM: ",self.ram)
            
stud1=Student("Shubham",11)

stud1.show()
stud1.lap1.show()