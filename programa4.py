PI = 3.14159

radio = float(input("ingresa el valor del radio: "))
print("el area del circulo es: {}".format(PI*radio*radio))


n1 = int(input("ingresa el primer valor: "))
n2 = int(input("ingresa el segundo valor: "))

print("{}^{} = {}".format(n1, n2, n1**n2))
print("{}/{} = {}".format(n1, n2, n1/n2))
print("{} mod {} = {}".format(n1, n2, n1%n2))
print("{} < {} = {}".format(n1, n2, n1<n2))
print("{} <= {} = {}".format(n1, n2, n1<=n2))
print("{} > {} = {}".format(n1, n2, n1>n2))
print("{} >= {} = {}".format(n1, n2, n1>=n2))
print("{} == {} = {}".format(n1, n2, n1==n2))
print("{} != {} = {}".format(n1, n2, n1!=n2))

#input es como el scanf
#radio =float convierte todo lo que esta dentro del parentesis a float
