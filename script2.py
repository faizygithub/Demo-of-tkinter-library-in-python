from tkinter import *
window=Tk()

def Kg_to_gpo():
    print(e2_value.get())
    grm=float(e2_value.get())*1000
    pounds=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274
    t1.insert(END,grm)
    t2.insert(END,pounds)
    t3.insert(END,ounce)
e1=Label(window,text="Kg")
e1.grid(row=0,column=0)
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b2=Button(window,text="Convert",command=Kg_to_gpo,width=20)
b2.grid(row=0,column=2)
e3=Label(window,text="Grams")
e3.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)
e4=Label(window,text="Pounds")
e4.grid(row=1,column=2)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=3)
e5=Label(window,text="Ounces")
e5.grid(row=1,column=4)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=5)

window.mainloop()
