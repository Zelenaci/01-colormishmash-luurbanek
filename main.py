#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import ( Label, Button, Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, S, StringVar, )

# from tkinter import ttk


"""class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()
        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()
    def close(self):
        self.destroy() """ # trida About pro viceoknove aplikace


class Application(tk.Tk): #dědí z tk.Tk
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self): #self - trida odkazuje sama na sebe
        super().__init__(className=self.name) # z tridy vytvorime objekr = spusti se __init_ #funkce super vraci predka
        self.title(self.name)

        self.bind("<Escape>", self.quit) #= kdyz zmacknu esc tak ukonci

        ###  R
        self.varR = StringVar()
        self.varR.trace("w",self)
        self.frameR = Frame(self)
        self.frameR.pack()
        self.lblR = Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor=S) #umisteni widgetu do programu
        self.scaleR = Scale (self.frameR, 
            from_=0, to=255, orient=HORIZONTAL,length=256, variable=self.varR, command=self.change,
        )
        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)

        ###  G
        self.varG = StringVar()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.lblG = Label(self.frameG, text="G")
        self.lblG.pack(side=LEFT, anchor=S) #umisteni widgetu do programu
        self.scaleG = Scale (self.frameG, 
            from_=0, to=255, orient=HORIZONTAL,length=256, variable=self.varG, command=self.change,
        )
        self.scaleG.pack(side=LEFT, anchor=S)
        self.entryG = Entry(self.frameG, width=5, textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)


        ###  B
        self.varB = StringVar()
        self.frameB = Frame(self)
        self.frameB.pack()
        self.lblB = Label(self.frameB, text="B")
        self.lblB.pack(side=LEFT, anchor=S) #umisteni widgetu do programu
        self.scaleB = Scale (self.frameB, 
            from_=0, to=255, orient=HORIZONTAL,length=256, variable=self.varB, command=self.change,
        )
        self.scaleB.pack(side=LEFT, anchor=S)
        self.entryB = Entry(self.frameB, width=5, textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)


        self.canvasMain = Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.quit)
        self.btn2.pack()

    """def about(self):
        window = About(self)
        window.grab_set()"""

    def change(self, event):
        #self.lblG.config(text="changeconfigtext")

        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorstring = f"#{r:02X}{g:02X}{b:02X}"
        self.canvasMain.config(background=colorstring)
        print(colorstring)
        #print(f"#{r:2x}{g:2x}{b:2x}")
        #print(f"#{r:02x}{g:02x}{b:02x}")

        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
