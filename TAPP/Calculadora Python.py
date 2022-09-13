from tkinter import *

texto = ""

def press(numero):
    global texto
    
    texto = texto + str(numero)
    valores.set(texto)
    
def resultado():
    try:
        global texto
        total = str(eval(texto))
        valores.set(total)
        
        texto = ""
    except:
        valores.set(" Inserta otro numero antes, por favor ")
        texto = ""
        
def c():
    global texto
    texto = ""
    valores.set("")
    
    

window = Tk()
window.configure(background="black")
window.title("CALCULADORA ITVER")
window.geometry("310x200")

valores = StringVar()
campo_texto = Entry(window, textvariable = valores, font =("Arial", 12))
campo_texto.grid(columnspan=4, ipadx=70)

button1 = Button(window, text=' 1 ',font =("Arial", 12), fg='black', bg='blue',
     command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(window, text=' 2 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(window, text=' 3 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(window, text=' 4 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(window, text=' 5 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(window, text=' 6 ', fg='black', bg='blue',font =("Arial", 12),
    command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(window, text=' 7 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(window, text=' 8 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(window, text=' 9 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(window, text=' 0 ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(window, text=' + ', fg='black', bg='blue',font =("Arial", 12),
    command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ', fg='black', bg='blue',font =("Arial", 12),
    command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(window, text=' * ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(window, text=' / ', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(window, text=' = ', fg='black', bg='blue',font =("Arial", 12),
    command=resultado, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(window, text='Clear', fg='black', bg='blue',font =("Arial", 12),
    command=c, height=1, width=7)
clear.grid(row=5, column='1')

Decimal= Button(window, text='.', fg='black', bg='blue',font =("Arial", 12),
     command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

window.mainloop()