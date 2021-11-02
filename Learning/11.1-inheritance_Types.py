# # single inheritance 
# class Employee:
#     company = 'Google'

#     def showDetails(self):
#         print("This is an employee")

# class Programmer(Employee):
#     language = "Python"

#     def getLang(self):
#         print(f"the language is {self.language}")

#     #if there are two same method in base and child class the method of the child class will be used and it can be used to override the parent class(base)
#     def showDetails(self):
#         print("This is an programmer")

# e= Employee()
# e.showDetails()

# p = Programmer()
# p.showDetails()
# print(p.company)











# # MULTIPLE inheritance 


# class Employee:
#     company = "visa"
#     eCode= 120

# class FreeLancer:
#     company ="fiver"
#     level = 0

#     def upgradeLevel(self):
#         self.level = self.level + 1

# class Programmer(Employee, FreeLancer): #Employee class will be given priority as its written first in the function 
#     name = "Dishant"

# p = Programmer()
# print(" level before upgrading",p.level)
# p.upgradeLevel()
# print("After updgrading ",p.level)










# # MULTI LEVEL INHERITANCE 

# class Person:
#     country = "India"
#     def __init__(self):
#         print("Initializing Person")

    
#     def takeBreak(self):
#         print("I am breathing......")

# class Employee(Person): #employee will inherit the person class
#     company = "honda"
    
#     def __init__(self):
#         super().__init__()
#         print("Initializing Employee")
    

#     def getSalary(self):
#         print(f"salary is {self.salary}")

#     def takeBreak(self):
#         print("I am an employee so I am also breathing ")


# class Programmer(Employee):  
#     company ="fiverr"

#     def __init__(self):
#         super().__init__()
#         print("Initializing Programmer")

#     def getSalary(self):
#         print("no salary to the programmer")

#     def takeBreak(self):
#         super().takeBreak()
#         print("i am breathing ++ programmer ")


# p= Person()
# p.takeBreak()
# #p.company() #this will be an error

# e= Employee()
# e.takeBreak()
# print(e.company)

# pr =Programmer()
# pr.takeBreak()
# # print(pr.company)
# # print(pr.country)







