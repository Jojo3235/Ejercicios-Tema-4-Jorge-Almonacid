class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            resultado = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            return resultado

    def esta_vacia(self):
        return self.primero is None


