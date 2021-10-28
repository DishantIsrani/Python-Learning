# class Number: #should be in PascalCase
#     def sum(self):
#         return self.a +self.b

# # this next line is an object instantition 
# # an object(application) is an instantition of the class(template). without that the memory is not allocated
# num = Number()

# num.a = 12
# num.b = 23
# s = num.sum()
# print(s)


class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

dishantsApplication = RailwayForm()
dishantsApplication.name = "Dishant"
dishantsApplication.train = "Rajdhani Express"
dishantsApplication.printData()
 



class Employee:
    compamy="Google"
    salary = 100


harry = Employee()
# this is an instance attribute 
kunal.salary =300

rajni = Employee()
# this is an instance attribute 
newuser.salary =400

print(kunal.compamy)
print(newuser.compamy)

Employee.compamy= "youtube"
print(kunal.compamy)
print(kunal.salary)

print(newuser.compamy)
print(newuser.salary)





class Employee:
    company = "Google"
    def getSalary(self):  #self is a paramater that is passed automatically 
        print(f"salary is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getSalary()   # Employee.getSalary(harry) both are same as we use self
