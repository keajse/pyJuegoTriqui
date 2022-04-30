from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class Triki:
    def __init__(self):
        self.jugador1 =""
        self.jugador2 = ""
        self.turno =1
        self.listaBotones = []
        self.tableroInt = []

    def bloquear_bton(self):
        for i in range(9):
            self.listaBotones[i].config(state='disable', bg="lightgray")

    '''def mensaje(self):
        messagebox.showinfo("HOLA", "Prueba")'''

    def cambiar(self, posi):
        messagebox
    
    def iniciar(self):        
        self.vnta = Tk() #Crear la ventana.
        self.vnta.geometry("400x500") # Dar dimensiones a la ventana.
        self.vnta.iconbitmap("img/logo.ico") #Agregar un icono.
        self.vnta.title("***  Juego de Triki 😉  ***")  #Agregar título.
        self.vnta.config(bg="#D0DDCE")
        self.vnta.maxsize(width=420, height=560)
        self.turnoJugador = StringVar()


        #Crear botones.
        #Para activar un método que tiene un parámetro es necesario activar la función
        #self.boton0 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.mensaje()).place(x=45, y=45)

        #Con ALT sostenido y clic puedo cambiar varios elementos a la vez
        self.boton0 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(0)).place(x=50, y=60)

        self.boton1 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(1)).place(x=150, y=60)

        self.boton2 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(2)).place(x=250, y=60)

        self.boton3 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(3)).place(x=50, y=160)

        self.boton4 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(4)).place(x=150, y=160)

        self.boton5 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(5)).place(x=250, y=160)

        self.boton6 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(6)).place(x=50, y=260)

        self.boton7 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(7)).place(x=150, y=260)

        self.boton8 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(8)).place(x=250, y=260)





        
        self.vnta.mainloop()


#Ejecutar el programa construyendo el objeto juego.

#Construcción de objecto, aplicación o programa.

juego = Triki()
juego.iniciar()