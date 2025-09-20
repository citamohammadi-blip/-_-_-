from tkinter import *
from tkinter import messagebox
win=Tk()
win.resizable(1,0)
win.geometry('250x400')

def show_choice():
    messagebox.showinfo('Done',f'os : {zaban.get()}\language :{zaban2.get()}')
        

lbl_fream1=LabelFrame(win,text='انتخاب زبان')
lbl_fream1.pack(fill='both')
zaban=StringVar(value='python')
zaban.set('python')
r1=Radiobutton(lbl_fream1, text='python',variable=zaban,value='python')
r1.pack()
r2=Radiobutton(lbl_fream1,text='java',variable=zaban,value='java')
r2.pack()
r3=Radiobutton(lbl_fream1,text='c++',variable=zaban,value='c++')
r3.pack()


lbl_fream2=LabelFrame(win,text='انتخاب سیستم عامل')
lbl_fream2.pack(fill='both')
zaban2=StringVar()
#zaban2.set('')
r4=Radiobutton(lbl_fream2, text='windows',variable=zaban2,value='windows')
r4.pack()
r5=Radiobutton(lbl_fream2,text='linux',variable=zaban2,value='linux')
r5.pack()
r6=Radiobutton(lbl_fream2,text='masos',variable=zaban2,value='masos')
r6.pack() 

btn_choice=Button(win,text='نمایش انتخواب',width=15,command=show_choice)
btn_choice.place(x=70,y=230)

lbl_language=Label(win,text='language :',font='arial 12 bold')
lbl_language.place(x=15,y=270)

lbl_os=Label(win,text='os :',font='arial 12 bold')
lbl_os.place(x=15,y=300)
win.mainloop()