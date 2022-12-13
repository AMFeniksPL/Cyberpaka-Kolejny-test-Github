from tkinter import *

window = Tk()
window.minsize(640, 480)
window.minsize(640, 480)
window.geometry("640x480")

photo = PhotoImage(file="Zrzut ekranu 2022-12-11 193101.png")

mainFrame = Label(window,
                  text="Moja pierwsza gra (od dawna)",
                  font = ("Arial", 28),
                  bd=10,
                  bg="black",
                  fg="white",
                  image=photo,
                  compound="top")

mainFrame.pack()

window.mainloop()