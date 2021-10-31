# # GLOBAL KEYWORD
# a = 54  # GLOBAL VARIABLE

# def func1():
#     global a # this will change the global variable to the value in function that is 8 
#     print("inside the function after saying to use global a and before changing a is", a)
#     a=8 # LOCAL VARIABLE IF GLOBAL KEYWORD IS NOT USED
#     print("inside the function", a)
    

# func1()
# print("outside the function", a)











# # ENUMERATE FUNCTION to index of list 

# list1= [3, 5, 6, "dishant", 6.7, False]

# # index = 0
# # for item in list1:
# #     print(item, index)
# #     index += 1

# # the above 4 line and below 2 line are same
# for index, item in enumerate(list1):
#     print(index, item)













# # LIST COMPREHENSION 
# a =[8,9, 10, 2, 4, 6, 4, 123, 56, 34, 5]
# # b=[]

# # for item in a:
# #     if item % 2 == 0:
# #         b.append(item)
# # print(b)

# # the above 5 line and below 2 lines are same 
# b = [i for i in a if i%2 == 0]
# print(b)



# SET COMPREHENSION 
t = [1, 2, 4, 5, 8, 9, 4, 8, 9, 10, 4, 5]
s= {i for i in t}
print(s)

