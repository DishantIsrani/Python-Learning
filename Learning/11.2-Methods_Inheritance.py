# # CLASS MEHTODS

# class Employee:
#     company ="camel"
#     salary = 100
#     location = "mumbai"

#     def ChangeSalary(self, sal):
#         self.__class__.salary = sal

#     # THE EASY METHOD FOR THE ABOVE STATEMENT AND FOR THE CLASS ATTRIBUTE IS
#     @classmethod
#     def ChangeSalary(cls, sal):
#         cls.salary = sal


# e = Employee()
# print("this is e.salary obj of employee************",e.salary)
# print("this is of employee**********",  Employee.salary)
# e.ChangeSalary(455)
# print("this is the e .salary obj after using e.changeSalary method so this is an instance*************", e.salary)
# print("This is the same Employee that hasnt been changed even after we use e.chanegSalary************", Employee.salary)
















# PROPERTY DECORATOR
class Employee:
    company = "Bharat Gas"
    salary =4500
    salaryBonus= 500
    # totalSalary = 5000 

# ALSO CALLED AS GETTER METHOD 
    @property
    def totalSalary(self):
        return self.salary +self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e= Employee()
print(e.totalSalary)
e.totalSalary = 4900
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)
