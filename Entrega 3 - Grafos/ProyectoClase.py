from collections import deque
import math

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
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2, peso = 1):
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)

def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append(Arista(destino, peso))

def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen:(0,None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):
    if(origen == destino):
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]


def dijkstra(grafo, destino, etiquetas, procesados):
    nodoActual = menorValorNoProcesado(etiquetas, procesados)
#    print "-----------------------------"
#    print "Nodo Actual:",nodoActual
#    print "Procesados",procesados
#    print "Etiquetas",etiquetas
    if(nodoActual == destino):
        return
    procesados.append(nodoActual)
    for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
        generarEtiqueta(grafo, vecino, nodoActual, etiquetas)
    dijkstra(grafo, destino, etiquetas, procesados)

def generarEtiqueta(grafo, nodo, anterior, etiquetas):
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior),anterior
    if(not(etiquetas.has_key(nodo)) or  acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]) ):
        etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
    return grafo.relaciones[nodo]

def vecinoNoProcesado(grafo, nodo, procesados):
    aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo,nodo))
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]


def peso (grafo, nodoOrigen, nodoDestino):
    return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso

def acumulado(etiqueta):
    return etiqueta[0]

def anterior(etiqueta):
    return etiqueta[1]

def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = filter(lambda (nodo,_):not nodo in procesados, etiquetas.iteritems())
    return min(etiquetadosSinProcesar, key=lambda (_, (acum, __)): acum)[0]

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

