from tkinter import *
import webbrowser
import json
from tkinter import messagebox as mbox

class Ventana:
    def __init__(self, interfaz) -> None:
        self.gui = interfaz
        self.gui.resizable(0,0)
        self.gui.title('GeoLoc')
        self.Lab()
        self.Ent()
        self.Bot()
        

    def Lab(self):
        Label(self.gui, text='Entre la direccion ip aqui:').pack()

    def Ent(self):
        self.ip = StringVar()
        Entry(self.gui, textvariable=self.ip, width=30, relief=SUNKEN, justify=RIGHT).pack()

    def Bot(self):
        Button(self.gui, text='Buscar',command=self.GetIp).pack()
        Button(self.gui, text='Salir',command=self.Salir).pack()

    def GetIp(self):
        url1 = "https://ipinfo.io/"
        url2 = "/json"
        ip_address = self.ip.get()
        str(ip_address)
        try:
            url = url1 + ip_address + url2
            v = webbrowser.open(url)
            j = json.loads(v.read())
            for dato in j:
               mbox.showinfo('GeoLoc',f'{dato} : {j[dato]}')
        except KeyError:
            mbox.showerror('Error','Ha ocurrido algun error!!!!')

    def Salir(self):
        self.gui.quit()
        self.gui.destroy()

objeto = Ventana(Tk())
objeto.gui.mainloop()