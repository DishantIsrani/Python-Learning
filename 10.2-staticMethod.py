class Employee:
    company = "Google"

    def getSalary(self, signature):  #self is a paramater that is passed automatically 
        print(f"salary is {self.salary}\n{signature}")

    @staticmethod
    def greet():  #no self in static in method
        print("Good Morning, Sir")


dishant = Employee()
dishant.salary = 10000
# dishant.getSalary()   # Employee.getSalary(dishant) both are same
dishant.getSalary("Thanks!")  # This inside the bracket is a signature

dishant.greet()  #Employee.greet(dishant)






