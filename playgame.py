#AUTHOR : James Gadoury
#CONTACT: gadouryjames@gmail.com
#GUI application developed using Tkinter and Python3
#Dreams in Text : Text game with a fantastical setting
#relies on playgame.py, game.py, interactables.py, and items.py

import tkinter as tk
from tkinter import *
from tkinter import font
from game import *
import subprocess as sub


class App(tk.Frame):
    def __init__(self, master=None):
        # in app - textbox contains output from print commands in other python files, entry sends user input to other python files
        # textbox resizes with app resize, the entry and label widgets do not
         super().__init__(master)
         self.master.title("Dreams in Text by James Gadoury")

         top=self.winfo_toplevel()
         top.rowconfigure(0, weight=1)
         top.columnconfigure(0, weight=1)
         self.grid_rowconfigure(0, weight = 1)
         self.grid_columnconfigure(0, weight = 1)
         self.grid_rowconfigure(1, weight = 0)
         self.grid_columnconfigure(1, weight = 1)
         self.grid_columnconfigure(0, weight = 0)

         self.textbox=Text(width = 130)
         self.textbox.grid(row = 0, column = 0, sticky = tk.N+tk.S+tk.E+tk.W, columnspan = 2)
         self.textbox.config(background = "black", foreground = "#56f442")
         self.textbox.configure(font=("Times New Roman", 14, "bold"))
         self.textbox.configure(state = DISABLED)
         self.entrythingy = Entry(width = 80)
         self.entrythingy.configure(font=("Times New Roman", 14, "bold"))
         self.entrythingy.grid(row = 1, column = 1)
         self.entryText = Label(text = "<ENTER COMMAND>")
         self.entryText.grid(row = 1, column = 0)


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
        # calls playTurn every time a user input / command is entered - if playTurn returns False then reset in instance of game over has been called
        #     -during reset, new instances have been created for each object
        #     -textbox is cleared of contents from current playthrough
        #     -beginGame is called to start new game
        if not playTurn(userInput):
            self.textbox.configure(state='normal') #textbox state changed to normal to allow edits to update
            self.textbox.delete(1.0, END)
            self.textbox.configure(state='disabled') #textbox state changed to disabled to not allow further edits
            beginGame()
        self.contents.set("")


    def redirector(self, inputStr):
        # redirects print() statements in other python files to the textbox widget
        self.textbox.configure(state='normal')
        self.textbox.insert(INSERT, inputStr)
        self.textbox.see(END)
        self.textbox.configure(state='disabled')






#create the app
myapp = App()



#start the app
myapp.mainloop()
