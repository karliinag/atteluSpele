from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox



count=0
correctAnswer=0
Answer=[]
Answer_dict={}

def btnClick(btn,number):
    global count, correctAnswer, Answer, Answer_dict
    if btn["bat.jpg"]=="pyimage6" and count<2:
     btn["bat.jpg"]=imageList[number]
     count+=1
        Answer.append(number)
        Answer_dict[btn]=imageList(number)

    else:
        messagebox.showinfo("Vienādi attēli, neuzminēji")
        for key in Answer_dict:
            key["image"]="pyimage6"
count=0
Answer=[]
Answer_dict={}

return 0

myimg1=ImageTk.PhotoImage(Image.open("at1.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("at2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("at3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("at4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("at5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("at6.png"))

bgImg=ImageTk.PhotoImage(Image.open("bat.jpg"))


gameWindow=Tk()
gameWindow.geometry("375x480")
gameWindow.title("Vienādie attēli")
btn0=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn1,0))
btn1=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn2,1))
btn2=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn3,2))
btn3=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn4,3))
btn4=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn5,4))
btn5=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn6,5))
btn6=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn7,6))
btn7=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn8,7))
btn8=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn9,8))
btn9=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn10,9))
btn10=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn11,10))
btn11=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn1,11))

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







ImageList
gameWindow.mainloop()
