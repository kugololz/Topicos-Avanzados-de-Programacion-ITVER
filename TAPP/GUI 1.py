from tkinter import ttk
from tkinter import *

#Window
window = Tk()
window.geometry('1920x1080')

#Titulo
titulo = Label(window, text = "Instituto Tecnologico de Veracruz", font=("Comic Sans",40))  .grid(row = 0, column=2)

#Usuario
usernameLabel = Label(window, text="Usuario", font=40).grid(row=1, column=0)
username = StringVar()
userEntry = Entry(window, textvariable="username").grid(row= 1, column = 1)

#Contrasena

passwordLabel = Label(window, text = 'Contraseña', font=40).grid(row = 2, column = 0)
password = StringVar()
passwordEntry = Entry(window, textvariable="password").grid(row = 2, column = 1)

#Checkbox
captcha = ttk.Checkbutton(window, text="No soy un robot").grid(row = 3, column = 0)
alumno = ttk.Checkbutton(window, text= "Soy Alumno" ).grid(row=4, column=0)

f = Frame()

#Boton Login
loginButton = Button(window, text="Entrar").grid(row=5, column=3)  

window.state('zoomed')
window.mainloop()