# class Dog:
#     species="Cnaine"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# dog1=Dog("Buddy",3)
# dog2=Dog("Charlie",5)

# print(dog1.name,dog1.age,dog1.species)
# print(dog2.name,dog2.age,dog2.species)

class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
    def config(self):
        print("Configuration is: ","processor: ",self.cpu,"RAM: ", self.ram)
        
    def comapare(self,other):
        if(self.ram==other.ram):
            return True
        else:
            return False
        
com1=Computer("i5",16)
com2=Computer("i6",16)

if com1.comapare(com2):
    print("They have same RAM")


com1.config()
        