class Employee:
    #declaring class variables
    no_of_emps=0
    raise_amount=1.04

    def __init__(self, first,last,pay):
        self.first=first
        self.last=last
        self.email="{}.{}@gmail.com".format(first,last)
        self.pay=pay

        Employee.no_of_emps+=1

    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay*=self.raise_amount


#initializing the class instances
emp1=Employee("Ramesh","Nanavati",75000)
emp2=Employee("Raghav","Shukla",70000)

#2 ways of calling class methods
print(emp1.fullname())
print(Employee.fullname(emp2))

print(emp1.email)   #outputting the attribute of the instance
print(emp2.email)

emp2.apply_raise()
print(emp2.pay)

print(emp1.__dict__)
emp1.raise_amount=1.05
print(emp1.raise_amount)
print(Employee.raise_amount)
print(emp1.__dict__)