import tkinter as tk
from tkinter import messagebox
from lista_reproduccion import ListaReproduccion
import pygame

class Reproductor:
    def __init__(self, root):  
        self.root = root
        self.root.title("Reproductor de Música")

        self.lista = ListaReproduccion()
        pygame.mixer.init()
        self.pausado = False

        tk.Label(root, text="Nombre de la canción:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Artista:").pack()
        self.entry_artista = tk.Entry(root)
        self.entry_artista.pack()

        tk.Label(root, text="Duración:").pack()
        self.entry_duracion = tk.Entry(root)
        self.entry_duracion.pack()

        tk.Label(root, text="Ruta del archivo:").pack()
        self.entry_ruta = tk.Entry(root)
        self.entry_ruta.pack()

        tk.Button(root, text="Agregar Canción", command=self.agregar_cancion).pack(pady=5)

        self.lista_box = tk.Listbox(root, width=60)
        self.lista_box.pack(pady=5)

        tk.Button(root, text=" Reproducir / Reanudar", command=self.reproducir).pack(pady=2)
        tk.Button(root, text=" Pausar", command=self.pausar).pack(pady=2)
        tk.Button(root, text=" Detener", command=self.detener).pack(pady=2)
        tk.Button(root, text=" Anterior", command=self.anterior).pack(pady=2)
        tk.Button(root, text=" Siguiente", command=self.siguiente).pack(pady=2)

    def agregar_cancion(self):
        nombre = self.entry_nombre.get()
        artista = self.entry_artista.get()
        duracion = self.entry_duracion.get()
        ruta = self.entry_ruta.get()

        if not nombre or not artista or not duracion or not ruta:
            messagebox.showerror("Error", "Debes llenar todos los campos.")
            return

        self.lista.agregar_cancion(nombre, artista, duracion, ruta)
        self.actualizar_lista()
        self.limpiar_espacios()

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for cancion in self.lista.obtener_lista():
            self.lista_box.insert(tk.END, cancion)

    def limpiar_espacios(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_artista.delete(0, tk.END)
        self.entry_duracion.delete(0, tk.END)
        self.entry_ruta.delete(0, tk.END)

    def reproducir(self):
        if self.lista.actual:
            if self.pausado:
                pygame.mixer.music.unpause()
                self.pausado = False
            else:
                ruta = self.lista.actual.ruta
                try:
                    pygame.mixer.music.load(ruta)
                    pygame.mixer.music.play()
                except:
                    messagebox.showerror("Error", "No se pudo reproducir el archivo.")

    def pausar(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pausado = True

    def detener(self):
        pygame.mixer.music.stop()
        self.pausado = False

    def siguiente(self):
        if self.lista.actual and self.lista.actual.siguiente:
            self.lista.actual = self.lista.actual.siguiente
            self.pausado = False
            self.reproducir()
            self.actualizar_lista()

    def anterior(self):
        if self.lista.actual and self.lista.actual.anterior:
            self.lista.actual = self.lista.actual.anterior
            self.pausado = False
            self.reproducir()
            self.actualizar_lista()


if __name__ == "__main__":  
    root = tk.Tk()
    app = Reproductor(root)
    root.mainloop()
    