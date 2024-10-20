from tkinter import*
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="1234":
       screen2=Toplevel(screen)
       screen2.title("decryption")
       screen2.geometry('400x200')
       screen2.config(bg="#00bd56")

       message=Text1.get(1.0,END)
       decode_message=message.encode('ascii')
       base64_bytes=base64.b64decode(decode_message)
       encrypt=base64_bytes.decode('ascii')

       Label(screen2,text="decrypt",font="arail",fg="white",bg="#00bd56").place(x=10,y=0)
       Text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       Text2.place(x=10,y=40,width=380,height=150)

       Text2.insert(END,encrypt)

    elif password=="":     
        messagebox.showerror("encryption","input password")

    elif password !="1234":
        messagebox.showerror("encryption","invalid password")
         

def encrypt():
    password=code.get()

    if password=="1234":
       screen1=Toplevel(screen)
       screen1.title("encryption")
       screen1.geometry('400x200')
       screen1.config(bg="#ed3833")

       message=Text1.get(1.0,END)
       encode_message=message.encode('ascii')
       base64_bytes=base64.b64encode(encode_message)
       encrypt=base64_bytes.decode('ascii')

       Label(screen1,text="encrypt",font="arail",fg="white",bg="#ed3833").place(x=10,y=0)
       Text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       Text2.place(x=10,y=40,width=380,height=150)

       Text2.insert(END,encrypt)

    elif password=="":     
        messagebox.showerror("encryption","input password")

    elif password !="1234":
        messagebox.showerror("encryption","invalid password")

    



def main_screen():
    global screen
    global code
    global Text1

    screen=Tk()
    screen.geometry("375x398")

    #Icon
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    screen.title("pct app")
    def reset():
        code.set("")
        Text1.delete(1.0,END)


    Label(text="enter text for encryption and decryption",fg='black',font=("calbri",13)).place(x=10,y=10)
    Text1=Text(font="Robote 20",bg='white',relief=GROOVE,wrap=WORD,bd=0)
    Text1.place(x=10,y=50,width=355,height=100)

    Label(text="enter secret key for encryption and decryption",fg='black',font=("calbri",13)).place(x=15,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=('arial',25),show="*").place(x=10,y=200)

    Button(text="encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="decryt",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="reset",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)


    
    

    screen.mainloop()

main_screen()   