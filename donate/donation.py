from tkinter import *
from tkinter import PhotoImage

class Root:
    def __init__(self, interfaz) -> None:
        self.gui = interfaz
        self.gui.resizable(0,0)
        self.gui.title('Doname algo')

        self.imagen = PhotoImage(file='donate/BTCQR.png')
        Label(self.gui, image=self.imagen).pack()

obj=Root(Tk())
obj.gui.mainloop()