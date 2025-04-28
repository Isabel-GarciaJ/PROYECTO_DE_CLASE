
#Clase Producto con nombre y peso
class Producto:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso  # en gramos

# Clase Nodo, con el peso del pedido y los punteros izquierdo y derecho
class Nodo:
    def __init__(self, pedido):
        self.pedido = pedido
        self.izq = None
        self.der = None

# Clase Pedido con el número de pedido, lista de productos y su peso
class Pedido:
    def __init__(self, numpedido, lista_productos):
        self.numpedido = numpedido
        self.productos = lista_productos
        self.peso = sum(prod.peso for prod in lista_productos) / 1000  # kg

    def imprimir(self):
        print(f"Pedido #{self.numpedido} - Peso: {self.peso:.2f} kg - Productos: {[p.nombre for p in self.productos]}")

    def chequear_entrega(self):
        print(f"Pedido #{self.numpedido} entregado.")
        self.peso = 0
        self.numpedido = None
        self.productos = []

# Repartidor con nombre, capacidad y vehículo
class Repartidor:
    def __init__(self, nombre, capacidad, vehiculo):
        self.nombre = nombre
        self.capacidad = capacidad * 1000  # capacidad en gramos
        self.vehiculo = vehiculo   

# Clase Almacen que maneja los productos, repartidores y el árbol de pedidos
class Almacen:
    def __init__(self):
        self.catalogo = {}
        self.arbol = ArbolBinario()
        self.repartidores = []

    def cargar_productos(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            next(f)  # Saltar nombres
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 2:  # Se espera nombre y peso
                    nombre, peso = partes
                    self.catalogo[nombre] = Producto(nombre, int(peso))  
                    

    def contratarRepartidor(self, nombre, capacidad, vehiculo):
        self.repartidores.append(Repartidor(nombre, capacidad, vehiculo))

    def crear_pedido(self, numpedido, lista_nombres_productos):
        productos_pedido = []
        for nombre in lista_nombres_productos:
            if nombre in self.catalogo:
                productos_pedido.append(self.catalogo[nombre])
            else:
                print(f"Producto '{nombre}' no encontrado en el catálogo.")
        pedido = Pedido(numpedido, productos_pedido)
        self.arbol.insertar(pedido)

    def rutaDomicilio(self):
        while self.arbol.raiz is not None:
            peso_total, ruta = self.arbol.rutaPesada()
            peso_total_gramos = peso_total * 1000
            mejor_repartidor = None
            min_excedente = float('inf')

            for repartidor in self.repartidores:
                excedente = repartidor.capacidad - peso_total_gramos
                if 0 <= excedente < min_excedente:
                    min_excedente = excedente
                    mejor_repartidor = repartidor

            if mejor_repartidor:
                print(f"\nRepartidor asignado: {mejor_repartidor.nombre} ({mejor_repartidor.vehiculo})")
                print("Ruta de pedidos a entregar:")
                for nodo in ruta:
                    nodo.pedido.imprimir()
                    nodo.pedido.chequear_entrega()
                    self.arbol.eliminar(nodo.pedido)  # Eliminar el pedido una vez entregado
                print(f"Peso total de la entrega: {peso_total:.2f} kg")
            else:
                print("\nNo hay repartidor disponible con suficiente capacidad para el siguiente pedido.")
                break

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, pedido):
        if self.raiz is None:
            self.raiz = Nodo(pedido)
        else:
            self.insertar_nodo(self.raiz, pedido)

    def insertar_nodo(self, nodo, pedido):
        if pedido.peso < nodo.pedido.peso:
            if nodo.izq is None:
                nodo.izq = Nodo(pedido)
            else:
                self.insertar_nodo(nodo.izq, pedido)
        else:
            if nodo.der is None:
                nodo.der = Nodo(pedido)
            else:
                self.insertar_nodo(nodo.der, pedido)

    def rutaPesada(self):
        assert self.raiz is not None
        peso, ruta = self.rutaPesada1(self.raiz)
        return peso, ruta

    def rutaPesada1(self, nodo):
        assert nodo is not None
        if not nodo.izq and not nodo.der:
            return nodo.pedido.peso, [nodo]
        pesoIzq, rutaIzq = float('-inf'), []
        pesoDer, rutaDer = float('-inf'), []
        if nodo.izq:
            pesoIzq, rutaIzq = self.rutaPesada1(nodo.izq)
        if nodo.der:
            pesoDer, rutaDer = self.rutaPesada1(nodo.der)
        if pesoIzq > pesoDer:
            return nodo.pedido.peso + pesoIzq, [nodo] + rutaIzq
        else:
            return nodo.pedido.peso + pesoDer, [nodo] + rutaDer

    def eliminar(self, pedido_buscado):
        if self.raiz is None:
            return  #si el abrol está vacion no hace nada
        self.raiz = self._eliminar_nodo(self.raiz, pedido_buscado)

    def _eliminar_nodo(self, nodo, pedido_buscado):
        if nodo is None:
            return nodo
        # Buscar el nodo con el pedido que coincida
        if pedido_buscado.peso < nodo.pedido.peso:
            nodo.izq = self._eliminar_nodo(nodo.izq, pedido_buscado)
        elif pedido_buscado.peso > nodo.pedido.peso:
            nodo.der = self._eliminar_nodo(nodo.der, pedido_buscado)
        else:
            # Caso 1: Nodo sin hijos (nodo hoja)
            if nodo.izq is None and nodo.der is None:
                return None
            # Caso 2: Nodo con un solo hijo
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Caso 3: Nodo con dos hijos
            sucesor = self._obtener_sucesor(nodo)
            nodo.pedido = sucesor.pedido
            nodo.der = self._eliminar_nodo(nodo.der, sucesor.pedido)
        return nodo

    def _obtener_sucesor(self, nodo):
        nodo = nodo.der
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

# Crear el almacén
almacen = Almacen()

# Cargar productos
almacen.cargar_productos("ListaProductos.txt")

# Contratar repartidores
almacen.contratarRepartidor("Ana", 10, "A Pie")
almacen.contratarRepartidor("Gabriel", 40, "Moto")
almacen.contratarRepartidor("Mariana", 20, "Bicicleta")

# Crear pedidos
almacen.crear_pedido(1, ["Leche", "Harina", "Panela"])
almacen.crear_pedido(2, ["Queso", "Jamón", "Arepa", "Salchichón"])
almacen.crear_pedido(3, ["Six-Pack Corona", "Cartón de huevos", "ProductoX", "ProductoX"])

# Entregar pedidos
almacen.rutaDomicilio()
