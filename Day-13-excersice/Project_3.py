import sqlite3
from tkinter import *
from tkinter import scrolledtext
# =============================================================================
# 

conn = sqlite3.connect('OrgDB.db')
print("Opened database succuessfully")

conn.execute('''CREATE TABLE Employees
             (EmpNumber INT PRIMARY KEY NOT NULL,
             EmpName TEXT NOT NULL,
             EmpGender TEXT NOT NULL,
             EmpNationality TEXT NOT NULL,
             EmpDOB TEXT NOT NULL,
             Address TEXT NOT NULL,
             EmpDepartment TEXT NOT NULL,
             EmpSALARY REAL)''')

print("Table created successfully")

def fun():
    print("EmpNumber: ",     v.get())
    print("EmpName: ",       v1.get())
    print("EmpGender: ",     v2.get())
    print("EmpNationality: ",v3.get())
    print("EmpDOB: ",        v4.get())
    print("EmpAddress: ",    v5.get())
    print("EmpDepartment: ", v6.get())
    print("EmpSALARY: ",     v7.get())


    data=(v.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get())
    c=conn.cursor()
    
    c.execute("INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?)",data)
    conn.commit()
#    conn.close() 
    print("Data entered successfully!")
    
    
def Add_Employee():
    c=Toplevel(root)
    c.title("Add Employee")
    #c.geometry('200x160x230+130')
    EmpNumber=Label(c,text="EmpNumber").grid(row=0,column=0)
    Entry(c,textvariable=v).grid(row=0,column=1)
    
    EmpName=Label(c,text="EmpName").grid(row=1,column=0)
    Entry(c,textvariable=v1).grid(row=1,column=1)
    
    EmpGender=Label(c,text="EmpGender").grid(row=2,column=0)
    Entry(c,textvariable=v2).grid(row=2,column=1)
    
    EmpNationality=Label(c,text="EmpNationality").grid(row=3,column=0)
    Entry(c,textvariable=v3).grid(row=3,column=1)

    EmpDOB=Label(c,text="EmpDOB").grid(row=4,column=0)
    Entry(c,textvariable=v4).grid(row=4,column=1)
    
    Address=Label(c,text="Address").grid(row=5,column=0)
    Entry(c,textvariable=v5).grid(row=5,column=1)
    
    EmpDepartment=Label(c,text="EmpDepartment").grid(row=6,column=0)
    Entry(c,textvariable=v6).grid(row=6,column=1)
    
    EmpSALARY=Label(c,text="EmpSALARY").grid(row=7,column=0)
    Entry(c,textvariable=v7).grid(row=7,column=1)

    submit=Button(c,text="Submit",command=fun).grid(row=8,column=0)
    
def View_Employee():
    cc=Toplevel(root)
    cc.title("View Employees")
    cc.geometry('350x200')
    txt=scrolledtext.ScrolledText(cc,width=40,height=10)
    txt.grid(column=0,row=0)
    c=conn.cursor()
    c.execute("SELECT * FROM Employees")
    for row in c:
        txt.insert(END,row)

    

    
root = Tk()
v=IntVar()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=IntVar()

root.title("root window")

Button(root,text="Add Employee",command=Add_Employee).grid()
Button(root,text="View Employees",command=View_Employee).grid()

root.mainloop()