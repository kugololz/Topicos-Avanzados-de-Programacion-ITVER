import tkinter
from tkinter import *

ventana = Tk()
ventana.title('Mi primera ventana')
ventana.geometry('800x600')
ventana.resizable(True, True)
ventana.configure(bg="#FFFFFF")
ventana.maxsize(1900,1820)

etiqueta1 = Label(ventana, text = "Hola mi prmier GUI Python")
etiqueta1.pack()

etiquetaFormato = Label(ventana, text = "Este es un ejemlo de ventana formateada", 
                        font = ("Comic Sans", 40), pady = 10, padx = 20, relief= "raised",
                        background= "black", foreground= "white")
etiquetaFormato.pack()

ventana.state('zoomed')
ventana.mainloop()

