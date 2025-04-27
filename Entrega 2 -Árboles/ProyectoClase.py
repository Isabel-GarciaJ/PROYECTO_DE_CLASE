#Big tree
#find_attr y find_attrs: Busca uno o varios nodos por atributo.

#find_name y find_names: Busca uno o varios nodos por nombre.  

#Clase Nodo, capacidad(peso), nodos hijos, pedido(numero de pedido) y metodo para cambiar el pedido
class Nodo:
    def __init__(self, pedido):
        self.pedido = pedido 
        self.peso = self.pedido.peso
        self.der = None
        self.izq = None

#Pedido (Si se agregan productos usar lectura de archivos),(numero de pedido), 
# peso (si se usan productos,metodo para calcular peso), (precio a cobrar no seeeeee)

class Pedido:
    def __init__ (self, numpedido, peso, precio):  
        self.numpedido = numpedido
        self.peso = peso
        self.precio = precio
    
    #imprimir el pedido
    def imprimir(self):
        print("Pedido #", self.numpedido, " - Peso: ", self.peso, "kg - Precio: $", self.precio)

    #Metodo para que repartidor entregue el pedido
    def chequear_entrega(self):
        print("Pedido #", self.numpedido, "entregado.")
        self.peso = 0
        self.numpedido = None
        self.precio = 0
    

#Repartidor: nombre, capacidad y vehiculo,(Lista con numero de pedidos)
class Repartidor:
    def __init__ (self, nombre, capacidad, vehiculo):
        self.nombre = nombre
        self.capacidad = capacidad
        self.vehiculo = vehiculo       

#Almacen la ultima lagrima
class Almacen:
    def __init__ (self):
        self.productos = []
        self.arbol = ArbolBinario()
        self.repartidores = []
        self.pedidos = []
    
    #metodo para llenar el arbol con los pedidos

    #metodo para llenar los productos del almacen

    #metodo para contratar (construir) repartidores
    def contratarRepartidor(self, nombre, capacidad, vehiculo):
        self.repartidores.append(Repartidor(nombre, capacidad, vehiculo))

    #metodo para entregar los pedidos
    def rutaDomicilio(self):
        difMin = float('inf')
        peso, ruta = self.arbol.rutaPesada()
        repar = None
        for repartidor in self.repartidores:
            dif = repartidor.capacidad - peso
            if dif < difMin and dif > 0:
                dif - peso
                repar = repartidor
        print("El repartidor ", repar.nombre, "realizara los domicilios")
        for pedido in ruta:
            pedido.chequear_entrega()
        



#posibles metodos a agregar
def obtener_sucesor(actual):
    actual = actual.der
    while actual is not None and actual.izq is not None:
        actual = actual.izq
    return actual

def eliminar_nodo(raiz, x):
    if raiz is None:
        return raiz

    if raiz.pedido > x:
        raiz.izq = eliminar_nodo(raiz.izq, x)
    elif raiz.pedido < x:
        raiz.der = eliminar_nodo(raiz.der, x)
    else:
        if raiz.izq is None:
            return raiz.der
        if raiz.der is None:
            return raiz.izq

        sucesor = obtener_sucesor(raiz)
        raiz.pedido = sucesor.pedido
        raiz.der = eliminar_nodo(raiz.der, sucesor.pedido)
        
    return raiz

def cambiar_pedido(self, nuevo_pedido):
        self.pedido = nuevo_pedido

def recorrido_inorden(raiz):
    if raiz is not None:
        recorrido_inorden(raiz.izq)
        print(raiz.pedido, end=" ")
        recorrido_inorden(raiz.der)

# Arbol binario,todos los nodos son pedidos, empleados fijos (repartidor). Altura 3
    #Metodo para peso de las rutas
    #Metodo para decidir que repatidores pueden realizar y que se escoja el de una capacidad más cercana
    #agregar nuevas rutas
    #Eliminar pedido ya recorrido
    #metodo para buscar nodo (numero pedido) con big tree find_name
    #Impripmir
class ArbolBinario:
    #Constructor de un árbol binario de busqueda
    def __init__(self):
        self.raiz = None

    #Metodo para insertar un nodo, valor es el peso del pedido
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_nodo(self.raiz, valor)

    #Metodo para insertar un nodo teniendo en cuenta su peso, valor es el peso del pedido
    def insertar_nodo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self.insertar_nodo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self.insertar_nodo(nodo.der, valor)

    #metodo para obtener la ruta con mayor peso
    def rutaPesada(self):
        assert self.raiz is not None
        peso, ruta = self.rutaPesada1(self.raiz)
        return peso, ruta

    #Metodo para encontrar la ruta con mayor peso
    def rutaPesada1(self, nodo):
        assert nodo is not None

        if not nodo.izq and not nodo.der:
          return nodo.peso, [nodo]
        
        pesoIzq, rutaIzq = float('-inf'), []
        pesoDer, rutaDer = float('-inf'), []

        if nodo.izq is not None:
            pesoIzq, rutaIzq = self.rutaPesada1(nodo.izq)
        if nodo.der is not None:
            pesoDer, rutaDer =  self.rutaPesada1(nodo.der)

        if pesoIzq > pesoDer:
            return nodo.peso + pesoIzq, [nodo] + rutaIzq
        else:
            return nodo.peso + pesoDer, [nodo] + rutaDer

    #Metodo para recorrer el arbol en inorden
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izq)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.der)

    #metodo para recorrer el arbol en preorden
    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.recorrido_preorden(nodo.izq)
            self.recorrido_preorden(nodo.der)

    #metodo para recorrer el arbol en postorden
    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izq)
            self.recorrido_postorden(nodo.der)
            print(nodo.valor, end=' ')

#Demo: Rutas ya establecidas, metodo para agregar rutas