#Emplezar proyecto 30/06/2024 12:37 AM#
#iportar toda las librerias contenidas en .imports.py
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import webbrowser
from tkinter import messagebox as mBox
import os

#diseno de la interfaz
class Windows:
    def __init__(self, interfaz) -> None:
        self.root = interfaz
        self.root.title('TKC`s')
        self.root.geometry('700x320')
        self.root.resizable(0,0)
        self.root.config(bg='black')
        self.frame1 = Frame(self.root, borderwidth=5, relief=SUNKEN, background='red').pack(expand=True, side='top', anchor='n', ipadx=750, ipady=25)
        self.Menus()
        self.Entradas()
        self.Botones()
        self.Listas()
        self.Texto()
#agragar fotos y logos
        self.imagen = PhotoImage(file='images/foto1.png')
        Label(self.root, image=self.imagen, bd=0).place(x=0,y=150)
        self.imagen2 = PhotoImage(file='images/Diapositiva1.png')
        Label(self.frame1, image=self.imagen2, bd=0).place(x=320,y=10)
#creacion de los menus----------------------------
    def Menus(self):
        self.barramenu = Menu(self.root)
        self.root.config(menu=self.barramenu)

        self.opc1 = Menu(self.barramenu, tearoff=0)
        self.opc1.add_command(label='Uso', command=self.Usos)
#menu1
        self.opc2 = Menu(self.barramenu, tearoff=0)
        self.opc2.add_command(label='Tor', command=self.Tor)
        self.opc2.add_separator()
        self.opc2.add_command(label='Kali linux', command=self.KLux)
        self.opc2.add_separator()
        self.opc2.add_command(label='VPN', command=self.VPN)
        self.opc2.add_separator()
        self.opc2.add_command(label='private mail', command=self.Pmail)
#menu3  
        self.opc3 = Menu(self.barramenu, tearoff=0)      
        self.opc3.add_command(label='libre en la red', command=self.FREE)
        self.opc3.add_separator()
        self.opc3.add_command(label='DONAME ALGO AHÍ', command=self.Donate)

        self.barramenu.add_cascade(label='Ayuda', menu=self.opc1)
        self.barramenu.add_cascade(label='Herramientas web',menu=self.opc2)
        self.barramenu.add_cascade(label='Camino a la libertad',menu=self.opc3)

#textos en pantalla
    def Texto(self):
        Label(self.root, text='Generar FAKE ID de: UK', background='green', relief=SUNKEN, width=20).place(x=0,y=80)
        Label(self.root, text='Fake Address: USA', background='green', relief=SUNKEN, width=20).place(x=0,y=120)
        Label(self.root, text='Encriptado', background='green', relief=SUNKEN, width=20).place(x=400,y=80)
        Label(self.root, text='Desencriptado', background='green', relief=SUNKEN, width=20).place(x=400,y=120)
        Label(self.root, text='FTP fuerza bruta', background='green', relief=SUNKEN, width=20).place(x=400,y=160)
        Label(self.root, text='ATK diccionario', background='green', relief=SUNKEN, width=20).place(x=400,y=200)
#entradas en pantallas
    def Entradas(self):
        pass
#botones en pantalla
    def Botones(self):
        Button(self.root, text='Salir', width=10, background='red', cursor='pirate', command=self.Salir).place(x=600,y=270)
        Button(self.root, text='Generar', width=10, background='red', cursor='pirate', command=self.FID).place(x=150,y=78)
        Button(self.root, text='Generar', width=10, background='red', cursor='pirate', command=self.FADD).place(x=150,y=118)
        Button(self.root, text='Web Scrap', width=10, background='green', command=self.WSCR).place(x=10,y=15)
        Button(self.root, text='Geo Loc', width=10, background='green', command=self.GeoLoc).place(x=150,y=15)
        Button(self.root, text='Brute Subdomain', width=20, background='green', command=self.Brute_sub).place(x=450,y=15)
        Button(self.root, text='Generar', width=10, background='red', cursor='heart', command=self.Encriptado).place(x=550,y=78)
        Button(self.root, text='Generar', width=10, background='red', cursor='heart', command=self.Decript).place(x=550,y=118)
        Button(self.root, text='Generar', width=10, background='red', cursor='heart', command=self.FTP).place(x=550,y=158)
        Button(self.root, text='Generar', width=10, background='red', cursor='heart', command=self.DICT).place(x=550,y=198)


#listas despleglabes
    def Listas(self):
        pass

#funciones

    def Salir(self):
        self.root.quit()
        self.root.destroy()

    def FID(self):
        from fake_id import fiduk

    def FADD(self):
        from fake_id import fidusa

    def Tor(self):
        webbrowser.open('https://www.torproject.org')

    def KLux(self):
        webbrowser.open('https://www.kali.org')

    def VPN(self):
        webbrowser.open('https://protonvpn.com')

    def Pmail(self):
        webbrowser.open('https://proton.me/mail')

    def FREE(self):
        webbrowser.open('menu\index.html')

    def Donate(self):
        from donate import donation

    def WSCR(self):
        from scrapp import scrapping

    def Encriptado(self):
        from encript import encript2

    def Decript(self):
        from encript import decript2

    def Usos(self):
        webbrowser.open_new('uso\index.html')

    def FTP(self):
        from ftp import fbrute

    def DICT(self):
        from dict import main

    def GeoLoc(self):
        from geo import geoip

    def Brute_sub(self):
        from subdominios import bsubdom


objeto = Windows(Tk())
objeto.root.mainloop()