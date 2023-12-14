import tkinter
from PIL import Image, ImageTk
import random

# step 2
# Building Main Window of application
root = tkinter.Tk()
root.geometry('400x400')
root.title("Roll the Dice")
root.configure(bg="white")

# step 3
# Adding label Into Frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and format
l1 = tkinter.Label(root, text="Let's Play!!", fg="black", bg="white", font="Helvetica 16 bold italic")
l1.pack()

# step 4
# images
Dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between 0 to 6 and generating image
image2 = ImageTk.PhotoImage(file='dice.png')

# construct a label with label widget for Image
label1 = tkinter.Label(root, image=image2)
label1.image = image2

# packing a widget in the parent widget
label1.pack(expand = True)

# step 5
# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))

    # update image
    label1.configure(image=image1, bg="white")

    # keep a referance
    label1.image = image1

    # adding button and command will use rolling dice function

button = tkinter.Button(root, text="Roll the Dice", font=('Arial,12,bold'), width=20, height=2, bg="red", fg='white',
                            command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

root.mainloop()