from cgitb import reset
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("atteluSpele")
gameWindow.configure(bg="black")


myimg1=ImageTk.PhotoImage(Image.open("at1.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("at2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("at3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("at4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("at5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("at6.png"))

ImageList=[myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,myimg5,myimg5,myimg6,myimg6]

bgImg=ImageTk.PhotoImage(Image.open("bat.jpg"))

btn0=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn0,0))
btn1=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn1,1))
btn2=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn2,2))
btn3=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn3,3))
btn4=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn4,4))
btn5=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn5,5))
btn6=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn6,6))
btn7=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn7,7))
btn8=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn8,8))
btn9=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn9,9))
btn10=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn10,10))
btn11=Button(width=12,height=10,image=bgImg,command=lambda:btnClick(btn11,11))

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

random.shuffle(ImageList)

count=0
correctAnswer=0
Answer=[]
Answer_dict={}
Answercount=0

def reset():
    global count,correctAnswer, Answer, Answer_dict, Answercount
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)

    btn0["Image"]="pyimage5"
    btn1["Image"]="pyimage5"
    btn2["Image"]="pyimage5"
    btn3["Image"]="pyimage5"
    btn4["Image"]="pyimage5"
    btn5["Image"]="pyimage5"

    random.shuffle(ImageList)

    count=0
    correctAnswer=0
    Answer=[]
    Answer_dict={}
    Answercount=0       

def infoLogs():
  gameWindow=Toplevel()
  gameWindow.title("Info par programmu")
  gameWindow.geometry("500x300")
  apraksts=Label(gameWindow,text="Tev ir jāatmin divas vienādas kartiņas")  
  apraksts.grid(row=0, column=0)
  return 0

def btnClick(btn,number):
    global count, correctAnswer, Answer, Answer_dict
    if btn["bat.jpg"]=="pyimage6" and count<2:
        btn["bat.jpg"]=ImageList[number]
    count+=1
    Answer.append(number)
    Answer_dict[btn]=ImageList[number]
    if len(Answer)==2:
        if ImageList[Answer[0]]==ImageList[Answer[1]]:
            for key in Answer_dict:
                key["state"]=DISABLED
            correctAnswer+=2
            if(correctAnswer==2):
                 messagebox.showinfo("Vienādi attēli, uzminēji")
                 correctAnswer=0
            if(correctAnswer==6):
                messagebox.askquestion("Vienādi attēli","Tu uzvarēji, vēlies spēlēt vēlreiz?")
        else:
            messagebox.showinfo("Vienādi attēli.","neuzminēji")
            for key in Answer_dict:
                key["Image"]=="pyiimage6"
    
        count=0
        Answer=[]
        Answer_dict={}

        return 0
 

galvenaIzvele=Menu(gameWindow)
gameWindow.config(menu=galvenaIzvele)

opcijas=Menu(galvenaIzvele, tearoff=False)
galvenaIzvele.add_cascade(label="Opcijas", menu=opcijas)
opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet",command=gameWindow.quit)
galvenaIzvele.add_command(label="Par programmu",command=infoLogs)
gameWindow.mainloop()
