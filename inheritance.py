class Person:
    def work(self):
        print("person working")
class Doctor(Person):
    def treat(self):
        print(" Doctor treats")
class Patient(Doctor):
    def sick(self):
        print("sickling")
d=Patient() 
d.treat()
d.work() 
d.sick()  

