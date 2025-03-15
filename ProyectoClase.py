import math

class Nodo:
	def __init__(self, pedido):
		self.siguiente = None
		self.pedido = pedido
		
	def imprimir(self):
		print(self.pedido.imprimir())
	
class Cliente:
	def __init__(self, nombre):
		self.nombre = nombre
		self.direccion = None
		self.distancia = None
	
	def setdireccion(self):
		calle = int(input("Introduzca la calle"))
		carrera = int(input("Introduzca la carrera"))
		distancia = [calle, carrera]
		self.direccion = str("Calle ", calle, " #", carrera)
		self.distancia = distancia

class Pedido:
	def __init__ (self, cliente, listproductos, numorden):    # clase pedido, tiene un cliente, productos a comprar y el numero del pedido
		self.cliente = cliente
		self.listproductos = listproductos
		self.numorden = numorden
	
	def imprimir(self):
		string = (
            f"--- Pedido {self.numorden} ---\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Compra: {self.listproductos}\n"
            f"Dirección: {self.cliente.direccion}"
        )
		return string

class Lista:
	def __init__ (self):
		self.cabeza = None
		self.local = [0,0]		#tomamos el local como punto de referencia
	
    #Verificar si la lista está vacía
	def vacia(self):
		if self.cabeza is None:
			return True
		else:
			return False
	
    #Contar la cantidad de elementos existentes en la lista
	def length(self):
		contador = 0
		nodo = self.cabeza
		if self.vacia():
			return contador
		else:
			while nodo != None:
				contador += 1
				nodo = nodo.siguiente
			return contador	
	 
    #Imprimir en pantalla los elementos de la lista
	def imprimir(self):
		nodo = self.cabeza
		if self.vacia():
			print("La lista esta vacia")
		else:
			for i in range (1,self.length()+1):
				print(print(f"{i}. {nodo.imprimir()}"))	
				nodo = nodo.siguiente
	
	#Agregar un elemento (Solo se agregaran por el inicio de la lista)
	def addNodo(self,pedido):
		newNodo = Nodo(pedido)
		newNodo.siguiente = self.cabeza
		self.cabeza = newNodo
	
	#ordenar la lista de menor a mayor distancia
	def insertion_sort(lista, distancia):
		for i in range(1, len(lista)):
			clave = lista[i]
			j = i - 1
			while j >= 0 and distancia(lista[j]) > distancia(clave):
				lista[j + 1] = lista[j]
				j -= 1
			lista[j + 1] = clave
		return lista

	#calcular la distancia del cliente al local
	def _calcular_distancia(self, nodo):
		x, y = self.local 
		a, b = nodo.pedido.cliente.distancia
		dx = a - x
		dy = b - y
		return math.sqrt(dx**2 + dy**2)  # Raíz cuadrada para obtener la 

#==================== OPCION 1 =========================	
#Buscar un elemento en la lista usando un método de ordenamiento (Busqueda Lineal)
def buscarElementoL(lista, valor, pos=0):
    if pos >= len(lista):  
        return -1
    if lista[pos] == valor:  
        return pos
    return buscarElementoL(lista, valor, pos + 1)  

result = buscarElementoB(lista, valor)
if result != -1:
    print(f"El elemento se encontro en la posicion{result}")
else:
    print("IEl elemento no se encontro")
