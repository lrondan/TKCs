from tkinter import *
from tkinter import messagebox as mBox
import hashlib

class App:
    def __init__(self, interfaz):
        self.app = interfaz
        self.app.geometry('300x200')
        self.app.resizable(0,0)
        self.app.title('Encriptado')
        self.app.config(bg='red')
        self.Vistas()

    def Vistas(self):
        self.clave = StringVar() 
        Label(self.app, text='Introduzca el texto a cifrar:').place(x=0,y=0)
        Entry(self.app, textvariable=self.clave, width=45).place(x=0, y=25)
        Button(self.app, width=7, text='MD5', command=self.MD5).place(x=25,y=60)
        Button(self.app, width=7, text='SHA224', command=self.SHA224).place(x=125,y=60)
        Button(self.app, width=7, text='SHA256', command=self.SHA256).place(x=225,y=60)
        Button(self.app, width=7, text='SHA384', command=self.SHA384).place(x=25,y=160-50)
        Button(self.app, width=7, text='SHA512', command=self.SHA512).place(x=125,y=160-50)
        Button(self.app, width=7, text='SHA1', command=self.SHA1).place(x=225,y=160-50)
        Button(self.app, width=7, text='Salir', command=self.Salir).place(x=230,y=160)    



#funciones
    def MD5(self):
        md5 = hashlib.md5(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash MD5:'," %s" % str(md5))
        with open('./mensaje.txt', 'w')as file:
            for lines in md5:
                file.write(lines)
        
        
    def SHA224(self):
        sha224 = hashlib.sha224(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash SHA224:', "%s" % str(sha224))
        with open('./mensaje.txt', 'w')as file:
            for lines in sha224:
                file.write(lines)

    def SHA256(self):
        sha256 = hashlib.sha256(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash SHA256:', "%s" % str(sha256))
        with open('./mensaje.txt', 'w')as file:
            for lines in sha256:
                file.write(lines)

    def SHA384(self):
        sha384 = hashlib.sha384(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash SHA384:', "%s" % str(sha384))
        with open('./mensaje.txt', 'w')as file:
            for lines in sha384:
                file.write(lines)

    def SHA512(self):
        sha512 = hashlib.sha512(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash SHA512:', "%s" % str(sha512))
        with open('./mensaje.txt', 'w')as file:
            for lines in sha512:
                file.write(lines)

    def SHA1(self):    
        sha1 = hashlib.sha1(self.clave.get().encode('utf-8')).hexdigest()
        mBox.showinfo('Hash SHA1:', "%s" % str(sha1))
        with open('./mensaje.txt', 'w')as file:
            for lines in sha1:
                file.write(lines)

    def Salir(self):
        self.app.quit()
        self.app.destroy()

objeto = App(Tk())
objeto.app.mainloop()