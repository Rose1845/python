class Employee:
 def __init__(self,name,id):
     self.name=name;
     self.id=id;
 def display(self):
     print("id: %d \nname: %s"%(self.id,self.name))
emp = Employee("rose",13)
emp.display()