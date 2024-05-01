from tkvideo import tkvideo
from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
from tkinter import messagebox
import openpyxl

root = Tk()
root.geometry('990x660+200+10')
root.title('Login Page')
root.configure(background="black")

wrong = 0
correct = 1

def crt_ans():
    global correct
    correct = correct + 1
    feedback_label1.config(text="Correct!", foreground="green")
    print((f"the score is: {correct} !!"))

def wng_ans():
    global wrong
    wrong = wrong + 1
    feedback_label1.config(text="Wrong!", foreground="RED")
    print((f"the wrong is: {wrong} !!"))

def crt_ans1():
    global correct
    correct = correct + 1
    feedback_label2.config(text="Correct!", foreground="green")
    print((f"the score is: {correct} !!"))

def wng_ans1():
    global wrong
    wrong = wrong + 1
    feedback_label2.config(text="Wrong!", foreground="RED")
    print((f"the wrong is: {wrong} !!"))

def crt_ans2():
    global correct
    correct = correct + 1
    feedback_label3.config(text="Correct!", foreground="green")
    print((f"the score is: {correct} !!"))

def wng_ans2():
    global wrong
    wrong = wrong + 1
    feedback_label3.config(text="Wrong!", foreground="RED")
    print((f"the wrong is: {wrong} !!"))

def crt_ans3():
    global correct
    correct = correct + 1
    feedback_labe.config(text="Correct!", foreground="green")
    print((f"the score is: {correct} !!"))

def wng_ans3():
    global wrong
    wrong = wrong + 1
    feedback_labe.config(text="Wrong!", foreground="RED")
    print((f"the wrong is: {wrong} !!"))

def nxtpg():
    global count
    if not count > len(pages) - 2:
        for p in pages:
            p.pack_forget()
        count += 1
        page = pages[count]
        page.pack(pady=40)
    else:
        global wrong
        global correct
        total = wrong + correct
        score = correct
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(correct, total))
        workbook = openpyxl.load_workbook("data2.xlsx")
        sheet = workbook.active
        sheet.append([correct, wrong, total])
        workbook.save("data2.xlsx")
        print("hello")
        root.destroy()

btm_fm = Frame(root)
nxtbtn = tb.Button(btm_fm, text="NEXT", bootstyle="success outline", width=20, command=nxtpg)
nxtbtn.pack()
btm_fm.pack(side=tk.BOTTOM, pady=10)

main_frame = Frame(root)

pg1 = Frame(main_frame)
lbl1 = tk.Label(pg1, text="Are you ready to start your American Sign Language Journey?", font=("bold", 27)).pack()
lbl2 = tk.Label(pg1, text="Fasten your seatbelts, we are ready to take off!!", font=("bold", 26)).pack()
pg1.pack(pady=150)

pg2 = Frame(main_frame)
l1 = Label(pg2, text="Let's Learn:", font=("Helvetica", 16)).pack()
lbl2 = Label(pg2)
lbl2.pack()
player = tkvideo("hello2.mp4", lbl2, loop=1, size=(400, 300))
player.play()
style = tb.Style()
style.configure('success.TButton', font=('Helvetica', 18))
butt1 = tb.Button(pg2, text="HELLO", style="success.TButton", width=29).pack(pady=2)

pg3 = Frame(main_frame)
lbl4 = tk.Label(pg3, text="Choose the correct option:", font=("bold", 22)).pack()
lbl3 = Label(pg3)
lbl3.pack()
player = tkvideo("hello2.mp4", lbl3, loop=1, size=(400, 300))
player.play()
butt2 = tb.Button(pg3, text="HELLO", style="warning.TButton", width=29, command=crt_ans).pack(pady=10)
butt3 = tb.Button(pg3, text="CAP", style="warning.TButton", width=29, command=wng_ans).pack(pady=5)
feedback_label1 = tk.Label(pg3, font=("arial", 25, "bold"))
feedback_label1.pack(pady=15)

pg4 = Frame(main_frame)
l2 = Label(pg4, text="Let's Learn:", font=("Helvetica", 16)).pack()
lbl5 = Label(pg4)
lbl5.pack()
player = tkvideo("please2.mp4", lbl5, loop=1, size=(400, 300))
player.play()
style = tb.Style()
style.configure('success.TButton', font=('Helvetica', 18))
butt4 = tb.Button(pg4, text="PLEASE", style="success.TButton", width=29).pack(pady=2)

pg5 = Frame(main_frame)
lbl6 = tk.Label(pg5, text="Choose the correct option:", font=("bold", 22)).pack()
lbl7 = Label(pg5)
lbl7.pack()
player = tkvideo("please2.mp4", lbl7, loop=1, size=(400, 300))
player.play()
butt5 = tb.Button(pg5, text="HELLO", style="warning.TButton", width=29, command=wng_ans1).pack(pady=10)
butt6 = tb.Button(pg5, text="PLEASE", style="warning.TButton", width=29, command=crt_ans1).pack(pady=5)
feedback_label2 = tk.Label(pg5, text="", font=("arial", 25, "bold"))
feedback_label2.pack(pady=15)

pg7 = Frame(main_frame)
l3 = Label(pg7, text="Let's Learn:", font=("Helvetica", 16)).pack()
lbl8 = Label(pg7)
lbl8.pack()
player = tkvideo("me2.mp4", lbl8, loop=1, size=(400, 300))
player.play()
style = tb.Style()
style.configure('success.TButton', font=('Helvetica', 18))
butt7 = tb.Button(pg7, text="I / ME", style="success.TButton", width=29).pack(pady=2)

def click_bind(e):
    lol2.config(text=f"You Selected: {combo.get()}",fg="orange")
    if combo.get()=="ME":
        feedback_label4.config(text="Correct!", foreground="green")
    else:
        feedback_label4.config(text="Wrong!", foreground="red")

pg8 = Frame(main_frame)
lol = Label(pg8, text="Select From DropDown", font=("arial", 30), width=24).pack()
lbl8 = Label(pg8)
lbl8.pack()
player = tkvideo("me2.mp4", lbl8, loop=1, size=(400, 300))
player.play()

val = ["OPEN", "HELLO", "PLEASE", "ME", "YOU", "OK"]
combo = tb.Combobox(pg8, bootstyle="danger", values=val, width=35)
combo.pack(pady=19)
combo.current(0)
combo.bind("<<ComboboxSelected>>", click_bind)
lol2 = tk.Label(pg8, text="Your Selection Appears Here", font=("arial", 20), width=24)
lol2.pack(pady=17)

feedback_label4 = tk.Label(
    pg8,
    text="", font=("arial", 25, "bold"))
feedback_label4.pack()

pg9 = Frame(main_frame)
l4 = Label(pg9, text="Let's Learn:", font=("Helvetica", 16)).pack()
lbl9 = Label(pg9)
lbl9.pack()
player = tkvideo("fine2.mp4", lbl9, loop=1, size=(400, 300))
player.play()

style = tb.Style()
style.configure('success.TButton', font=('Helvetica', 18))
butt8 = tb.Button(pg9, text="FINE", style="success.TButton", width=29).pack(pady=2)

pg10 = Frame(main_frame)

lbl10 = tk.Label(pg10, text="Choose the correct option:", font=("bold", 22)).pack()
lbl11 = Label(pg10)
lbl11.pack()
player = tkvideo("fine2.mp4", lbl11, loop=1, size=(400, 300))
player.play()

butt9 = tb.Button(pg10, text="FINE", style="warning.TButton", width=29, command=crt_ans2).pack(pady=10)

butt10 = tb.Button(pg10, text="WELCOME", style="warning.TButton", width=29, command=wng_ans2).pack(pady=5)
feedback_label3 = tk.Label(
    pg10,
    text="", font=("arial", 25, "bold"))
feedback_label3.pack(pady=15)

feedback_label_drag = None

def check_drop(event):
    global feedback_label_drag  # Access the global variable
    dropped_label = event.widget
    if dropped_label.cget("text") == "FINE":
        feedback_label_drag.config(text="Correct!", foreground="green")
        crt_ans2()  # Update score for correct answer
    else:
        feedback_label_drag.config(text="Wrong!", foreground="red")
        wng_ans2()  # Update score for wrong answer

pg11 = Frame(main_frame)
lbl12a = tk.Label(pg11, text="Use Drag and Drop To", font=("bold", 19)).pack()
lbl12 = tk.Label(pg11, text="Complete The Following Sentence from scattered words:", font=("bold", 20)).pack()
lbl13 = Label(pg11)
lbl13.pack()
player = tkvideo("iamfine2.mp4", lbl13, loop=1, size=(400, 300))
player.play()

fm = Frame(pg11)
LL = tk.Label(fm, text="I Am...", font=("arial", 21), width=60, fg="#df3079")
LL.pack(pady=30)
fm.pack(pady=30)

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

label = Label(fm, text="FINE", font=("helvetica", 14))
label.place(x=20, y=20)

label2 = Label(fm, text="HAPPY", font=("helvetica",14))
label2.place(x=240, y=30)

label3 = Label(fm, text="BETTER", font=("helvetica", 14))
label3.place(x=380, y=60)

label4 = Label(fm, text="NICE", font=("helvetica", 14))
label4.place(x=830, y=50)

label5 = Label(fm, text="GOOD", font=("helvetica", 14))
label5.place(x=130, y=140)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
label.bind("<ButtonRelease-1>", check_drop)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)
label2.bind("<ButtonRelease-1>", check_drop)

label3.bind("<Button-1>", drag_start)
label3.bind("<B1-Motion>", drag_motion)
label3.bind("<ButtonRelease-1>", check_drop)

label4.bind("<Button-1>", drag_start)
label4.bind("<B1-Motion>", drag_motion)
label4.bind("<ButtonRelease-1>", check_drop)

label5.bind("<Button-1>", drag_start)
label5.bind("<B1-Motion>", drag_motion)
label5.bind("<ButtonRelease-1>", check_drop)

pg12 = Frame(main_frame)
l5 = Label(pg12, text="Let's Learn:", font=("Helvetica", 16)).pack()
lbl14 = Label(pg12)
lbl14.pack()
player = tkvideo("help2.mp4", lbl14, loop=1, size=(400, 300))
player.play()

style = tb.Style()
style.configure('success.TButton', font=('Helvetica', 18))
butt11 = tb.Button(pg12, text="HELP", style="success.TButton", width=29).pack(pady=2)

pg6 = Frame(main_frame)

lbl41 = tk.Label(pg6, text="Choose the correct option:", font=("bold", 22)).pack()
lbl31 = Label(pg6)
lbl31.pack()
player = tkvideo("help2.mp4", lbl31, loop=1, size=(400, 300))
player.play()

butt10 = tb.Button(pg6, text="I AM FINE", style="warning.TButton", width=29, command=wng_ans3).pack(pady=10)

butt11 = tb.Button(pg6, text="HELP", style="warning.TButton", width=29, command=crt_ans3).pack(pady=5)

feedback_labe = tk.Label(pg6, text="", font=("arial", 25, "bold"))
feedback_labe.pack(pady=13)

main_frame.pack(fill=tk.BOTH, expand=True)

pages = [pg1, pg2, pg3, pg4, pg5, pg7, pg8, pg9, pg10, pg11, pg12, pg6]
count = 0

root.mainloop()
