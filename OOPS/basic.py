class Employee:
    
    def __init__(self,eid,name,age,gender,desg):
        self.eid=eid
        self.name=name
        self.age=age
        self.gender=gender
        self.desg=desg
        
    def display(self):
        print("Employee Id: ",self.eid)
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Gender: ",self.gender)
        print("Employee Designation: ",self.desg)

emp=Employee("EMP123","Sanidhya Varshney",22,"M","Software Developer")
emp.display()
        