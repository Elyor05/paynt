from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageDraw
from random import *


def point(event):
    x1, y1 = (event.x - 12), (event.y - 12)
    x2, y2 = (event.x + 12), (event.y + 12)
    cv.create_line(x1, y1, x2, y2, fill='black', activefill='yellow', width=5)
    draw.line([x1, y1, x2, y2], fill='black', width=5)


okno = Tk()
okno.title("Paint")
okno.geometry("1280x720")
okno.iconbitmap("paint-board-and-brush.ico")
okno.resizable(width=False, height=False)
okno["background"] = "black"

cv = Canvas(okno, width=1280, height=720, background="white")

img_1 = PIL.Image.new("RGB", (1280, 720), "white")
draw = ImageDraw.Draw(img_1)

cv.bind('<B1-Motion>', point)
cv.pack(expand=1, fill=BOTH)


def save():
    filename = f'image_{randint(0, 100000)}.png'
    img_1.save(filename)
    messagebox.showinfo("Saved image", "Молодец",)
    messagebox.showwarning(message='crash')


save_button = Button(text="Save", bg="black", fg="white", font=("Comic Sans MS", 20), command=save)
save_button.place(relx=0.5, rely=0.9)

okno.mainloop()
