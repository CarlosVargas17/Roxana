#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from threading import *
from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import date
import time
import speech_recognition as sr
import webbrowser
import pywhatkit
from datetime import datetime
import pyttsx3
import urllib.request
import wikipedia
import json
import os
import pyjokes
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from googletrans import Translator
from tkinter import ttk as ttk
import ttkthemes as them
from gtts import gTTS
import playsound

class Roxana():
    def __init__(self):

        self.backcolor = "#141454"
        self.fgcolor = "white"
        self.salida = []
        """
        Preferencias:
        Nombre:
        Nacimiento:
        Tema:
        Idioma:
        Lugar:
        """
        with open('./preferencias.txt', 'r') as f:
            # with open('./preferencias.txt', 'r') as f:
            lineas = [linea.split() for linea in f]
        for linea in lineas:
            self.salida.append(linea)
        i = 0
        self.temas=[['Claro', 'Oscuro (por defecto)', 'Verde', 'Rojo', 'Cielo', 'Morado'],
               ["#ffffff","#141454","#34B677","#FB2929","#31DFE8","#340A3C"],
               ["#000000","#ffffff","#ffffff","#ffffff","#000000","#ffffff"]]



        self.elementos = self.salida
        tam = len(self.salida)
        if tam == 0:
            self.encuesta()
        else:
            for i in range(len(self.temas[0])):
                print(str(self.salida[2]))
                print("0", self.temas[0][i])
                if self.temas[0][i] in self.salida[2]:

                    print("1",self.temas[1][i])
                    print("2",self.temas[2][i])
                    self.backcolor = self.temas[1][i]
                    self.fgcolor = self.temas[2][i]
            self.ventana()

    def encuesta(self):
        self.root = them.ThemedTk(theme="arc")
        #self.root.overrideredirect(True)
        ax = them.THEMES
        print(ax)
        # ['adapta', 'aquativo', 'arc', 'black', 'blue', 'breeze',
        # 'clearlooks', 'elegance', 'equilux', 'itft1', 'keramik',
        # 'kroc', 'plastik', 'radiance', 'scidblue', 'scidgreen',
        # 'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand',
        # 'smog', 'ubuntu', 'winxpblue', 'yaru']

        ancho_ventana = 720
        alto_ventana = 480
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root.geometry(posicion)
        self.root.config(bg=self.backcolor)
        self.root.wm_attributes('-topmost', False)
        self.root.iconbitmap('./images/icon.ico')
        #self.root.overrideredirect(False)
        self.root.resizable(0, 0)
        imagen = ("./images/64x64.png")
        imagen02 = ("./images/256x256.png")
        self.imagen2 = ImageTk.PhotoImage(image=Image.open(imagen02))
        # imagen = ("./images/64x64.png")
        self.imagen = ImageTk.PhotoImage(image=Image.open(imagen))
        self.logo = Label(self.root, image=self.imagen, bg=self.backcolor)
        self.logo.place(x=15, y=5)
        self.lbl1 = Label(self.root, text="Te realizaré una encuesta para conocerte un poco mas", font=("Arial", 16),
                          bg=self.backcolor, fg=self.fgcolor)
        self.lbl1.place(x=125, y=20)
        self.lbl2 = Label(self.root, text="La siguiente información será solo utilizada para que Roxana\n"
                                          "te conozca un poco mas, no se utilizará de otra manera,\n"
                                          "pero es totalmente obligatoria para mejorar tu experiencia.\n"
                                          "Al presionar Acepto, aceptarás nuestros terminos no estaticos\n"
                                          "si presionas No Acepto, el programa se cerrará.", font=("Arial", 12),
                          bg=self.backcolor, fg=self.fgcolor)
        self.lbl2.place(x=150, y=60)

        self.btn1 = Button(self.root, text="Acepto", command=self.aceptar, font=("Arial", 11), bg="#139134",
                           fg=self.fgcolor, highlightthickness=0, highlightcolor="green", relief="flat",
                           activeforeground=self.fgcolor, activebackground="green")
        self.btn1.place(x=540, y=170)
        self.btn2 = Button(self.root, text="No Acepto", command=self.declinar, font=("Arial", 11), bg="#FB2929",
                           fg=self.fgcolor, highlightthickness=0, highlightcolor="red", relief="flat",
                           activeforeground=self.fgcolor, activebackground="red")
        self.btn2.place(x=440, y=170)
        self.root.mainloop()

    def aceptar(self):
        self.logo.config(image=self.imagen2)
        self.logo.place(x=420, y=55)
        self.btn1.destroy()
        self.btn2.destroy()
        self.lbl1.config(text="Contesta por favor con la verdad", font=("Arial", 18))
        self.lbl1.place(x=20, y=10)
        self.lbl2.config(text="¿Cómo te llamas?")
        self.lbl2.place(x=28, y=50)
        self.ent1 = Entry(self.root, font=("Arial", 10), fg="black", width=44)
        self.ent1.place(x=20, y=80)
        self.lbl3 = Label(self.root, text="¿Cuál es tu fecha de nacimiento?", font=("Arial", 12), bg=self.backcolor,
                          fg=self.fgcolor)
        self.lbl3.place(x=23, y=110)
        now = datetime.now()
        anio = now.year
        mes = now.month
        dia = now.day
        self.de = DateEntry(self.root, locale='es_MX', date_pattern='dd/mm/y', year=anio, month=mes, day=dia, width=26,
                            selectmode='day', cursor="hand1", font="Arial 14", highlightthickness=0,
                            selectbackground='gray80',
                            selectforeground='black',
                            normalbackground='white',
                            normalforeground='black',
                            background='gray90',
                            foreground='black',
                            bordercolor='gray90',
                            othermonthforeground='gray50',
                            othermonthbackground='white',
                            othermonthweforeground='gray50',
                            othermonthwebackground='white',
                            weekendbackground='white',
                            weekendforeground='black',
                            headersbackground='white',
                            headersforeground='gray70')
        self.de.place(x=20, y=140)
        self.lbl4 = Label(self.root, text="Selecciona un tema", font=("Arial", 12), bg=self.backcolor, fg=self.fgcolor)
        self.lbl4.place(x=28, y=170)
        tema = StringVar()
        self.temas = ttk.Combobox(self.root, width=47, textvariable=tema, state="readonly")
        self.temas.set("Oscuro (por defecto)")
        self.temas['values'] = ('Claro', 'Oscuro (por defecto)', 'Verde', 'Rojo', 'Cielo', 'Morado')
        self.temas.place(x=20, y=200)
        self.temas.bind("<<ComboboxSelected>>", self.detecta_cambio)

        self.lbl5 = Label(self.root, text="Selecciona un idioma", font=("Arial", 12), bg=self.backcolor,
                          fg=self.fgcolor)
        self.lbl5.place(x=27, y=230)
        idiomas = StringVar()
        self.idioma = ttk.Combobox(self.root, width=47, textvariable=idiomas, state="readonly")
        self.idioma['values'] = ('Español', 'Ingles', 'Chino', 'Ruso', 'Francés', 'portugués')
        self.idioma.place(x=20, y=260)
        self.idioma.bind("<<ComboboxSelected>>", self.detecta_idioma)

        self.lbl6 = Label(self.root, text="Datos geograficos", font=("Arial", 12), bg=self.backcolor, fg=self.fgcolor)
        self.lbl6.place(x=27, y=290)

        place2 = "CP"
        self.ent3 = Entry(self.root, font=("Arial", 12), width=10, fg='Grey')
        self.ent3.insert(0, place2)
        self.ent3.bind("<FocusIn>", lambda args: self.entradabox(self.ent3))
        self.ent3.bind("<FocusOut>", lambda args: self.salidabox(place2, self.ent3))
        self.ent3.bind('<KeyRelease>', lambda e: self.verifica(self.ent3, '0123456789'))
        self.ent3.place(x=20, y=320)

        place1 = "Ciudad"
        self.ent2 = Entry(self.root, font=("Arial", 12), fg='Grey', width=20)
        self.ent2.insert(0, place1)
        self.ent2.bind("<FocusIn>", lambda args: self.entradabox(self.ent2))
        self.ent2.bind("<FocusOut>", lambda args: self.salidabox(place1, self.ent2))
        self.ent2.place(x=150, y=320)

        self.lbl7 = Label(self.root, text="Estado", font=("Arial", 12), bg=self.backcolor, fg=self.fgcolor)
        self.lbl7.place(x=20, y=350)

        estado = StringVar()
        self.estados = ttk.Combobox(self.root, width=48, textvariable=estado, state="readonly")
        self.estados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur",
                                  "Campeche", "Coahuila de Zaragoza", "Colima", "Chiapas",
                                  "Chihuahua", "Distrito Federal", "Durango", "Guanajuato",
                                  "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán de Ocampo",
                                  "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro",
                                  "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
                                  "Tamaulipas", "Tlaxcala", "Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas")
        self.estados.place(x=20, y=380)

        self.btn3 = Button(self.root, text="Confirmar", width=22, height=1, command=self.llena, font=("Arial", 18),
                           bg="#139134", fg=self.fgcolor, highlightthickness=0, highlightcolor="green", relief="flat",
                           activeforeground=self.fgcolor, activebackground="green")
        self.btn3.place(x=20, y=410)

        self.idioma.update()

    def declinar(self):
        exit()

    def salidabox(self, text, elem):
        place1 = text
        if elem['fg'] == 'Black' and len(elem.get()) == 0:
            elem.delete(0, END)
            elem['fg'] = 'Grey'
            elem.insert(0, place1)

    def entradabox(self, elem):
        if elem['fg'] == 'Grey':
            elem['fg'] = 'Black'
            elem.delete(0, END)

    def verifica(self, elem, cadena):
        valor = elem.get()
        for i in valor:
            if i not in cadena:
                elem.delete(valor.index(i), valor.index(i) + 1)

    def llena(self):
        name = self.ent1.get()
        fecha = self.de.get()
        tema = self.temas.get()
        idioma = self.idioma.get()
        cp = self.ent3.get()
        city = self.ent2.get()

        state = self.estados.get()
        print(name)
        print(fecha)
        print(tema)
        print(idioma)
        print(cp)
        print(city)
        print(state)
        if name != "" and tema != "" and idioma != "" and cp != "" and city != "" and state != "":
            text = name + "\n" + fecha + "\n" + tema + "\n" + idioma + "\n" + cp + "\n" + city + "\n" + state
            print(text)
            f = open('./preferencias.txt', 'w')
            f.write(text)
            f.close()

            messagebox.showinfo(message="Tus datos han sido generados correctamente", title="Transacción satisfactoria")
            self.btn3.config(state=DISABLED)

        else:
            messagebox.showwarning(message="Algúl campo se encuentra vacio, verifique y llenelo", title="Alerta")

    def detecta_cambio(self, event):
        seleccionado = self.temas.get()
        print("Nuevo elemento seleccionado:", seleccionado)

        temas = [['Claro', 'Oscuro (por defecto)', 'Verde', 'Rojo', 'Cielo', 'Morado'],
                      ["#ffffff", "#141454", "#34B677", "#FB2929", "#31DFE8", "#340A3C"],
                      ["#000000", "#ffffff", "#ffffff", "#ffffff", "#000000", "#ffffff"]]

        for i in range(len(temas[0])):
            if temas[0][i] in seleccionado:
                print("1", temas[1][i])
                print("2", temas[2][i])
                self.backcolor = temas[1][i]
                self.fgcolor = temas[2][i]


        self.root.config(bg=self.backcolor)
        self.root.wm_attributes('-topmost', False)
        self.root.iconbitmap('./images/icon.ico')
        self.lbl1.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl2.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl3.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl4.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl5.config(bg=self.backcolor, fg=self.fgcolor)
        self.logo.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl6.config(bg=self.backcolor, fg=self.fgcolor)
        self.lbl7.config(bg=self.backcolor, fg=self.fgcolor)

        self.root.update()

    def detecta_idioma(self, event):
        seleccionado = self.idioma.get()
        print("Nuevo idioma seleccionado:", seleccionado)

    def ventana(self):
        name0 = self.elementos[0]
        name = ""
        for i in (name0):
            name += (i + " ")
        print(name)
        print(self.salida)
        print(self.elementos)

        self.root = them.ThemedTk(theme="arc")
        ax = them.THEMES
        print(ax)
        # ['adapta', 'aquativo', 'arc', 'black', 'blue', 'breeze',
        # 'clearlooks', 'elegance', 'equilux', 'itft1', 'keramik',
        # 'kroc', 'plastik', 'radiance', 'scidblue', 'scidgreen',
        # 'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand',
        # 'smog', 'ubuntu', 'winxpblue', 'yaru']

        ancho_ventana = 720
        alto_ventana = 480
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root.geometry(posicion)
        self.root.config(bg=self.backcolor)
        self.root.wm_attributes('-topmost', False)
        self.root.iconbitmap('./images/icon.ico')
        #self.root.overrideredirect(True)
        self.root.resizable(0, 0)
        imagen = ("./images/64x64.png")
        imagen02 = ("./images/256x256.png")
        imagen03 = ("./images/256x256_i.png")
        self.imagen2 = ImageTk.PhotoImage(image=Image.open(imagen02))
        # imagen = ("./images/64x64.png")
        self.imagen = ImageTk.PhotoImage(image=Image.open(imagen))
        self.micro = ImageTk.PhotoImage(image=Image.open(imagen03))
        self.logo = Label(self.root, image=self.imagen, bg=self.backcolor)
        self.logo.place(x=15, y=5)
        self.lbl1 = Label(self.root, text=("Bienvenido " + name), anchor="n", justify=RIGHT, width=33,
                          font=("Arial", 22), bg=self.backcolor, fg=self.fgcolor)
        self.lbl1.place(x=95, y=20)
        self.btnmic = Button(self.root, text="", image=self.micro, command=self.escuchando, bg=self.backcolor,
                             fg=self.fgcolor, highlightthickness=0, highlightcolor=self.backcolor,
                             activebackground=self.backcolor, relief="flat")
        self.btnmic.place(x=232, y=80)

        """self.btn1 = Button(self.root, text="Acepto", command=self.aceptar, font=("Arial", 11), bg="#139134",
                           fg=self.fgcolor, highlightthickness=0, highlightcolor="green", relief="flat",
                           activeforeground=self.fgcolor, activebackground="green")
        self.btn1.place(x=540, y=170)
        self.btn2 = Button(self.root, text="No Acepto", command=self.declinar, font=("Arial", 11), bg="#FB2929",
                           fg=self.fgcolor, highlightthickness=0, highlightcolor="red", relief="flat",
                           activeforeground=self.fgcolor, activebackground="red")
        self.btn2.place(x=440, y=170)"""

        self.console = Label(self.root, text="Presiona para escucharte", width=39, anchor="n", justify=RIGHT,
                             font=("Arial", 22), bg=self.backcolor, fg=self.fgcolor)
        self.console.place(x=20, y=380)
        self.root.mainloop()

    def escuchando(self):
        t = threading.Thread( target=self.llama)
        t.start()
    def mensaje(self,texto,componente):
        componente.config(text=texto)
    def mic(self,r,source):

        self.audio = r.listen(source)

    def llama(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:

            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            ta = threading.Thread(name="self.talk",target=self.talk2("Escuchando"),daemon=True)
            wr = threading.Thread(target=self.mensaje("Escuchando", self.console), daemon=True)
            au = threading.Thread(name="self.mic",target=self.mic(r, source))
            print(self.audio)
            wr2 = threading.Thread(target=self.mensaje("Procesando", self.console))

        try:
            query = r.recognize_google(self.audio, language='es-MX')
            respuesta = query.lower()
            if "roxana" in respuesta:
                respuesta = respuesta.replace("roxana ", "")
                print("Estoy tratando de entender...")

                wr2 = threading.Thread( target=self.mensaje("Estoy tratando de entender", self.console))
                ta2 = threading.Thread( target=self.talk("estoy tratando de entender"))
                wr2.start()
                ta2.start()
                print(f"Dijiste: {respuesta}\n")

                wr3 = threading.Thread(target=self.mensaje((f"Dijiste: {respuesta}\n"), self.console))
                wr3.start()
                ta3 = threading.Thread( target=self.talk(f"Dijiste: {respuesta}\n"))
                ta3.start()

                if "facebook" in (respuesta):
                    self.talk2("Abriendo Facebook")
                    wr4 = threading.Thread(target=self.mensaje("Abriendo Facebook", self.console))
                    wr4.start()
                    webbrowser.open('https://www.facebook.com')
                if "whatsapp" in (respuesta):
                    res2 = respuesta.replace(" ", "")
                    subcadena = res2[-10:]
                    self.talk("Enviando mensaje al ", subcadena)
                    now = datetime.now()
                    num = "+52" + subcadena
                    hora = now.hour
                    min = now.minute
                    min2 = min + 1
                    print(hora, min)
                    print(num)
                    pywhatkit.sendwhatmsg(num,
                                          "Este mensaje fue enviado desde el asistente de voz, este mensaje se envió a las: " + str(
                                              hora) + ":" + str(min2) + "horas", hora, min2)
                    # 4371095941
                    self.talk("El mensaje ya fué enviado")
                if "chiste" in (respuesta) or "broma" in (respuesta):
                    broma = (pyjokes.get_joke('es'))
                    print(broma)
                    self.talk(broma)
                if "traduce" in respuesta:
                    respuesta = respuesta.replace("traduce ", "")
                    traductor = Translator()
                    tradu = traductor.translate(str(respuesta), dest='en')

                    comp = "La traduccion es: " + str(tradu.text)
                    comp2 = "La traduccion es: " + str(tradu.pronunciation)
                    print(comp)
                    self.talk(comp2)
                if "qué hora es" in respuesta:
                    now = datetime.now()
                    hora = now.hour
                    tip=""
                    tip2=""
                    if hora>12:
                        hora=hora-12
                        tip="P.M"
                        tip2="PM"
                    else:
                        tip="A.M"
                        tip2 = "AM"
                    min = now.minute
                    if hora==1:
                        if min==1:
                            frase= "es la "+str(hora)+" " + str(tip2) + " con "+str(min)+" minuto"
                            frase2 = "Es la " + str(hora)+" " + str(tip) + " con " + str(min) + " minuto"
                        else:
                            frase2 = "Es la " + str(hora)+" "+str(tip)+ " con " + str(min) + " minutos"
                            frase = "es la " + str(hora) +" " + str(tip2) +  " con " + str(min) + " minutos"
                    else:
                        if min == 1:
                            frase2 = "Son las " + str(hora)+" "+str(tip) + " con " + str(min) + " minuto"
                            frase = "son las " + str(hora) +" " + str(tip2) +  " con " + str(min) + " minuto"
                        else:
                            frase2 = "Son las " + str(hora)+" "+str(tip) + " con " + str(min) + " minutos"
                            frase = "son las " + str(hora) +" " + str(tip2) +  " con " + str(min) + " minutos"

                    threading.Thread(target=self.mensaje(frase2, self.console))
                    threading.Thread(target=self.talk(frase))
            self.reload()


        except Exception as e:
            print("No te entendi", e)
            self.talk("No comprendo lo que dijiste")
            self.reload()


    def talk(self,text):
        self.engine = pyttsx3.init()

        self.voices = self.engine.getProperty('voices')

        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 1)
        self.engine.say(text)
        #self.engine.save_to_file(text,"voz.mp3")
        self.engine.runAndWait()
    def talk2(self,text):
        #tts=gTTS(text=text,lang="es",tld="com.mx")
        #filename="voz.mp3"
        #tts.save(filename)
        filename="voz.wav"
        playsound._playsoundWin(filename)

    def reload(self):
        pass










