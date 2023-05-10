# Ejercicio 3

# Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos).
# Contemplar las siguientes consideraciones:
# cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre,
# en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva-;
# cada desvío puede tener múltiples puntos de entrada y salida;
# se deben cargar seis estaciones de trenes y doce cambios de agujas;
# cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
# y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente;
# encontrar el camino más corto desde:
# la estación King's Cross hasta la estación Waterloo,
# la estación Victoria Train Station hasta la estación Liverpool Street Station,
# la estación St. Pancras hasta la estación King's Cross;

class nodoArista(object):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.sig = None
        self.ady = Arista()

class Grafo(object):
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.size = 0

class Arista(object):
    def __init__(self):
        self.inicio = None
        self.size = 0


def insertar_vertice(grafo, nombre, tipo):
    nodo = nodoVertice(nombre, tipo)
    if grafo.inicio is None:
        grafo.inicio = nodo
    else:
        aux = grafo.inicio
        while aux.sig is not None:
            aux = aux.sig
        aux.sig = nodo
    grafo.size += 1

def insertar_arista(grafo, origen, destino, nombre):
    nodo = nodoArista(nombre, destino)
    aux = grafo.inicio
    while aux is not None:
        if aux.nombre == origen:
            break
        aux = aux.sig
    aux2 = aux.ady.inicio
    if aux2 is None:
        aux.ady.inicio = nodo
    else:
        while aux2.sig is not None:
            aux2 = aux2.sig
        aux2.sig = nodo
    grafo.size += 1

def barrido_vertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print('Nombre:', aux.nombre, 'Tipo:', aux.tipo)
        print('Adyacentes:')
        barrido_arista(aux.ady)
        aux = aux.sig

def barrido_arista(vertice):
    aux = vertice.inicio
    while aux is not None:
        print('Nombre:', aux.nombre, 'Destino:', aux.destino)
        aux = aux.sig

def dijkstra(grafo, origen, destino):
    if grafo.inicio is not None:
        if origen != destino:
            dic = {}
            aux = grafo.inicio
            while aux is not None:
                dic[aux.nombre] = {'distancia': 99999
                    , 'visitado': False, 'anterior': None}
                aux = aux.sig
            dic[origen]['distancia'] = 0
            actual = origen
            while actual != destino:
                adyacentes = []
                aux = grafo.inicio
                while aux is not None:
                    if aux.nombre == actual:
                        break
                    aux = aux.sig
                ady = aux.ady.inicio
                while ady is not None:
                    adyacentes.append(ady.destino)
                    ady = ady.sig
                for a in adyacentes:
                    if dic[a]['visitado'] is False:
                        if dic[actual]['distancia'] + 1 < dic[a]['distancia']:
                            dic[a]['distancia'] = dic[actual]['distancia'] + 1
                            dic[a]['anterior'] = actual
                dic[actual]['visitado'] = True
                distancia_minima = 99999
                for v in dic:
                    if dic[v]['visitado'] is False:
                        if dic[v]['distancia'] < distancia_minima:
                            distancia_minima = dic[v]['distancia']
                            actual = v
            pila = []
            while actual is not None:
                pila.append(actual)
                actual = dic[actual]['anterior']
            while len(pila) > 0:
                print(pila.pop())
        else:
            print('El origen y el destino son el mismo')
    else:
        print('El grafo está vacío')

def main():
    