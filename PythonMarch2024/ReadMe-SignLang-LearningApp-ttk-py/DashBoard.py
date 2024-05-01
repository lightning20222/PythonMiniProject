from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from subprocess import call
import webbrowser

root=Tk()
root.title("ReadMe DashBoard")
root.geometry("990x618+200+10")

'''
def open2():
    call(["python","LivePratice.py"])
'''
def open2():
    html_file_path = "D:/PythonMarch2024/ReadMe-SignLang-LearningApp-ttk-py/Sign-Language-Translator-newclassifier/index.html"
    webbrowser.open(html_file_path)

def open3():
    call(["python","Learn4.py"])

def open4():
    call(["python","Report.py"])


# hex for dash img colour #efddcd
# ......................................................................................
img=PhotoImage(file="DashImg.png")
lbl=Label(root,image=img)
lbl.place(x=0,y=0,relwidth=1,relheight=1)

# txt=tb.Label(root,text="WELCOME!!",font=("Helvetica",50),bootstyle="danger")
# txt.pack(pady=20)
btn1=tb.Button(root,text="Live Pratice !!",bootstyle="danger outline",width=20,command=open2)
btn1.place(x=180,y=520)

btn2=tb.Button(root,text="Learn !!",bootstyle="danger outline",width=20,command=open3)
btn2.place(x=410,y=520)

btn3=tb.Button(root,text="Report !!",bootstyle="danger outline",width=20,command=open4)
btn3.place(x=630,y=520)

# .............................................................................................
root.mainloop()

