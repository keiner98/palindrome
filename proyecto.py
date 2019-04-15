
import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import re
import os
import time

class mostrar():

    def __init__(self):
        self.lista=list()
        self.ventana()
    
    def funciones(self):
        self.grafo()
        self.validar()

        
    def ventana(self):
        self.vista=tk.Tk()
        self.vista.title("Grafico")
        self.vista.geometry('800x400')
        self.texto=tk.Label(self.vista,text="Ingrese palabra palindrome:",font=("Agency FB",14))
        self.texto.pack(padx=0,pady=0)
        self.texto.place(x=10, y=10)
        self.dato=tk.Entry(self.vista,text="validar")
        self.dato.place(x=10, y=40)
        self.boton= tk.Button(self.vista,text="Validar",fg="black",command=self.funciones)
        self.boton.place(x=150, y=40)
        self.vista.mainloop()

    def validar(self):     
        palabra = self.dato.get()
        validar2 = re.match('^[a-zA-Z0-9]+',palabra)
        valen = len(palabra)%2
        total = len(palabra)
        if valen == 1 and total >=3 and validar2 is not None:
            pos = 15
            cont=0
            for i in self.lista:
                self.lista[cont].destroy()
                cont=cont+1 
         
            for i in palabra:
                botonp= tk.Button(self.vista,text=i,fg="black",background="blue",command=self.animaciones)
                botonp.pack(padx=0,pady=0,ipadx=130,ipady=10)
                botonp.grid(row=0, column=1, columnspan=3, sticky='EWNS')
                botonp.place(x=(10)+pos, y=70)
                pos = pos + 15
                self.lista.append(botonp)
        else:
            messagebox.showerror("Validación","Dato invalido")


    def grafo(self):
        self.circulo = Canvas(width=380,height=220,bg="#EFEFEF")
        self.circulo.pack(expand=NO)
        self.circulo.place(x=20,y=160)
        #Lineas de inicio      
        self.circulo.create_line(0,150,23,150,width=4,fill="black")
        self.circulo.create_line(12,140,23,150,width=4,fill="black")
        self.circulo.create_line(12,160,23,150,width=4,fill="black")
        
        #creacion del primer estado
        self.circulo.create_oval(23, 95, 65, 130, width=2, fill='white')
        self.circulo.create_oval(25, 120, 85, 180, width=5, fill='white')
        self.circulo.create_text(55, 150, text='P', fill='black')

        #transiciones primer estado
        self.circulo.create_text(35, 85, text='a,#/#a', fill='black')
        self.circulo.create_text(35, 70, text='b,#/#b', fill='black')
        self.circulo.create_text(35, 55, text='a,a/aa', fill='black')
        self.circulo.create_text(35, 40, text='b,a/ab', fill='black')
        self.circulo.create_text(35, 25, text='a,b/ba', fill='black')
        self.circulo.create_text(35, 10, text='b,b/bb', fill='black')
        self.circulo.create_line(85, 150, 175, 150, width=5, fill='black')
        #transiciones de la linea 1
        self.circulo.create_text(125, 135, text='c,b/b', fill='black')
        self.circulo.create_text(125, 120, text='c,#/#', fill='black')
        self.circulo.create_text(125, 165, text='c,b/b', fill='black')
        self.circulo.create_oval(173, 95, 215, 130, width=2, fill='white')
        self.circulo.create_oval(175, 120, 235, 180, width=5, fill='white')
        self.circulo.create_text(205, 150, text='q', fill='black')
        self.circulo.create_line(235, 150, 315, 150, width=5, fill='black')

        #transiciones del sendo estado
        self.circulo.create_text(220, 85, text='a,a/λ', fill='black')
        self.circulo.create_text(220, 70, text='b,b/λ', fill='black')
        
        #transicion de la linea 2
        self.circulo.create_text(280, 165, text='λ,#/#', fill='black')

        #creacion del segundo estado
        self.circulo.create_oval(315, 120, 375, 180, width=5, fill='white')
        self.circulo.create_oval(320, 125, 370, 175, width=2, fill='white')
        self.circulo.create_text(345, 150, text='r', fill='black')


    def animaciones(self):
        self.pintar1
        self.tiempo()
        self.pintar2()           
        
    def tiempo(self):
        time.sleep(3)

    def pintar1(self,x):
        self.circulo.create_line(0,150,23,150,width=4,fill="red")
        self.circulo.create_line(12,140,23,150,width=4,fill="red")
        self.circulo.create_line(12,160,23,150,width=4,fill="red")

    def pintar2(self):
        self.circulo.create_line(0,150,23,150,width=4,fill="black")
        self.circulo.create_line(12,140,23,150,width=4,fill="black")
        self.circulo.create_line(12,160,23,150,width=4,fill="black")

x=mostrar()