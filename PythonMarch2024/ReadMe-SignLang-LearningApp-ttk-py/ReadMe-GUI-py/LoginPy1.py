from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from subprocess import call 

login=Tk()

def open():
    call(["python","SplashScreen.py"])  

def get_data(event=None): # Modified to accept an event argument
    username=usernameEntry.get()
    password=PasswordEntry.get() 
    if username=='' or password=='':
        print("Cant be Empty")
        messagebox.showerror("Login Error","Password or Username can't be Empty")
        return
    elif username=='PM' or password=='123' :
        print(username + " " + password)
        login.destroy()
        open()
    else:
        messagebox.showerror("Login Error","Password or Username is Incorrect")

login.geometry('990x660+200+10')
bgImage=ImageTk.PhotoImage(file='bglog.png')
bgLabel=Label(login,image=bgImage)
bgLabel.pack()
login.title('Login Page')

def on_enter(e):
    if usernameEntry.get() == 'Username':  # Check if the placeholder text is present
        usernameEntry.delete(0, END)  # Clear the placeholder text

def on_enter1(e):
    if PasswordEntry.get() == 'Password':  # Check if the placeholder text is present
        PasswordEntry.delete(0, END)  # Clear the placeholder text
        PasswordEntry.configure(show='*')  # Set show option to '*' for password entry

heading=Label(login,text='USER LOGIN',font=('Georgia',23,'bold'),bg='white',fg='green')
heading.place(x=124,y=120)
usernameEntry=Entry(login,width=25,font=('Times',13),bd=0,fg='#013220')
usernameEntry.place(x=124,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind("<FocusIn>",on_enter)

frame1=Frame(login, width=250,height=2,bg='green')
frame1.place(x=124,y=220)

PasswordEntry=Entry(login,width=25,font=('Times',13),bd=0,fg='#013220', show='')
PasswordEntry.place(x=124,y=260)
PasswordEntry.insert(0,'Password')
PasswordEntry.bind("<FocusIn>",on_enter1)
PasswordEntry.bind("<Return>", get_data)  # Bind the <Return> key to the get_data function for password entry

frame2=Frame(login, width=250,height=2,bg='green').place(x=124,y=282)

forgetbutton=Button(login,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',fg='green').place(x=270,y=295)

loginbutton=Button(login,text='Login',font=('open sans',16,'bold'),fg='white',bg='green',activeforeground='white',activebackground='green',cursor='hand2',bd=0,width=19, command=get_data)
loginbutton.place(x=124,y=360)
loginbutton.bind("<Return>", get_data) # Bind the <Return> key to the get_data function

orlabel=Label(login,text="--------------- OR -------------- ",font=('open sans',16),bg='white',fg='green').place(x=124,y=420)


facebook=PhotoImage(file='facebook.png')
fb=Label(login,image=facebook,bg='white').place(x=180,y=470)

google=PhotoImage(file='google.png')
fb=Label(login,image=google,bg='white').place(x=230,y=470)

twitter=PhotoImage(file='twitter.png')
fb=Label(login,image=twitter,bg='white').place(x=280,y=470)


dha=Label(login,text="Don't have an Account?",font=('open sans',9,'bold'),bg='white',fg='green').place(x=124,y=530)

dhabutton=Button(login,text='Create New One',font=('open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='white',activebackground='grey',cursor='hand2',bd=0).place(x=270,y=530)

login.mainloop()

