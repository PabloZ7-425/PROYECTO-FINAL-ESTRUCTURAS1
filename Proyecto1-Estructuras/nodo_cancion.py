class NodoCancion:
    def __init__(self, nombre, artista, duracion, ruta):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.ruta = ruta
        self.anterior = None
        self.siguiente = None
