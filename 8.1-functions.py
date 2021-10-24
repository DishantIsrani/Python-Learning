def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45, 56, 78, 90]
percentage1 = percent(marks1)


marks2 = [65, 76, 98, 90]
percentage2 = percent(marks2)

print(percentage1, percentage2)


# Quiz 
# DEFAULT ARGUEMENTS 
# IF IN BELOW GREET STATEMENT IF ONE DOESNT ADD NAME IT WILL TAKE STRANGER AS A DEFAULT ARGUEMENT 
def greet(name = "STRANGER: as no arguement was passed in greet"):
    print("Good day," + name)

greet("Dishant")
greet()
