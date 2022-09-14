from  tkinter import *
cal=Tk()
cal.title("CALCUALTOR")
cal.geometry("350x350")
txt=Entry()
txt.place(x=80)
def clicked(num):
    first_num=txt.get()
    txt.delete(0,END)
    txt.insert(0,str(first_num)+str(num))
def add():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    txt.delete(0,END)
def multi():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="multiplication"
    txt.delete(0,END)
def sub():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="substration"
    txt.delete(0,END)
def div():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="division"
    txt.delete(0,END)
def clear():
    txt.delete(0,END)
def equal():
    if math=="addition":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)+int(new_value))
    if math=="multiplication":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)*int(new_value))
    if math=="substration":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)-int(new_value))
    if math=="division":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)/int(new_value))    
but1=Button(cal,text='1',height=2,width=2,command=lambda:clicked(1))
but1.place(x=40,y=20)
but2=Button(cal,text='2',height=2,width=2,command=lambda:clicked(2))
but2.place(x=100,y=20)
but3=Button(cal,text='3',height=2,width=2,command=lambda:clicked(3))
but3.place(x=160,y=20)
but4=Button(cal,text='4',height=2,width=2,command=lambda:clicked(4))
but4.place(x=40,y=80)
but5=Button(cal,text='5',height=2,width=2,command=lambda:clicked(5))
but5.place(x=100,y=80)
but6=Button(cal,text='6',height=2,width=2,command=lambda:clicked(6))
but6.place(x=160,y=80)
but7=Button(cal,text='7',height=2,width=2,command=lambda:clicked(7))
but7.place(x=40,y=140)
but8=Button(cal,text='8',height=2,width=2,command=lambda:clicked(8))
but8.place(x=100,y=140)
but9=Button(cal,text='9',height=2,width=2,command=lambda:clicked(9))
but9.place(x=160,y=140)
but0=Button(cal,text='0',height=2,width=2,command=lambda:clicked(0))
but0.place(x=220,y=20)
add=Button(cal,text='+',height=2,width=2,command=add)
add.place(x=220,y=80)
multi=Button(cal,text='*',height=2,width=2,command=multi)
multi.place(x=40,y=200)
sub=Button(cal,text='-',height=2,width=2,command=sub)
sub.place(x=100,y=200)
div=Button(cal,text='/',height=2,width=2,command=div)
div.place(x=160,y=200)
clear=Button(cal,text='cl',height=2,width=2,command=clear,bg="gray")
clear.place(x=220,y=200)
equal=Button(cal,text='=',height=2,width=2,command=equal,bg="gray")
equal.place(x=220,y=140)
cal.mainloop()
