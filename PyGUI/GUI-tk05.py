from tkinter import *
window = Tk()
window.title('Place Example')
window.geometry('300x200')
colors = ['red','green','light blue','yellow']
[Label(window,font="Arial 12",text='place(80,%d),anchor=NW' % (20+i*40),bg=colors[i]).place(x=40,y=20+i*40,width=200,height=30) for i in range(4)]
window.mainloop()