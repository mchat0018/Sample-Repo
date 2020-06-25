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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    
    @classmethod
    def init_from_String(cls,empString):    #class method as an alternate constructor
        first,last,pay=empString.split("-")
        return cls(first,last,float(pay))


#initializing the class instances
emp1=Employee("Ramesh","Nanavati",75000)
emp2=Employee("Raghav","Shukla",70000)

#using the alternate constructors made by a class method
emp3=Employee.init_from_String("John-Doe-60000")
emp4=Employee.init_from_String("Jane-Doe-60000")

#2 ways of calling class methods
print(emp1.fullname())
print(Employee.fullname(emp2))

print(emp1.email)   #outputting the attribute of the instance
print(emp3.email)

#modify raise using class method
Employee.set_raise_amt(1.05)
emp2.apply_raise()
emp4.apply_raise()
print(emp2.pay)
print(emp4.pay)