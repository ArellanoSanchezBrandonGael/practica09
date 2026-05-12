#            llave  valor
diadeMes= { "enero": 31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30,
            "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31} 
#lsitas que contienen listas


print(diadeMes) #imprime completo
print(diadeMes.keys()) #imprime las llaves
for llave in diadeMes.keys():
    print(llave)

print(diadeMes.items())
print("enero tiene {} dias".format( diadeMes["enero"])) #imprime elemento de la lista
print("julio tiene {} dias".format( diadeMes["julio"]))
print("agosto tiene {} dias".format( diadeMes["agosto"]))
print("diciembre tiene {} dias".format( diadeMes["diciembre"]))

#se busca mediante las llaves
