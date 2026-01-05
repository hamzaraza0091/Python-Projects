from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age,salary):
        self.name  = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary

    @abstractmethod
    def work(self):
        pass

 
class Chairman(Person):
    def work(self):
        return f"{self.name} is The Chairman of this Company."
    
class Secretray(Person):
    def work(self):
        return f"{self.name} is The Personal Secretray Of Chariman who manage Everything."
    
class Advisior(Person): 
    def work(self):
        return f"{self.name} Is the Advisior of The Company who give the Advice."

class Manager(Person):
    def work(self):
        return f"{self.name} is The Manager of The company He Manages Employees and Tasks."
    
class Employee(Person):
    def work(self):
        return f"{self.name} She is the Employee in this Company She works on assigned Tasks."
    
class OfficeBoy(Person):
    def work(self):
        return f"{self.name} is an OfficeBoy he maintain Office Cleanliness and support."
    

class Company:
    def __init__(self,name):
        self.name = name
        self.staff = []


    def add_person(self,person):
        self.staff.append(person)
    
    def company_structure(self):
        print(f"\nCompany Name: {self.name}")
        print("-" * 40)


        for p in self.staff:
            print(p.work())

if __name__ == "__main__":


    company = Company("Al_Ansar Group of Tech")

    chairman = Chairman("Hamza", 22, 5000000)
    secretray = Secretray("Ahmed", 30, 6000000)
    advisior = Advisior("Bilal", 35, 300000)
    manager = Manager("Sara", 27, 150000)
    employee = Employee("Sana", 25, 80000)
    officeboy = OfficeBoy("Usman", 26, 45000)
    
    company.add_person(chairman)
    company.add_person(secretray)
    company.add_person(advisior)
    company.add_person(manager)
    company.add_person(employee)
    company.add_person(officeboy)

    company.company_structure()
    