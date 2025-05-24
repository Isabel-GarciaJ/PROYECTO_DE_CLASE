from collections import deque
import math
import heapq

class Grafo(object):
    def __init__(self):
        self.relaciones = {}
        self.sucursales = {}
    def __str__(self):
        return str(self.relaciones)

class Nodo():
    def __init__(self, calle, carrera, nombre):
        self.nombre = nombre
        self.direccion = [calle, carrera]
        self.pedido = False
    
class Arista(object):
    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso
    def __str__(self):
        return str(self.elemento) + str(self.peso)


# Insertar elementos
#metodo para agregar sucursal dependiendo de la distancia con carrera y calle
def addsucursal(grafo, calle, carrera, nombre):
    nueva_sucursal = Nodo(calle, carrera, nombre)
    grafo.sucursales[nombre] = nueva_sucursal
    grafo.agregar_nodo(nueva_sucursal)
    for difnombre, difsucursal in grafo.sucursales.items():
        if difnombre == nombre:
            continue  # No se conecta consigo misma
        distancia = calcular_distancia(nueva_sucursal, difsucursal)
        grafo.agregar_arista(nueva_sucursal, difsucursal, distancia)

#calcular la distancia entre nodos
def calcular_distancia(nodo1, nodo2):
	x, y = nodo1.direccion
	a, b = nodo2.direccion
	dx = abs(a - x) # obtener valor absoluto
	dy = abs(b - y)
	return math.sqrt(dx**2 + dy**2)  # Raíz cuadrada para obtener la distancia
    

# Elimminar elementos
#metodo para eliminar sucursales y aristas de sucursales
def eliminar_sucursal_arista(grafo, nombre):
    if nombre not in grafo.sucursales:
        print("Sucursal no encontrada")
        return
    nodo = grafo.sucursales[nombre]

    for nodo_origen, aristas in grafo.relaciones.items():
        grafo.relaciones[nodo_origen] = [arista for arista in aristas if arista.elemento != nodo]

    if nodo in grafo.relaciones:
        del grafo.relaciones[nodo]
    del grafo.sucursales[nombre]


# Buscar elementos
# metodo para encontrar el camino minimo para entregar pedidos

def camino_minimo(grafo, origen, destino):
    distancias = {nodo: float('inf') for nodo in grafo.sucursales.values()}
    previos = {nodo: None for nodo in grafo.sucursales.values()}
    distancias[grafo.sucursales[origen]] = 0
    
    cola = [(0, grafo.sucursales[origen])]  # (distancia, nodo)

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual.nombre == destino:
            break
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for arista in grafo.relaciones.get(nodo_actual, []):
            vecino = arista.elemento
            peso = arista.peso
            distancia_nueva = distancia_actual + peso
            
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                previos[vecino] = nodo_actual
                heapq.heappush(cola, (distancia_nueva, vecino))
    
    # Reconstruir camino desde destino hacia origen
    camino = []
    actual = grafo.sucursales[destino]
    while actual:
        camino.append(actual)
        actual = previos[actual]
    camino.reverse()
    
    return camino, distancias[grafo.sucursales[destino]]


# Crear un grafo no dirigido
g = Grafo()
# Crear nodos (sucursales) predefinidos
nodos = [
    Nodo(1, 1, "Sucursal A"),
    Nodo(3, 5, "Sucursal B"),
    Nodo(6, 2, "Sucursal C"),
    Nodo(8, 8, "Sucursal D")
]

print(g.grafo)  # {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
print(g.obtener_vecinos("A"))  # ['B', 'C']

