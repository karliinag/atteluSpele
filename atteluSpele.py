from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.geometry("375x480")
gameWindow.title("Vienādie attēli")
btn0=Button(width=12,height=10)
btn1=Button(width=12,height=10)
btn2=Button(width=12,height=10)
btn3=Button(width=12,height=10)
btn4=Button(width=12,height=10)
btn5=Button(width=12,height=10)
btn6=Button(width=12,height=10)
btn7=Button(width=12,height=10)
btn8=Button(width=12,height=10)
btn9=Button(width=12,height=10)
btn10=Button(width=12,height=10)
btn11=Button(width=12,height=10)

btn0.grid(row=1, column=0)
btn1.grid(row=2, column=0)
btn2.grid(row=3, column=0)
btn3.grid(row=1, column=1)
btn4.grid(row=2, column=1)
btn5.grid(row=3, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=2)
btn8.grid(row=3, column=2)
btn9.grid(row=1, column=3)
btn10.grid(row=2, column=3)
btn11.grid(row=3, column=3)

myimg1=ImageTk.PhotoImage(Image.open("at1.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("at2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("at3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("at4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("at5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("at6.png"))


gameWindow.mainloop()