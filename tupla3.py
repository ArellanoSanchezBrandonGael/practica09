from collections import namedtuple


planeta = namedtuple('planeta',['nombre','numero']) #primer argumento que recibe es el nombre de la tupla

mercurio = planeta('mercurio',1)
venus = planeta('venus',2)
tierra = planeta('tierra',3)
marte = planeta('marte',4)

print(mercurio.nombre)
print(mercurio.numero)
print(venus[0])
print(venus[1])


print("campos de la tupla: {}".format(tierra._fields))
