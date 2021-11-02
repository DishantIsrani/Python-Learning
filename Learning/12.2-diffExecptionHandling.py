# try:
#     a = int(input("enter a number:"))
#     c =1/a
#     print(c)
# except ValueError as e:
#     print("Execption 1 occured! please enter a valid value")
#     # print(e)

# except ZeroDivisionError as e:
#     print("Execption 2 occured! Dont divide by 0")
#     # print(e)

# print("Thanks!")






# # RAISING EXECPTION

# def increment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ValueError("This is a value error")

# a = increment(45)
# print(a)
# increment('233wef')
# print(a)











# # TRY WITH ELSE
# # if try works then else will be printed or except will be printed

# try:
#     i = int(input("enter a number: "))
#     c = 1/i
# except Exception as e:
#     print(e)
# else:
#     print("we were successful and in else block now")







# # TRY WITH FINALLY 
# # EXECUTION OF PIECE OF CODE IRRESPECTIVE OF THE EXECPTION
# # FINALLY WILL RUN NO MATTER IF THE CODE IS RIGHT OR WRONG EVEN IF WE EXIT THE CODE AT EXCEPT IT WILL STILL WORK
# try:
#     i = int(input("enter a number: "))
#     c = 1/i
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print("we were Done and in the finally block now")
#     print("this will run always no matter what happens")

# print("this will run only if the try works and will not run in except as it exits the code there")

