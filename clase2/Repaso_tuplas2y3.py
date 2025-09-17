#Concatenamos Listas 
lista1=[1,2,3,4]
lista2=[5,6,7,8]
lista3=[lista1+lista2]#Concatenamos
print(lista3)
lista3.extend([7,8,9,1])#FUuncion para agregar elementos a una lista
print(lista3)

print(lista2.index(7)) #Fuincion para ubicar en que 
                        #indice se encuentra el valor ingresado

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))

#Para poner al reves una lista

lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitieno sus elementos:
lsita2= lista2 *2
print(lista2)

#Metodos de ordenamiento, en python es una funcion

lista2.sort()#Ordenamiento asendente
print(lista2)
lista2.sort(reverse=True)#Ordenamiento desendente
print(lista2)

