# DUNDER METHODS IS METHODS WITH __example___

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1


n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)


# OTHER DUNDER METHODS LIKE STR 
n= Number(9)
print(n)
print("the len is ", len(n))