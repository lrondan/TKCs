from tkinter import *
from tkinter import messagebox as mBox
import hashlib

class App:
    def __init__(self, interfaz):
        self.app = interfaz
        self.app.geometry('300x200')
        self.app.resizable(0,0)
        self.app.title('Desencriptado')
        self.app.config(bg='blue')
        self.Vistas()

    def Vistas(self):
        self.clave = StringVar()
        self.type = StringVar()
        Label(self.app, text='Introduzca el texto a desencriptar:').place(x=5,y=0)
        Label(self.app, text='Hash a resolver: ').place(x=5,y=80)
        Entry(self.app, textvariable=self.clave, width=45).place(x=5, y=25)
        Entry(self.app, textvariable= self.type, width=25).place(x=5,y=105)
        Button(self.app, text='OK',command=self.main).place(x=165,y=105)
        Button(self.app, width=7, text='Salir', command=self.Salir).place(x=230,y=160)


#funciones
    def main(self):
        try:
            resolvedor = open('encript/archivo_resolv.txt')
            for x in resolvedor.readlines():
                a = x.strip('\n').encode('utf-8')
                if self.type.get() == 'md5':
                    a = hashlib.md5(a).hexdigest()
                    mBox('respuestas',a)
                elif self.type.get() == 'sha1':
                    a = hashlib.sha1(a).hexdigest()
                    mBox('respuestas',a)
                elif self.type.get() == 'sha224':
                    a = hashlib.sha224(a).hexdigest()
                    mBox('respuestas',a)
                elif self.type.get() == 'sha256':
                    a = hashlib.sha256(a).hexdigest()
                    mBox('respuestas',a)
                elif self.type.get() == 'sha384':
                    a = hashlib.sha384(a).hexdigest()
                    mBox('respuestas',a)
                elif self.type.get() == 'sha512':
                    a = hashlib.sha512(a).hexdigest()
                    mBox('respuestas',a)
                else:
                    mBox.showerror('Tipo de encriptado no valido')
                
                if a == self.type.get():
                    print('ok')
                    break
        except Exception as e:
            mBox.showerror(e)
            

    def Salir(self):
        self.app.quit()
        self.app.destroy()

objeto = App(Tk())
objeto.app.mainloop()