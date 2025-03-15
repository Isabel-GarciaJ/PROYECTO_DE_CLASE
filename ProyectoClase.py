class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None
		
	def imprimir(self):
		d = str (self.data)
		return d

class Lista:
	def __init__ (self):
		self.cabeza = None
	
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
				string = str(i) + ". " + nodo.imprimir()
				print(string)	
	
	#Agregar un elemento (Solo se agregaran por el inicio de la lista)
	def addNodo(self,data):
		newNodo = Nodo(data)
		newNodo.siguiente = self.cabeza
		self.cabeza = newNodo
		
#Buscar un elemento en la lista usando un método de ordenamiento (a libre elección del grupo)
