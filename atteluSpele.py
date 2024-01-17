from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

def resize_image(img_path, target_size):
    original_image = Image.open(img_path)
    resized_image = original_image.resize(target_size)
    return ImageTk.PhotoImage(resized_image)

def reset_cards():
    for btn in buttons:
        btn.config(image=bgImg, state=NORMAL)
    global count, pairs_found, images
    random.shuffle(images)
    count = 0
    pairs_found = 0

def btnClick(btn, number):
    global count, prev_btn, prev_number, pairs_found
    if btn["state"] == NORMAL and count < 2:
        btn.config(image=images[number])
        count += 1
        if count == 1:
            prev_btn = btn
            prev_number = number
        elif count == 2:
            btn.after(1000, lambda: check_match(btn, prev_btn, number, prev_number))

def check_match(btn1, btn2, num1, num2):
    global count, pairs_found
    if images[num1] == images[num2]:
        btn1.config(state=DISABLED)
        btn2.config(state=DISABLED)
        pairs_found += 1
        if pairs_found == len(images) // 2:
            messagebox.showinfo("Apsveicu,Tu uzvarēji!")
            reset_cards()
    else:
        btn1.config(image=bgImg)
        btn2.config(image=bgImg)
    count = 0

gameWindow = Tk()
gameWindow.title("Memory Game")
gameWindow.configure(bg="black")

bgImg = resize_image("bat.jpg", (200, 300))

myimg1 = resize_image("at1.jpg", (200, 300))
myimg2 = resize_image("at2.jpg", (200, 300))
myimg3 = resize_image("at3.jpg", (200, 300))
myimg4 = resize_image("at4.jpg", (200, 300))
myimg5 = resize_image("at5.jpg", (200, 300))
myimg6 = resize_image("at6.png", (200, 300))

images = [myimg1, myimg2, myimg3, myimg4, myimg5, myimg6, myimg1, myimg2, myimg3, myimg4, myimg5, myimg6]
random.shuffle(images)

buttons = []
for i in range(len(images)):
    button = Button(width=200, height=300, image=bgImg, command=lambda i=i: btnClick(buttons[i], i))
    button.grid(row=i // 4, column=i % 4)
    buttons.append(button)

count = 0
pairs_found = 0
prev_btn = None
prev_number = None

menuBar = Menu(gameWindow)
gameWindow.config(menu=menuBar)

optionsMenu = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Ocijas", menu=optionsMenu)
optionsMenu.add_command(label="Jauna spēle", command=reset_cards)
optionsMenu.add_command(label="Iziet", command=gameWindow.quit)

infoMenu = Menu(menuBar, tearoff=False)
menuBar.add_command(label="Kā spēlēt?", command=lambda: messagebox.showinfo("Atmiņas spēle", "Atrodi un uzklikšķini uz vienādajiem attēliem"))

gameWindow.mainloop()




