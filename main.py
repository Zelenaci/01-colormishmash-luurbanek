#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import (Label, Button, Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, S, StringVar, IntVar)

# from tkinter import ttk

class Application(tk.Tk):  # dědí z tk.Tk
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):  # self - trida odkazuje sama na sebe
        super().__init__(className=self.name)  # z tridy vytvorime objekr = spusti se __init_ #funkce super vraci predka
        self.title(self.name)

        self.bind("<Escape>", self.quit)  # = kdyz zmacknu esc tak ukonci

        ###  R
        self.varR = IntVar()
        self.frameR = Frame(self)
        self.frameR.pack()
        self.lblR = Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor=S)  # umisteni widgetu do programu
        self.scaleR = Scale(
            self.frameR,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=256,
            variable=self.varR,
        )
        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)

        ###  G
        self.varG = IntVar()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.lblG = Label(self.frameG, text="G")
        self.lblG.pack(side=LEFT, anchor=S)  # umisteni widgetu do programu
        self.scaleG = Scale(
            self.frameG,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=256,
            variable=self.varG,
        )
        self.scaleG.pack(side=LEFT, anchor=S)
        self.entryG = Entry(self.frameG, width=5, textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)

        ###  B
        self.varB = IntVar()
        self.frameB = Frame(self)
        self.frameB.pack()
        self.lblB = Label(self.frameB, text="B")
        self.lblB.pack(side=LEFT, anchor=S)  # umisteni widgetu do programu
        self.scaleB = Scale(self.frameB,
                            from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varB,
                            )
        self.scaleB.pack(side=LEFT, anchor=S)
        self.entryB = Entry(self.frameB, width=5, textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)



        self.canvasMain = Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>", self.mousehandler)

        self.varMain = StringVar()
        self.entryMain = Entry(
            self,
            textvariable=self.varMain,
            state="readonly",
            readonlybackground="#ffffff",
        )
        self.entryMain.pack()

        self.btnQ = Button(self, text="Quit", command=self.quit)

        self.varR.trace("w", self.change)
        self.varG.trace("w", self.change)
        self.varB.trace("w", self.change)

        self.frameMem = Frame(self)
        self.frameMem.pack()
        self.canvasMem = []

        for row in range(3):
            for column in range(7):
                canvas = Canvas(self.frameMem, width=50, height=50, background="#FFFFFF")
                canvas.grid(row=row, column=column)
                canvas.bind("<Button-1>", self.mousehandler)
                self.canvasMem.append(canvas)

    def mousehandler(self, event):
        # print(dir(event))
        if self.cget("cursor") != "pencil":
            self.config(cursor="pencil")
            self.color = event.widget.cget("background")

        elif self.cget("cursor") == "pencil":
            self.config(cursor="")
            event.widget.config(background=self.color)

    def change(self, var, index, mode):

        r = int(self.varR.get())
        g = int(self.varG.get())
        b = int(self.varB.get())
        colorstring = f"#{r:02X}{g:02X}{b:02X}"
        self.canvasMain.config(background=colorstring)
        self.varMain.set(colorstring)

        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
