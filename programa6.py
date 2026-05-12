n1 = int(input("ingresa el primer valor: "))
n2 = int(input("ingresa el segundo valor: "))

print("1. suma \n2. resta \n3.multiplicacion \n4.division \n5. cociente \n6. residuo")
print("7. salir")
op = input("selecciona una operacion: ")

while True: 
    if op == "1":
        print("{}+{} = {}".format(n1, n2, n1+n2))
    elif op == "2":
        print("{}-{} = {}".format(n1, n2, n1-n2))
    elif op == "3":
        print("{}*{} = {}".format(n1, n2, n1*n2))
    elif op == "4":
        print("{}/{} = {}".format(n1, n2, n1/n2))
    elif op == "5":
        print("{}//{} = {}".format(n1, n2, n1//n2))
    elif op == "6":
        print("{} mod {} = {}".format(n1, n2, n1%n2))
    elif op == "7":
        break
    else:
        print("la opcion no es valida")
    print("1. suma \n2. resta \n3.multiplicacion \n4.division \n5. cociente \n6. residuo")
    print("7. salir")
    op = input("selecciona una operacion: ")

