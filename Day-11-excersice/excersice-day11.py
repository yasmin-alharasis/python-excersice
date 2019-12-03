from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import *
from tkinter import scrolledtext
# =============================================================================
# Q1
# =============================================================================
parent= Tk()

name=Label(parent,text='Name').grid(row=0,column=0)
svalue=StringVar()
e1=Entry(parent,textvariable=svalue).grid(row=0,column=1)
password=Label(parent,text="Password").grid(row=1,column=0)
svalue1=StringVar()
e2=Entry(parent,textvariable=svalue1).grid(row=1,column=1)

def act():
    if svalue.get()=="Orange" and svalue1.get()=="Coding Academy":
        print("Successful login")
    else:
        print("Wrong User Name or Password")
    
submit=Button(parent,text='Submit',command=act).grid(row=4,column=0)
parent.mainloop()
# =============================================================================
# Q2
# =============================================================================

def clicked():
    messagebox.showinfo('','This is a message')

def open_child1():
    parent= Tk()
    name=Label(parent,text='Emp Number').grid(row=0,column=0)
    e1=Entry(parent).grid(row=0,column=1)
    password=Label(parent,text="Emp Name").grid(row=1,column=0)
    e2=Entry(parent).grid(row=1,column=1)
        
    exit=Button(parent,text='exit').grid(row=4,column=0)
    parent.mainloop()    
    
def open_child2():
    v = Toplevel(root)
    v.geometry('300x200')
    txt = scrolledtext.ScrolledText(v, width=40, height=10)
    txt.insert("insert","the count is 1 ")
    txt.grid(column=0,row=0)
            
root = Tk()
root.title("root window")
Button(root,text="Open message",command=clicked).grid()    
Button(root,text="Open child window 1",command=open_child1).grid()    
Button(root,text="Open child window 2",command=open_child2).grid()    

root.mainloop()   
    
# =============================================================================
#Q3     
# =============================================================================
col = Tk()
col.geometry("400x250")
def getColor():
    color = askcolor()
    col.configure(background = color[1])
Button(text="Select Color", command = getColor).pack()
mainloop()
    
    
    
    
    
    
    
    
    
    
    
