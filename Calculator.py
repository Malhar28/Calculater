from tkinter import *
from pygame import mixer


root = Tk()
root.title('Calculator')
root.geometry("634x800")
root.wm_iconbitmap("calculater.ico")
# root.config(background="silver")


def clicked(event):
    mixer.init()
    mixer.music.load("click.mp3")
    mixer.music.play()


    global scval
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            value = eval(screen.get())

        scval.set(value)
        screen.update()

    elif text == "c":
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get() + text)
        screen.update()
    
    

scval = StringVar()
scval.set("")

screen = Entry(root, textvar=scval, font="comicsansms 40 bold")
screen.pack(fill=X, ipadx=10, pady=11, padx=10)


# ====================================================================================
frame1 = Frame(root, bg='light grey')
frame1.pack()

b1 = Button(frame1, text="9", padx=10, pady=10, font="lucida 33")
b1.pack(side=LEFT, padx=16, pady=7)
b1.bind("<Button-1>", clicked)

b2 = Button(frame1, text="8", padx=10, pady=10, font="lucida 33")
b2.pack(side=LEFT, padx=16, pady=7)
b2.bind("<Button-1>", clicked)

b3 = Button(frame1, text="7", padx=10, pady=10, font="lucida 33")
b3.pack(side=LEFT, padx=16, pady=7)
b3.bind("<Button-1>", clicked)
# ====================================================================================



# ====================================================================================
frame2 = Frame(root, bg='light grey')
frame2.pack()

b4 = Button(frame2, text="6", padx=10, pady=10, font="lucida 33")
b4.pack(side=LEFT, padx=16, pady=7)
b4.bind("<Button-1>", clicked)

b5 = Button(frame2, text="5", padx=10, pady=10, font="lucida 33")
b5.pack(side=LEFT, padx=16, pady=7)
b5.bind("<Button-1>", clicked)

b6 = Button(frame2, text="4", padx=10, pady=10, font="lucida 33")
b6.pack(side=LEFT, padx=16, pady=7)
b6.bind("<Button-1>", clicked)
# ====================================================================================




# ====================================================================================
frame3 = Frame(root, bg='light grey')
frame3.pack()

b7 = Button(frame3, text="3", padx=10, pady=10, font="lucida 33")
b7.pack(side=LEFT, padx=16, pady=7)
b7.bind("<Button-1>", clicked)

b8 = Button(frame3, text="2", padx=10, pady=10, font="lucida 33")
b8.pack(side=LEFT, padx=16, pady=7)
b8.bind("<Button-1>", clicked)

b9 = Button(frame3, text="1", padx=10, pady=10, font="lucida 33")
b9.pack(side=LEFT, padx=16, pady=7)
b9.bind("<Button-1>", clicked)
# ====================================================================================




# ====================================================================================
frame4 = Frame(root, bg='light grey')
frame4.pack()


b0 = Button(frame4, text="0", padx=123, pady=10, font="lucida 33")
b0.pack(side=LEFT, padx=16, pady=7)
b0.bind("<Button-1>", clicked)
# ====================================================================================





# ====================================================================================
frame5 = Frame(root, bg='light grey')
frame5.pack()

b10 = Button(frame5, text="+", padx=10, pady=10, font="lucida 33")
b10.pack(side=LEFT, padx=16, pady=7)
b10.bind("<Button-1>", clicked)

b11 = Button(frame5, text="-", padx=15, pady=10, font="lucida 33")
b11.pack(side=LEFT, padx=16.5, pady=7)
b11.bind("<Button-1>", clicked)

b12 = Button(frame5, text="*", padx=12, pady=10, font="lucida 33")
b12.pack(side=LEFT, padx=16, pady=7)
b12.bind("<Button-1>", clicked)
# ====================================================================================




# ====================================================================================
frame6 = Frame(root, bg='light grey')
frame6.pack()

b13 = Button(frame6, text="/", padx=15, pady=10, font="lucida 33")
b13.pack(side=LEFT, padx=16, pady=7)
b13.bind("<Button-1>", clicked)

b14 = Button(frame6, text="c", padx=11, pady=10, font="lucida 33")
b14.pack(side=LEFT, padx=16, pady=7)
b14.bind("<Button-1>", clicked)

b15 = Button(frame6, text="=", padx=10, pady=10, font="lucida 33")
b15.pack(side=LEFT, padx=16, pady=7)
b15.bind("<Button-1>", clicked)
# ====================================================================================




root.mainloop()


