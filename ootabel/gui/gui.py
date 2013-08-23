'''
Created on 05.08.2013

@author: Ants Torim
'''
from tkinter import *
from tkinter import ttk
from tabel import Tabel

class Presenter:
    
    def build(self, n, m):
        self.root = Tk()
        self.root.option_add('*tearOff', False) #Menyy normaalne v2ljan2gemine
        menubar = Menu(self.root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Hello!", command=self.menuClick)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.configure(menu=menubar)
        self.root.title("Tabeli nullide sagedus")
        self.tabel = Tabel(n, m)
        content=ttk.Frame(self.root)
        content.grid(column=0, row=0)
        frame=ttk.Frame(content, borderwidth=5, relief="sunken")
        frame.grid(column=0, row=0)
        for ni in range(n):
            for mj in range(m):
                self.addButton(ni, mj, frame)
        self.freqlabels = []
        for mj in range(m):
            self.addLabel(mj, frame, n)
                
    def addButton(self, ni, mj, frame):
        button = ttk.Button(frame, text=str(self.tabel[ni][mj]), command=lambda: self.buttonPress(ni, mj, button))
        button.grid(column=ni, row=mj)

    def addLabel(self, m, frame, n):
        assert len(self.freqlabels)==m
        label = ttk.Label(frame)
        self.freqlabels.append(label)
        self.refreshLabel(m)
        label.grid(column=n, row=m)    
    
    def refreshLabel(self, m):
        self.freqlabels[m].configure(text=str(self.tabel.freq[m][0]))
    
    def buttonPress(self, n, m, b):
        self.tabel[n][m] += 1
        b.configure(text=str(self.tabel[n][m])) 
        self.refreshLabel(m)
    
    def menuClick(self):
        print("menuClick")
    
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    p = Presenter()
    p.build(4, 6)
    p.run()