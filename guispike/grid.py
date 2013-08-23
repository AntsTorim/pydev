'''
Created on 30.07.2013

@author: Ants Torim
'''
from tkinter import *
from tkinter import ttk



if __name__ == '__main__':
    #Initialize widget tree
    root = Tk()
    content=ttk.Frame(root)
    frame=ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=200)
    namelbl = ttk.Label(content, text="Johann Gambolputty von Ausfernen of Ulm")
    name=ttk.Entry(content)
    #Initialize buttons
    onevar = BooleanVar()
    twovar = BooleanVar()
    threevar = BooleanVar()
    onevar.set(True)
    twovar.set(False)
    threevar.set(True)
    one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
    two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
    three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
    ok = ttk.Button(content, text="Okay")
    cancel = ttk.Button(content, text="Cancel")
    #Set geometry
    content.grid(column=0, row=0)
    frame.grid(column=0, row=0, columnspan=3, rowspan=2)
    namelbl.grid(column=3, row=0, columnspan=2)
    name.grid(column=3, row=1, columnspan=2, sticky="w")
    one.grid(column=0, row=3)
    two.grid(column=1, row=3)
    three.grid(column=2, row=3)
    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)
    root.mainloop()
    
    