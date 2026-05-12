#def define funciones xdddd
#n es el tipo

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n = int(input("ingresa un numero entero: "))
print("{}".format(factorial(n)))

∫
