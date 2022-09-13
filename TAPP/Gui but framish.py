from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import hashlib

#cancel/verify functions
def validateLogin(user, password):
    print("Usuario:", user.get())
    print("Contrasena:", password.get())
    return
    
def cancel():
    window.destroy()
    
    
#variable
clave_valida = "12345"


#window creation with Tk()
window = Tk()
window.geometry("900x400")
window.resizable(False, False)
window.config(bg = 'white')
window.title('ITVER Login Page')

#Title Frame Creation
frame_one = Frame(window)  
frame_one.pack()
frame_one.config(bg = "#262a94")
frame_one.config(width= 900, height= 150)


#Creating an ImageTk object
image = (Image.open(r"C:\Users\chato\OneDrive\Documentos\ITVER\teclogo.jpg"))
resz_img = image.resize((150, 150), Image.Resampling.LANCZOS)
new_img = ImageTk.PhotoImage(resz_img)  

#Labeling the image into the frame
img = Label(frame_one, image = new_img)
img.place(x= 0, y =0)

#Text Label
text_label = Label(frame_one, text="Instituto Tecnologico de Veracruz")
text_label.config(fg='white', bg='#262a94', font=('Verdana', 30))
text_label.place(x=190, y = 35)

#Login credentials frame creation
frame_two = Frame(window)
frame_two.config(width= 900, height=450)
frame_two.config(bg = 'white')
frame_two.pack()



#User/Password entry
usernameLabel = Label(frame_two, text = "Usuario", font = 70, bg='white').grid(row = 1, column = 0, pady = 20)
user = StringVar()
usernameEntry = Entry(frame_two, textvariable = user).grid(row = 1, column = 1)

passwordLabel = Label(frame_two, text = "Contraseña", font = 70, bg = 'white').grid(row = 2, column = 0, pady = 20)
password = StringVar()
passwordEntry = Entry(frame_two, textvariable = password, show = "*").grid(row = 2, column = 1)

#Checkboxes
captcha = ttk.Checkbutton(frame_two, text = "No soy un robot", onvalue=1, offvalue=0).grid(row = 3, column = 1)
verify = ttk.Checkbutton(frame_two, text = "Soy estudiante", onvalue=1, offvalue=0).grid(row = 4, column = 1)

#Validar
validateLogin = partial(validateLogin, user, password)

#Boton Login
login = Button(frame_two, text = "Entrar", command = validateLogin).grid(row = 5, column = 1, pady = 20)
cancel = Button(frame_two, text = "Cancel", command= cancel).grid(row = 5, column = 0, pady = 20)

#window summoning
window.mainloop()