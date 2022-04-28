from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter

def bloquear():
    for i in range(0,9):
        botones[i].config(state='disable')
        botones[i].config(bg="#0E9EDA")

def jugadoresP():
    for i in range(0,9):
        botones[i].config(state='normal')
        botones[i].config(bg="#88D5F5")
        botones[i].config(text="")
        k[i] = "V"
    global player1, player2
    

    try:
        player1 = simpledialog.askstring("Jugador 1","Escriba el nombre del jugador 1: ").upper()
        if player1 == "":
            player1 = "JUGADOR 1"
        player2 = simpledialog.askstring("Jugador 2","Escriba el nombre del jugador 2: ").upper()
        if player2 =="":
            player2 = "JUGADOR 2"
    except Exception as ex:
        print("JUEGO CANCELADO")
        bloquear()

    
    shiftPlayer.set("Turno: " + player1)

def iniciarP():
    for i in range(0,9):
        botones[i].config(state='normal')
        botones[i].config(bg="#88D5F5")
        botones[i].config(text="")
        k[i] = "V"
    global player1, player2
    

    if player1 == "":

        try:
            player1 = simpledialog.askstring("Jugador 1","Escriba el nombre del jugador 1: ").upper()
            if player1 == "":
                player1 = "JUGADOR 1"
            player2 = simpledialog.askstring("Jugador 2","Escriba el nombre del jugador 2: ").upper()
            if player2 =="":
                player2 = "JUGADOR 2"
        except Exception as ex:
           print("JUEGO CANCELADO")
           bloquear()

    
    shiftPlayer.set("Turno: " + player1)
    

def cambiar(num):
    global turno, player1, player2
    if k[num] == "V" and turno==0:
        botones[num].config(text="X")
        botones[num].config(bg="#FAC3E7", fg="black")
        k[num]="X"
        turno = 1
        shiftPlayer.set("Turno: " + player2)
    
    elif k[num] == "V" and turno==1:
        botones[num].config(text="O")
        botones[num].config(bg="#D9FEFD", fg="black")
        k[num]="O"
        turno = 0
        shiftPlayer.set("Turno: " + player1)
    botones[num].config(state='disable')
    verificar()


def verificar():
    if (k[0]=="X" and k[1]=="X" and k[2]=="X") or (k[3]=="X" and k[4]=="X" and k[5]=="X") or (k[6]=="X" and k[7]=="X" and k[8]=="X"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player1 + ", ¡HAS GANADO!" )
        
    elif (k[0]=="X" and k[3]=="X" and k[6]=="X") or (k[1]=="X" and k[4]=="X" and k[7]=="X") or (k[2]=="X" and k[5]=="X" and k[8]=="X"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player1 + ", ¡HAS GANADO!")
    elif (k[0]=="X" and k[4]=="X" and k[8]=="X") or (k[2]=="X" and k[4]=="X" and k[6]=="X"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player1 + ", ¡HAS GANADO!")
    
    elif (k[0]=="O" and k[1]=="O" and k[2]=="O") or (k[3]=="O" and k[4]=="O" and k[5]=="O") or (k[6]=="O" and k[7]=="O" and k[8]=="O"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player2 + ", ¡HAS GANADO!")
    elif (k[0]=="O" and k[3]=="O" and k[6]=="O") or (k[1]=="O" and k[4]=="O" and k[7]=="O") or (k[2]=="O" and k[5]=="O" and k[8]=="O"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player2 + ", ¡HAS GANADO!")
    elif (k[0]=="O" and k[4]=="O" and k[8]=="O") or (k[2]=="O" and k[4]=="O" and k[6]=="O"):
        bloquear()
        messagebox.showinfo("GANADOR", "FELICIDADES " + player2 + ", ¡HAS GANADO!")
    elif (k[0]!="V" and k[1]!="V" and k[2]!="V" and k[3]!="V" and k[4]!="V" and k[5]!="V" and k[6]!="V" and k[7]!="V" and k[8]!="V") :
        messagebox.showinfo("EMPATE", player1 + " Y " + player2 + ", HAN QUEDADO EN EMPATE" )

vnta = Tk()
vnta.geometry("420x560")
vnta.title("Paz y bien Jugadores...")
vnta.config(bg="#D0DDCE")
vnta.maxsize(width=420, height=560)

turno = 0
player1 = ""
player2 = ""

botones = []

k = []

shiftPlayer = StringVar()




for i in range(0,9):
    k.append("V")

boton1 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(0))
boton1.place(x=40, y=80)

botones.append(boton1)

boton2 = Button(vnta, text="",width=12, height=6,command=lambda: cambiar(1))
boton2.place(x=160, y=80)

botones.append(boton2)

boton3 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(2))
boton3.place(x=280, y=80)

botones.append(boton3)

boton4 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(3))
boton4.place(x=40, y=200)

botones.append(boton4)

boton5 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(4))
boton5.place(x=160, y=200)

botones.append(boton5)

boton6 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(5))
boton6.place(x=280, y=200)

botones.append(boton6)

boton7 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(6))
boton7.place(x=40, y=320)

botones.append(boton7)

boton8 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(7))
boton8.place(x=160, y=320)
botones.append(boton8)

boton9 = Button(vnta, text="",width=12, height=6, command=lambda: cambiar(8))
boton9.place(x=280, y=320)
botones.append(boton9)

turnoTxt = Label(vnta, textvariable=shiftPlayer, font=("Arial",20,"bold"), bg="#D0DDCE").place(x=80, y=20)

iniciar = Button(vnta, text="Iniciar juego",width=10, height=2,font=("Arial",12,"bold"), command=iniciarP)
iniciar.config(bg="#F9614C", fg="white")
iniciar.place(x=40,y=460)

continuar = Button(vnta, text="Nuevos jugadores",width=20, height=2,font=("Arial",12,"bold"), command=jugadoresP)
continuar.config(bg="#F94C95", fg="white")
continuar.place(x=170,y=460)

realizado = Label(vnta, text="Realizado por Laura Juliana Serrano Garcia - Makeajse", bg="#D0DDCE").place(x=100, y=530)

bloquear()

vnta.mainloop()