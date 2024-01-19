#pieslēdz visas nepieciešamās bibliotēkas
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

def izmeri(sakum_img, beigu_img):#funkcija, lai mainītu attēlu izmēru.
    org_img = Image.open(sakum_img)
    rez_img= org_img.resize(beigu_img)
    return ImageTk.PhotoImage(rez_img)

def apgriezt():#funkcija, lai apgrieztu kārtis, ja netiek uzminēts pāris
    for btn in buttons:
        btn.config(image=bgImg, state=NORMAL)#izveido pogas normālo stāvokli, kā apgrieztu ar background img
    global count, pari, images#mainīgie
    random.shuffle(images)
    count = 0#mainīgā vērtība ir 0
    pari = 0#mainīgā vērtība ir 0

def btnClick(btn, number):#Funkcija btnclick
    global count, pogas, cipari, pari#mainīgie
    if btn["state"] == NORMAL and count < 2:#pārbauda vai poga ir apgriezta un nodrošina, lai nevar uzspiest vairāk par 2 pogām vienā gājienā
        btn.config(image=images[number])#ja IF noteikumi izpildīti pogai ļauj apgriezties
        count += 1#skaita klikšķus
        if count == 1:#IF, kas sagatavo pogu salīdzināšanai ar otru pogu
            pogas = btn
            cipari = number
        elif count == 2:
            btn.after(1000, lambda: parbaude(btn, pogas, number, cipari))#uztaisa pauzi

def parbaude(btn1, btn2, num1, num2):#funkcija parbaude
    global count, pari#mainīgie
    if images[num1] == images[num2]:#salīdzina vai abas bildes sakrīt
        btn1.config(state=DISABLED)#izslēdz pogu 1, ja 1 un 2 poga sakrīt
        btn2.config(state=DISABLED)#izslēdz pogu 2, ja 1 un 2 poga sakrīt
        pari += 1# seko cik pāri ir salikti
        if pari == len(images) // 2:#ja pari ir vienādi pusei no pogām, spēle beidzas un parādas paziņojums
            messagebox.showinfo("Apsveicu", "Tu uzvarēji!")#uzvaras paziņojums
            apgriezt()#apgriež kārtis sākuma pozīcijā
    else:
        btn1.config(image=bgImg)#ja nesakrīt, apgriež atpakaļ
        btn2.config(image=bgImg)#ja nesakrīt, apgriež atpakaļ
    count = 0# atstāj 0, lai varētu veidot jaunus pārus

gameWindow = Tk()
gameWindow.title("Atminu_spele")#spēles nosaukums
gameWindow.configure(bg="black")#spēles background melns

bgImg = izmeri("bat.jpg", (200, 300))#background izmērs

#attēlu izmēri
myimg1 = izmeri("at1.jpg", (200, 300))
myimg2 = izmeri("at2.jpg", (200, 300))
myimg3 = izmeri("at3.jpg", (200, 300))
myimg4 = izmeri("at4.jpg", (200, 300))
myimg5 = izmeri("at5.jpg", (200, 300))
myimg6 = izmeri("at6.png", (200, 300))

images = [myimg1, myimg2, myimg3, myimg4, myimg5, myimg6, myimg1, myimg2, myimg3, myimg4, myimg5, myimg6]# izveido images sarakstu
random.shuffle(images)#samaisa attēlu atrašanās vietas kārtību

#pogu atrašanās veidota ar for loop
buttons = []
for i in range(len(images)):# i ir mainīgais 
    button = Button(width=200, height=300, image=bgImg, command=lambda i=i: btnClick(buttons[i], i))
    button.grid(row=i // 4, column=i % 4)
    buttons.append(button)

count = 0
pari = 0
pogas = None
cipari = None

spele_menu = Menu(gameWindow)#izveido izvelni
gameWindow.config(menu=spele_menu)

opcijas_Logs = Menu(spele_menu, tearoff=False)
spele_menu.add_cascade(label="Ocijas", menu=opcijas_Logs)
opcijas_Logs.add_command(label="Jauna spēle", command=apgriezt)#dodas uz funkciju apgriezt
opcijas_Logs.add_command(label="Iziet", command=gameWindow.quit)#aizver spēli

#izveido vēlvienu logu priekš spēles noteikumiem
info_Logs = Menu(spele_menu, tearoff=False)
spele_menu.add_command(label="Kā spēlēt?", command=lambda: messagebox.showinfo("Atmiņas spēle", "Atrodi un uzklikšķini uz vienādajiem attēliem"))

gameWindow.mainloop()#noslēdz tkinter loop





