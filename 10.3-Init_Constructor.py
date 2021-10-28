class Employee:
    company = "Google"

    # __init__ will run the method automatically and it is called the constructor  
    def __init__(self, name, salary, subunit):
        self.name =name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")

    def getSalary(self, signature):  #self is a paramater that is passed automatically 
        print(f"salary is {self.salary}\n{signature}")

    @staticmethod
    def greet():  #no self in static in method
        print("Good Morning, Sir")


dishant = Employee("Dishant", "100k", "youtube")
dishant.getDetails()