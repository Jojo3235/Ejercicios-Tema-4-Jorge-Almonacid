# Carácter, Frecuencia, Código
# I,0.28,10
# N,0.16,110
# T,0.08,010
# E,0.16,011
# L,0.08,001
# G,0.08,000
# C,0.08,1111
# A,0.08,1110

class nodoArbol(object):
    
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

def insertar_nodo(raiz, info):
    if raiz == None:
        raiz = nodoArbol(info)
    else:
        if info < raiz.info:
            raiz.izq = insertar_nodo(raiz.izq, info)
        else:
            raiz.der = insertar_nodo(raiz.der, info)
    return raiz

def eliminar_nodo(raiz, clave):
    x = None
    if raiz != None:
        if clave < raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq == None:
                raiz = raiz.der
            elif raiz.der == None:
                raiz = raiz.izq
            else:
                raiz.izq, maximo = remplazar(raiz.izq)
                raiz.info = maximo
    return raiz, x

def remplazar(raiz):
    aux = None
    if raiz.der == None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

# crear arbol

arbol = nodoArbol('raíz')

# insertar nodos

arbol = insertar_nodo(arbol, 'I')
arbol = insertar_nodo(arbol, 'N')
arbol = insertar_nodo(arbol, 'T')
arbol = insertar_nodo(arbol, 'E')
arbol = insertar_nodo(arbol, 'L')
arbol = insertar_nodo(arbol, 'G')
arbol = insertar_nodo(arbol, 'C')
arbol = insertar_nodo(arbol, 'A')

