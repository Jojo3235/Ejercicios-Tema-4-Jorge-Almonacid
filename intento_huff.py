import heapq

class NodoHuffman(object):
    def __init__(self, info, frecuencia, izq, der):
        self.info = info
        self.frecuencia = frecuencia
        self.izq = izq
        self.der = der

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia
    
    def __str__(self):
        return "("+ str(self.info) + " : " + str(self.frecuencia) +")"
    
    def __repr__(self):
        return self.__str__()

class NodoArbol(object):
    def __init__(self, info, izq, der):
        self.info = info
        self.izq = izq
        self.der = der

    def __str__(self):
        return self.info
    
    def __repr__(self):
        return self.__str__()
    
class ArbolHuffman(object):
    def __init__(self, raiz):
        self.raiz = raiz
        self.heap = []
        self.codigos = {}
        self.codigos_inversos = bytearray{}

    def frecuencia