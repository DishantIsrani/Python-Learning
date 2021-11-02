# ITERATIVE FUNCTION FOR FACTORIAL 

# def factorial_iterative(n):
#     fact=1
#     for b in range(1, n+1):
#         fact=fact*b
#     return fact

# a = int(input("enter the number you want the factorial of: "))
# print(f"the factorial of {a} is {factorial_iterative(a)}")



# RECURSIVE FUNCTION FOR FACTORIAL 
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

a = int(input("enter the number you want the factorial of: "))
print(f"the factorial of {a} is {factorial_recursive(a)}")





