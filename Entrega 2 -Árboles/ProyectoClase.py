#Big tree
#find_attr y find_attrs: Busca uno o varios nodos por atributo.

#find_name y find_names: Busca uno o varios nodos por nombre.  

# Arbol no binario, empleados fijos (repartidor). Altura 3
    #Metodo para peso de las rutas
    #Metodo para decidir que repatidores pueden realizar y que se escoja el de una capacidad más cercana
    #agregar nuevas rutas
    #Eliminar pedido ya recorrido
    #metodo para buscar nodo (numero pedido) con big tree find_name
    #Impripmir

#Clase Nodo, capacidad(peso), nodos hijos, pedido(numero de pedido) y metodo para cambiar el pedido

#Pedido (Si se agregan productos usar lectura de archivos),(numero de pedido), peso (si se usan productos, metodo para calcular peso), (precio a cobrar no seeeeee)
    #imprimir
    #chequear pedido (Una vez pasa el repartidor se coloca peso en cero y pedido en none)

class Pedido:
	def __init__ (self, listproductos, numpedido, peso, precio):  
		self.listproductos = listproductos
		self.numpedido = numpedido
		self.peso = peso
		self.precio = precio
	
#Repartidor: nombre, capacidad y vehiculo,(Lista con numero de pedidos)
class Repartidor:
	def __init__ (self, nombre, capacidad, vehiculo):
		self.nombre = nombre
		self.capacidad = capacidad
		self.vehiculo = vehiculo

#Demo: Rutas ya establecidas, metodo para agregar rutas