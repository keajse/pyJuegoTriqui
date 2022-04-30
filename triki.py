from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class Triki:
    #init inicializa la clase.
    def __init__(self):
        self.jugador1 =""
        self.jugador2 = ""
        self.turno =1
        self.listaBotones = []
        self.tableroInt = []


    def bloquear_bton(self):
        for i in range(9):
            self.listaBotones[i].config(state='disable', bg="lightgray")
    
    #Para que los botones queden inhabilitados colocar la palabra 'disable'

    '''def mensaje(self):
        messagebox.showinfo("HOLA", "Prueba")'''

    def cambiar(self, posi):
        messagebox
    
    def iniciar(self):        
        self.vnta = Tk() #Crear la ventana.
        self.vnta.geometry("400x500") # Dar dimensiones a la ventana.
        self.vnta.iconbitmap("img/logo.ico") #Agregar un icono. Cuando se quiere ingresar a una carpeta bastará con ingresar el nombre seguido de /
        self.vnta.title("***  Juego de Triki 😉  ***")  #Agregar título.
        self.vnta.config(bg="#D0DDCE") #Establecer el color de fondo.
        self.vnta.maxsize(width=400, height=500) #Dimensiones máximas del objecto.
        self.turnoJugador = StringVar() 


        #Crear botones.
        #Para activar un método que tiene un parámetro es necesario activar la función
        #self.boton0 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.mensaje()).place(x=45, y=45)

        #Con ALT sostenido y clic puedo cambiar varios elementos a la vez
        self.boton0 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(0)).place(x=50, y=60)
        self.listaBotones.append(self.boton0) #Agrega los botones a la lista de botones.

        self.boton1 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(1)).place(x=150, y=60)
        self.listaBotones.append(self.boton1)

        self.boton2 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(2)).place(x=250, y=60)
        self.listaBotones.append(self.boton2)

        self.boton3 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(3)).place(x=50, y=160)
        self.listaBotones.append(self.boton3)

        self.boton4 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(4)).place(x=150, y=160)
        self.listaBotones.append(self.boton4)

        self.boton5 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(5)).place(x=250, y=160)
        self.listaBotones.append(self.boton5)

        self.boton6 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(6)).place(x=50, y=260)
        self.listaBotones.append(self.boton6)

        self.boton7 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(7)).place(x=150, y=260)
        self.listaBotones.append(self.boton7)

        self.boton8 = Button(self.vnta, width=9, height=4, font=("Arial", 12, "bold"), command=lambda: self.cambiar(8)).place(x=250, y=260)
        self.listaBotones.append(self.boton8)

        #Crear etiqueta jugador
        self.lbl_jugador = Label(self.vnta, textvariable="").pack()

        #pack() lo coloca debajo del siguiente objeto que tiene esta propiedad, por default siempre queda en el parte superior y centrado.





        
        self.vnta.mainloop()


#Ejecutar el programa construyendo el objeto juego.
#Construcción de objecto, aplicación o programa.

juego = Triki()
juego.iniciar()