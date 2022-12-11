from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from parabola import parabola 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.pyplot import grid

root = Tk()
root.geometry("400x150")

labelfr = LabelFrame(root,text="result",padx=20,pady=20)
labelfr.place(x=60,y=380)

vo = Label(root,text = "Masukan Keepatan awal")
agl= Label(root,text = "Angel")
x1 = Label(root,text = " Masukan\n nilai x\n(dalam meter)")
y1=  Label(root,text = " Masukan\n nilai y\n(dalam meter)")
e1 = Entry(root,width=10)
e2 = Entry(root,width=10)
e3 = Entry(root,width=10)
e4 = Entry(root,width=10)
vo.place(x = 16, y = 50)
e1.place(x = 20, y = 70)
agl.place(x = 113, y = 50)
e2.place(x = 120, y = 70)
x1.place(x = 202, y = 20)
e3.place(x = 220, y = 70)
y1.place(x = 310, y = 30)
e4.place(x = 320, y = 70)
def plot():
    vo=float(e1.get())
    agl=float(e2.get())
    x1=float(e3.get())
    y1=float(e4.get())
    parabola(vo,agl,x1,y1)
   


root.title(' Mencari Gerak ')
plot_button = Button(master = root, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Proses")
plot_button.place(x = 160, y = 100)
root.mainloop()