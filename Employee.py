class Employee:
    #declaring class variables
    no_of_emps=0
    raise_amount=1.04

    def __init__(self, first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

        Employee.no_of_emps+=1

    @property
    def email(self):    #uses the method as an attribute
        return "{}.{}@gmail.com".format(self.first,self.last)

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

    #special (dunder) methods
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.fullname(),self.email,self.pay)
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __eq__(self,other):
        return self.pay==other.pay
    def __len__(self):
        return len(self.fullname())    

#Developer and Manager classes are inheriting from class Employee
class Developer(Employee):
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
    
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)

    def __repr__(self):
        return "Developer('{}','{}',{},'{}')".format(self.fullname(),self.email,self.pay,self.prog_lang)
    def __str__(self):
        return "{} - {} - {}".format(self.fullname(),self.email,self.prog_lang)
    def __add__(self,other):
        return self.pay + other.pay
    def __eq__(self,other):
        return self.pay==other.pay
    def __len__(self):
        return len(self.fullname())
    
class Manager(Employee):
    raise_amount=1.15

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees==None:
            self.employees=[]
        else:
            self.employees=employees
    
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)
    
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def list_employees(self):
        for emp in self.employees:
            print("-->",emp.fullname())

    def __repr__(self):
        return "Manager('{}','{}',{})".format(self.fullname(),self.email,self.pay)
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __eq__(self,other):
        return self.pay==other.pay
    def __len__(self):
        return len(self.employees)


dev1=Developer("John","Doe",85000,"Python")
dev2=Developer("Jane","Doe",85000,"Java")

print(dev1)
print(dev2)
print(dev1==dev2)
dev2.apply_raise()
print(dev1==dev2)
print(dev1 + dev2)
print(len(dev1))

mgr=Manager("Pavitra","Prabhakar",95000,[dev1])
print(repr(mgr))
mgr.list_employees()
mgr.add_employee(dev2)
mgr.list_employees()
print(len(mgr))



