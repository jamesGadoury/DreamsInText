import tkinter as tk
from tkinter import *
from tkinter import font
from game import *
import subprocess as sub


class App(tk.Frame):
    def __init__(self, master=None):
         super().__init__(master)
         #self.pack()
         #self.frame = Frame(width = 800, height = 500)
         #self.frame.pack()
         self.master.title("Dreams in Text")
         top=self.winfo_toplevel()
         top.rowconfigure(0, weight=1)
         top.columnconfigure(0, weight=1)
         self.grid_rowconfigure(0, weight = 1)
         self.grid_columnconfigure(0, weight = 1)
         self.textbox=Text(width = 130)
         self.textbox.grid(row = 0, column = 0, sticky = tk.N+tk.S+tk.E+tk.W)
         self.textbox.grid_rowconfigure(0, weight = 1)
         self.textbox.grid_columnconfigure(0, weight = 1)
         #self.textbox.pack(side = LEFT, fill = BOTH, expand = YES)
         #self.yscrollbar=Scrollbar(orient=VERTICAL, command=self.textbox.yview)
         #self.yscrollbar.pack(side=RIGHT, fill=Y)
        # self.textbox["yscrollcommand"]=self.yscrollbar.set
         self.textbox.configure(state = DISABLED)
         #self.textbox.place(x = 10, y = 10, height = 100)
         self.entrythingy = Entry()
         self.entrythingy.grid(row = 1)
         self.entrythingy.grid_rowconfigure(1, weight = 0)

         #self.entrythingy.pack(side = LEFT)
         #self.entrythingy.place(x = 10, y = 470, height = 20)
         # here is the application variable
         self.contents = StringVar()
         # set it to some value
         self.contents.set("")
         # tell the entry widget to watch this variable
         self.entrythingy["textvariable"] = self.contents

         # and here we get a callback when the user hits return.
         # we will have the program print out the value of the
         # application variable when the user hits return
         self.entrythingy.bind('<Key-Return>', self.user_input)
         sys.stdout.write = self.redirector #whenever sys.stdout.write is called, redirector is called.
         beginGame()

    def user_input(self, event):
        userInput = self.contents.get()
        playTurn(userInput)
        self.contents.set("")

    def redirector(self, inputStr):
        self.textbox.configure(state='normal')
        self.textbox.insert(INSERT, inputStr)
        self.textbox.configure(state='disabled')






#create the app
myapp = App()



#start the app
myapp.mainloop()
