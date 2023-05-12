def degree(a,b):
    if b == 0:
        return 1
    else:
        return a * degree(a, b - 1)
    
a= int(input("Введите число "))
b= int(input("Введите степень "))
print(degree(a, b))