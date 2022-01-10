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
        self.protocol("WM_DELETE_WINDOW", self.quit)

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

        for row in range(10):
            for column in range(10):
                canvas = Canvas(self.frameMem, width=50, height=50, background="#000000") #vytvorim canvas
                canvas.grid(row=row, column=column) #pridam ho do mrizky
                canvas.bind("<Button-1>", self.mousehandler)
                self.canvasMem.append(canvas)

    def mousehandler(self, event):
        # print(dir(event))
        if self.cget("cursor") != "pencil": #kliknu poprve
            self.config(cursor="pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor") == "pencil": # druhy klik
            self.config(cursor="")
            event.widget.config(background=self.color)

            if event.widget is self.canvasMain:
                self.canvasColor2Slides(self.canvasMain)

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

    def canvasColor2Slides(self, canvas):
        color = canvas.cget("background") #ziskam barvu cget
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:], 16)  # ,16 = sestnactkova soustava
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)
        self.change()

    def colorSave(self):
        with open("colors.txt", "w") as f:
            f.write(self.canvasMain.cget("background")+ "\n") #cget config get ... get background
            for canvas in self.canvasMem:
                f.write(canvas.cget("background") + "\n")

    def colorLoad(self):
        if exists ("colors.txt"):
            with open("colors.txt", "r") as f:
                colorcode = f.readline().strip() #strip odstrani konec radku
                self.canvasMain.config(background=colorcode)
                    canvas.config(background=colorcode)
        else:
            print("nepodarilo se nacist soubor")

    def quit(self, event=None):
        self.colorSave()
        super().quit() #super ukazuje na predka ktereho ma pak quit zavolat


app = Application()
app.mainloop()
