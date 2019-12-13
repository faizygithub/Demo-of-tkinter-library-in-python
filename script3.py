from tkinter import *
window=Tk()
b1=Button(window,height=20,width=20)
try:
    image1=PhotoImage(file="/Desktop/test.jpg") # here you can path name accorrding to
                                                # ffile name
    b1.config(image=self.image1)
    b1.image=image
except TclError:
    pass
b1.pack(side=left)
window.mainloop()
