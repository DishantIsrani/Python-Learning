# def square(num):
#     return num * num

# l = [1, 2, 4]
# # methd=od 1
# l2 = []
# for item in l:
#     l2.append(square(item))
# print(l2)

# #  METHOD 2 MAP
# print(list(map(square, l)))








# #FILTER FUNCTION  list(filter(function, input_list))

# def greater_than_5(num):
#     if num > 5:
#         return True
#     else:
#         return False

# g10 = lambda num :num>10

# l = [1,3,65, 7,5,2,45,63,35,646,5,2,4,35,64,235,6,4,2,]
# print(list(filter(greater_than_5, l)))
# print(list(filter(g10, l)))









# #  REDUCE METHOD
# from functools import reduce

# sum = lambda a,b: a+b
# # l = [1,3,65, 7,5,2,45,63,35,646,5,2,4,35,64,235,6,4,2]
# l = [1, 2, 3, 4]
# # will add all elements in list l
# val = reduce(sum, l)
# print(val)



