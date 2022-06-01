

from tkinter import *
a=Tk()
a.title("junaid's Calulator ")
e=Entry(a,borderwidth=4,width=30,font="green 20 bold")

e.grid(row=0,column=10)
def clik(number):
    global k
    k=e.get()
    e.delete(0,END)
    e.insert(0,str(k)+str(number))
def clrfun():
    e.delete(0,END)
def plusfun():
    global Q
    global tapal
    tapal="addition"
    Q=e.get()
    e.delete(0,END)
    

def equalfun():
    p=e.get()

    e.delete(0,END)
    if tapal=="addition":
        e.insert(0,int(Q)+int(p))
    if tapal=="multiplication":
        e.insert(0,int(Q)*int(p))
    if tapal=="division":
        e.insert(0,int(Q)/int(p))
    if tapal=="subtraction":
        e.insert(0,int(Q)-int(p))
    if tapal=="%":

        e.insert(0,int(Q)%int(p))
def mulfun():
    global tapal
    global Q
    tapal="multiplication"
    Q=e.get()
    e.delete(0,END)
def divfun():
    global Q
    Q=e.get()
    global tapal
    tapal="division"
    e.delete(0,END)
def subfun():
    global Q
    Q=e.get()
    global tapal 
    tapal="subtraction"

    e.delete(0,END)
def perfun():
    global tapal
    tapal="%"
    global Q
    Q=e.get()
    e.delete(0,END)
def backspace():
    a=str(e.get())
    print(a)

    b=a[:len(a)-1:]
    e.delete(0,END)
    e.insert(0,int(b))

b1=Button(a,text="9",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(9)).grid(row=0,column=0)
b2=Button(a,text="8",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(8)).grid(row=0,column=1)
b3=Button(a,text="7",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(7)).grid(row=0,column=2)
b4=Button(a,text="6",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(6)).grid(row=1,column=0)
b5=Button(a,text="5",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(5)).grid(row=1,column=1)
b6=Button(a,text="4",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(4)).grid(row=1,column=2)
b7=Button(a,text="3",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(3)).grid(row=2,column=0)
b8=Button(a,text="2",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(2)).grid(row=2,column=1)
b9=Button(a,text="1",borderwidth=4,fg="red",padx=16,pady=10,command=lambda :clik(1)).grid(row=2,column=2)
b10=Button(a,text="X",borderwidth=4,fg="red",padx=14,pady=12,command=backspace).grid(row=6,column=0)
plus=Button(a,text="PLUS(+)",borderwidth=4,fg="blue",padx=26,pady=20,command=plusfun).grid(row=3,column=0)
clr=Button(a,text="Clear",borderwidth=4,fg="blue",padx=16,pady=10,command=clrfun).grid(row=3,column=1)
equal=Button(a,text="=",borderwidth=4,fg="blue",font=" italic 20 bold",padx=15,pady=9,command=equalfun).grid(row=3,column=2)
mul=Button(a,text="*",borderwidth=4,fg="blue",font=" italic 20 bold",padx=15,pady=9,command=mulfun).grid(row=4,column=0)
div=Button(a,text="/",borderwidth=4,fg="blue",font=" italic 20 bold",padx=15,pady=9,command=divfun).grid(row=4,column=1)

per=Button(a,text="%",borderwidth=4,fg="blue",font=" italic 20 bold",padx=15,pady=9,command=perfun).grid(row=5,column=2)
sub=Button(a,text="-",borderwidth=4,fg="blue",font=" italic 20 bold",padx=15,pady=9,command=subfun).grid(row=5,column=1)
b0=Button(a,text="0",borderwidth=4,fg="blue",padx=24,pady=13,command=lambda :clik(0)).grid(row=5,column=0)
a.mainloop()

