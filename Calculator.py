from tkinter import *

def buttonPress(num):
    global equation_text
    equation_text=equation_text + str(num)
    equation_label.set(equation_text)

def equalsTo():
    global equation_text
    x=str(eval(equation_text))
    equation_label.set(x)
    equation_text=x


def clearText():
    global equation_text
    equation_label.set("")
    equation_text=""

root=Tk()

equation_text=""
equation_label=StringVar()

root.geometry("400x500")
root.title("__Calculator__")

label=Label(root,
            textvariable=equation_label,
            height=2,
            bg='white',
            width=23
            ,font=("Arial",20))
label.pack(side=TOP,pady=10)

frame=Frame(root)
frame.pack()

button1=Button(frame,
               text="1",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(1),
                border=4)
button1.grid(row=0,column=0)


button2=Button(frame,
               text="2",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(2),
                border=4)
button2.grid(row=0,column=1)


button3=Button(frame,
               text="3",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(3),
                border=4)
button3.grid(row=0,column=2)


button4=Button(frame,
               text="4",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(4),
                border=4)
button4.grid(row=2,column=0)


button5=Button(frame,
               text="5",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(5),
                border=4)
button5.grid(row=2,column=1)


button6=Button(frame,
               text="6",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(6),
                border=4)
button6.grid(row=2,column=2)


button7=Button(frame,
               text="7",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(7),
                border=4)
button7.grid(row=3,column=0)


button8=Button(frame,
               text="8",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(8),
                border=4)
button8.grid(row=3,column=1)


button9=Button(frame,
               text="9",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(9),
                border=4)
button9.grid(row=3,column=2)


button10=Button(frame,
               text="0",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(0),
                border=4)
button10.grid(row=4,column=1)



ac_button=Button(frame,
               text="AC",
               font=("Arial",24),
               width=3,
               command=clearText,
               border=4)
ac_button.grid(row=4,column=0)


plus=Button(frame,
               text="+",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('+'),
                border=4)
plus.grid(row=0,column=3)


minus=Button(frame,
               text="-",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('-'),
                border=4)
minus.grid(row=2,column=3)

multiply=Button(frame,
               text="x",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('*'),
                border=4)
multiply.grid(row=3,column=3)


divide=Button(frame,
               text="/",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('/'),
                border=4)
divide.grid(row=4,column=3)

point=Button(frame,
               text=".",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('.'),
                border=4)
point.grid(row=4,column=2)


bracket_button1=Button(frame,
               text="(",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress('('),
                border=4)
bracket_button1.grid(row=5,column=0)

bracket_button2=Button(frame,
               text=")",
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress(')'),
                border=4)
bracket_button2.grid(row=5,column=1)


equals_button = Button(frame,
                        text="=",
                        font=("Arial",24),
                        width=3,
                        command=equalsTo,
                        border=5)
equals_button.grid(row=5,column=3)

power = Button(frame,
               text="**", 
               font=("Arial",24),
               width=3,
               command=lambda: buttonPress("**"),
               border=5)
power.grid(row=5,column=2)


root.mainloop()