#Emplezar proyecto 30/06/2024 12:37 AM#
#iportar toda las librerias contenidas en .imports.py
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

#diseno de la interfaz
class Windows:
    def __init__(self, interfaz) -> None:
        self.root = interfaz
        self.root.title('TKC`s')
        self.root.geometry('750x520')
        self.root.resizable(0,0)
        self.root.config(bg='black')
        self.frame1 = Frame(self.root, borderwidth=5, relief=SUNKEN, background='red').pack(expand=True, side='top', anchor='n', ipadx=750, ipady=25)
        self.Menus()
        self.Entradas()
        self.Botones()
#agragar fotos y logos
        self.imagen = PhotoImage(file='images/foto1.png')
        Label(self.root, image=self.imagen, bd=0).place(x=-25,y=330)
        self.imagen2 = PhotoImage(file='images/Diapositiva1.png')
        Label(self.frame1, image=self.imagen2, bd=0).place(x=320,y=10)
#creacion de los menus----------------------------
    def Menus(self):
        self.barramenu = Menu(self.root)
        self.root.config(menu=self.barramenu)

        self.opc1 = Menu(self.barramenu, tearoff=0)
        self.opc1.add_command(label='opc1')
#menu1
        self.opc2 = Menu(self.barramenu, tearoff=0)
        self.opc2.add_command(label='opc1')
        self.opc2.add_separator()
        self.opc2.add_command(label='opc2')
#menu3  
        self.opc3 = Menu(self.barramenu, tearoff=0)      
        self.opc3.add_command(label='opc1')
        self.opc3.add_separator()
        self.opc3.add_command(label='opc2')
        self.opc3.add_separator()
        self.opc3.add_command(label='opc3')

        self.barramenu.add_cascade(label='Desp1', menu=self.opc1)
        self.barramenu.add_cascade(label='Desp2',menu=self.opc2)
        self.barramenu.add_cascade(label='Desp3',menu=self.opc3)

#textos en pantalla
    def Texto(self):
        pass
#entradas en pantallas
    def Entradas(self):
        pass
#botones en pantalla
    def Botones(self):
        Button(self.root, text='Salir', width=10, justify=CENTER, background='red', cursor='pirate', font=BEVEL).place(x=650,y=470)
#funciones
    def Salir(self):
        self.root.quit()
        self.root.destroy()

        
objeto = Windows(Tk())
objeto.root.mainloop()