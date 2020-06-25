class Employee:
    def __init__(self, first,last,pay):
        self.first=first
        self.last=last
        self.email="{}.{}@gmail.com".format(first,last)
        self.pay=pay
    def fullname(self):
        return "{} {}".format(self.first,self.last)

emp1=Employee("Ramesh","Nanavati",75000)
emp2=Employee("Raghav","Shukla",70000)

print(emp1.email)   #outputting the attribute of the instance

#2 ways of calling class methods
print(emp1.fullname())
print(Employee.fullname(emp2))
