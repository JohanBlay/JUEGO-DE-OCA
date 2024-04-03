#CASO DE ESTUDIO
import tkinter as tk
import random

class Tablero:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juego de la Oca")
        
        self.canvas = tk.Canvas(self.root, width=800, height=50)
        self.canvas.pack()

        # Dibujar las casillas del tablero
        for i in range(16):
            x0, y0 = i*50, 0
            x1, y1 = x0+50, y0+50
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

        # Dibujar las fichas de los jugadores
        self.ficha_jugador1 = self.canvas.create_oval(10, 10, 20, 20, fill="red")
        self.ficha_jugador2 = self.canvas.create_oval(30, 10, 40, 20, fill="blue")

        self.dado = Dado()
        self.jugador_actual = 1
        self.resultado_jugador1 = 0
        self.resultado_jugador2 = 0

        # Crear botón "Tirar dado"
        self.boton_tirar_dado = tk.Button(self.root, text="Tirar dado", command=self.lanzar_dado)
        self.boton_tirar_dado.pack()

        # Etiqueta para mostrar el resultado del dado
        self.resultado_dado_label = tk.Label(self.root, text="Resultado del dado: ")
        self.resultado_dado_label.pack()

        self.canvas.bind("<Button-1>", self.lanzar_dado)

    def mostrar_tablero(self):
        self.root.mainloop()

    def lanzar_dado(self, event=None):
        if self.jugador_actual == 1:
            jugador = "Jugador 1"
            ficha = self.ficha_jugador1
            self.jugador_actual = 2
        else:
            jugador = "Jugador 2"
            ficha = self.ficha_jugador2
            self.jugador_actual = 1
        
        resultado_dado = self.dado.lanzar()
        print(jugador, "lanzó el dado y obtuvo:", resultado_dado)

        # Actualizar el resultado del dado en la etiqueta
        self.resultado_dado_label.config(text="Resultado del dado: " + str(resultado_dado))

        # Actualizar el resultado del jugador
        if jugador == "Jugador 1":
            self.resultado_jugador1 += resultado_dado
            print("Resultado total de Jugador 1:", self.resultado_jugador1)
            if self.resultado_jugador1 >= 16:
                print("¡Jugador 1 ha ganado!")
                self.mostrar_ganador("Jugador 1")
                return
        else:
            self.resultado_jugador2 += resultado_dado
            print("Resultado total de Jugador 2:", self.resultado_jugador2)
            if self.resultado_jugador2 >= 16:
                print("¡Jugador 2 ha ganado!")
                self.mostrar_ganador("Jugador 2")
                return

        # Mover la ficha en el tablero
        for _ in range(resultado_dado):
            # Obtener la posición actual de la ficha
            x0, y0, x1, y1 = self.canvas.coords(ficha)
            
            # Verificar si la ficha ha llegado al final del tablero
            if x1 >= 800:
                print("¡", jugador, "ha ganado!")
                self.mostrar_ganador(jugador)
                return
                
            # Mover la ficha horizontalmente
            self.canvas.move(ficha, 50, 0)

    def mostrar_ganador(self, ganador):
        # Eliminar el botón y la etiqueta del resultado del dado
        self.boton_tirar_dado.pack_forget()
        self.resultado_dado_label.pack_forget()
        # Crear una etiqueta grande para mostrar al ganador
        self.canvas.create_text(400, 25, text="¡" + ganador + " ha ganado!", font=("Helvetica", 20), fill="green")

class Ficha:
    def __init__(self, jugador):
        self.jugador = jugador
        self.posicion = 0

class Dado:
    def lanzar(self):
        return random.randint(1, 6)

def iniciar_juego():
    tablero = Tablero()
    tablero.mostrar_tablero()

# Iniciar el juego
iniciar_juego()
