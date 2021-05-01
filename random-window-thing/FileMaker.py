import tkinter as tk 
import sys
import os


def start():
    print("starting")



def exitprog():
    print("exiting")



def clearfile():
    print("clear")


root = tk.Tk()

startbtn = tk.Button(root, text="Start", command=start, height="5", width="33", bg="green")
exitbtn = tk.Button(root, text="Stop", command=exitprog, height="5", width="33", bg="red")
clearbtn = tk.Button(root, text="Clear File", command=clearfile, height="5", width="33", bg="yellow")

startbtn.pack()
exitbtn.pack()
clearbtn.pack()
 
root.title('Controls')
root.geometry('240x257')
root.resizable(False, False)
root.mainloop()
