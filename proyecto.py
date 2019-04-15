
import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import re
import os

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
        #self.dato.grid(ipadx=50, ipady=3)
        self.boton= tk.Button(self.vista,text="Validar",fg="black",command=self.funciones)
        self.boton.place(x=150, y=40)
        self.vista.mainloop()

    def validar(self):     
        palabra = self.dato.get()
        validar2 = re.match('^[a-zA-Z0-9]+',palabra)
        valen = len(palabra)%2
        total = len(palabra)
        if valen == 1 and total >=3 and validar2 is not None:
            va = 15
            cont=0
            for i in self.lista:
                self.lista[cont].destroy()
                cont=cont+1 
         
            for i in palabra:
                botonp= tk.Button(self.vista,text=i,fg="black",background="blue")
                botonp.pack(padx=0,pady=0,ipadx=130,ipady=10)
                botonp.grid(row=0, column=1, columnspan=3, sticky='EWNS')
                botonp.place(x=(10)+va, y=70)
                va = va + 15
                self.lista.append(botonp)
                
        else:
            messagebox.showerror("Validación","Dato invalido")


    def grafo(self):
        self.circulo = Canvas(width=500,height=220,bg="gray")
        self.circulo.pack(expand=NO)
        self.circulo.place(x=20,y=160)
        self.circulo.create_oval(50,100,150,200,width=5,fill="white")
        self.circulo.create_line(220,150,150,150,width=4,fill="black")
        self.circulo.create_oval(310,100,210,200,width=5,fill="white")
        self.circulo.create_line(310,150,370,150,width=4,fill="black")
        self.circulo.create_oval(370,100,470,200,width=5,fill="white")      
        self.circulo.create_oval(380,110,460,190,width=4,fill="white")
        
x=mostrar()