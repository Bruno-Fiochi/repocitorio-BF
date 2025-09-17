#Maradona :10 Un diccrionario esta compuesto por dos elemetnos
#UNA LLAVE Y UN VALOR 
#DICT(key : value)

diccionario= {
    "IDE":"Integrated Developmente  Environment",
    "POO":"Programacion Orientada a Objetos",
    "SABD" :"Sistema de Administracion de Base de Datos"
}
#Verufucar la cantidad de elementos en el diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con llave(key)
print(diccionario["IDE"])

# otra forma
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificacion de elemetos
diccionario["IDE"]="Entorno de Desarrollo Integrado"
print(diccionario["IDE"])

for termino in diccionario:#Recorremos mostrando solo las llaves
    print(termino)

# Funcion para recorrer Dicionario KEY and value
for termino, valor in diccionario.items():
    print(termino, valor)

#otras maneras de aceder a un diccionario 
for termino in diccionario.keys():
    print(termino)# muestra solo las llaves

for valor in diccionario.values():  #usamos una funcion para acceder al valor
    print(valor)

#comprobar la existencia d algun elemento
print("IDE" in diccionario)# devuelve booleano

#Agregar elemento
diccionario["PK"]= "Primari Key"
print(diccionario)

#Eliminar un elemento

diccionario.pop("SABD")
print(diccionario)

#Vaciar diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
