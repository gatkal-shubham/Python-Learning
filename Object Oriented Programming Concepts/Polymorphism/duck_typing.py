
""" Duck Typing: 
1. If there is a bird which is waking like a bird ,quaking like a bird and swimming like a duck then that bird is duck which simply means it doesn't matter it is duck or not ,what matters is if behavior of that bird is mathching with duck that means its a duck
    ( if it looks like duck swims like a duck, then it probably is a duck).
    Dynamic typing : means the type you can mention later
    
"""
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
    
class MyEditor:
    def execute(self):
        print("Spell checking")
        print("COnvention Checking")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()
        
ide=PyCharm()
lap1=Laptop()
lap1.code(ide)
 