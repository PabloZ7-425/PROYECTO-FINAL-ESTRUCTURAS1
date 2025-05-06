from nodo_cancion import NodoCancion

class ListaReproduccion:
    def __init__(self):
        self.actual = None

    def agregar_cancion(self, nombre, artista, duracion, ruta):
        nueva = NodoCancion(nombre, artista, duracion, ruta)
        if not self.actual:
            self.actual = nueva
            nueva.siguiente = nueva
            nueva.anterior = nueva
        else:
            ultima = self.actual.anterior
            ultima.siguiente = nueva
            nueva.anterior = ultima
            nueva.siguiente = self.actual
            self.actual.anterior = nueva

    def obtener_lista(self):
        canciones = []
        if self.actual:
            nodo = self.actual
            while True:
                texto = f"{nodo.nombre} - {nodo.artista} ({nodo.duracion})"
                canciones.append(texto)
                nodo = nodo.siguiente
                if nodo == self.actual:
                    break
        return canciones