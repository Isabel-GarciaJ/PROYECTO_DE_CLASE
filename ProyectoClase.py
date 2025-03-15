		
#Buscar un elemento en la lista usando un método de ordenamiento (Busqueda Lineal)
def buscarElementoL(lista, valor, pos=0):
    if pos >= len(lista):  
        return -1
    if lista[pos] == valor:  
        return pos
    return buscarElementoL(lista, valor, pos + 1)  

#Buscar un elemento en la lista usando un método de ordenamiento (Busqueda Binaria)
def buscarElementoB(lista, valor):
    izq, der = 0, len(lista) - 1  
    while izq <= der:
        mid = izq + (der - izq) // 2  
        if lista[mid] == valor:
            return mid  
        elif lista[mid] < valor: 
            izq = mid + 1  
        else: 
            der = mid - 1  
    return -1 

result = buscarElementoB(lista, valor)
if result != -1:
    print(f"El elemento se encontro en la posicion{result}")
else:
    print("IEl elemento no se encontro")