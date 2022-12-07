from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from parabola import parabola 

root = Tk()
root.geometry("600x170")

labelfr = LabelFrame(root,text="result",padx=20,pady=20)
labelfr.place(x=60,y=380)

vo = Label(root,text = "Masukkan Kecpatan awal")
agl= Label(root,text = "Masukkan Sudut")
x1 = Label(root,text = " Masukan nilai x\n(dalam meter)")
y1=  Label(root,text = " Masukan nilai y\n(dalam meter)")
e1 = Entry(root,width=14)
e2 = Entry(root,width=13)
e3 = Entry(root,width=11)
e4 = Entry(root,width=11)
vo.place(x = 26, y = 20)
e1.place(x = 50, y = 70)
agl.place(x = 210, y = 20)
e2.place(x = 210, y = 70)
x1.place(x = 332, y = 5)
e3.place(x = 342, y = 70)
y1.place(x = 450, y = 5)
e4.place(x = 460, y = 70)
def plot():
    vo=float(e1.get())
    agl=float(e2.get())
    x1=float(e3.get())
    y1=float(e4.get())
    parabola(vo,agl,x1,y1)
   


root.title(' Mencari Gerak Parabola')
plot_button = Button(master = root, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Proses")
plot_button.place(x = 260, y = 100)
root.mainloop()