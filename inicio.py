#!/usr/bin/env python
# -*- coding: utf-8 -*
from tkinter import *
from PIL import ImageTk
from PIL import Image
import index as rox
import time


class SimpleApp():
    def __init__(self, **kwargs):
        root = Tk()

        self.filename = './images/256x256.png'
        self.master = root

        self.master.resizable(0, 0)
        ancho_ventana = 720
        alto_ventana = 480

        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

        self.master.geometry(posicion)
        self.master.config(bg="#141454")
        self.canvas = Canvas(root, width=480, height=400, bg="#141454", highlightthickness=0)
        self.canvas.pack()
        self.salida = []
        with open('./preferencias.txt', 'r') as f:
            # with open('./preferencias.txt', 'r') as f:
            lineas = [linea.split() for linea in f]
        for linea in lineas:
            self.salida.append(linea)
        i = 0
        self.elementos = self.salida
        tam = len(self.salida)
        if tam == 0:
            self.lbl = Label(self.master, anchor="n", justify=RIGHT, width=33,
                             text="Hola, soy Roxana, y seré tu asistente", bg="#141454", fg="white", font=("Arial", 18))
            self.lbl.pack(expand=True, fill=X)
            self.update = self.draw(1).__next__
            root.after(10, self.update)
        else:
            self.lbl = Label(self.master, anchor="n", justify=RIGHT, width=33, text="Hola, que gusto verte otra vez",
                             bg="#141454", fg="white", font=("Arial", 18))
            self.lbl.pack(expand=True, fill=X)
            self.update = self.draw(2).__next__
            root.after(10, self.update)

        root.mainloop()

    def draw(self, num):
        image = Image.open(self.filename)
        angle = 0
        c = 0
        salida = []
        if num == 1:
            with open('inicio.txt', 'r') as f:
                lineas = [linea.split() for linea in f]
        else:
            with open('inicio2.txt', 'r') as f:
                lineas = [linea.split() for linea in f]

        for linea in lineas:
            salida.append(linea)

        i = 0
        tam = len(salida)

        while True and i <= tam:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                235, 235, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle -= 5
            angle %= 360
            c += 1
            if c % 150 == 0:
                if i == tam - 1:
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 19))
                    self.master.update()
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 20))
                    self.master.update()
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 21))
                    self.master.update()
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 22))
                    self.master.update()
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 23))
                    self.master.update()
                    time.sleep(0.0005)
                    self.lbl.config(font=("Arial", 24))
                    self.master.update()
                    i = tam + 1


                else:
                    self.lbl.config(text=salida[i])
                    i += 1
        if i == tam + 1:
            i = 0
            self.canvas.delete()
            self.master.destroy()
            a = rox.Roxana()


b = SimpleApp()
