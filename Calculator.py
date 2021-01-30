from tkinter import *
import math as m
def click(text):
    old=e1.get()
    e1.delete(0,END)
    e1.insert(0,old+text)
    return
def fun(event):
    try:
       val=event.widget
       text=val['text']
       num=e1.get()
       result=''
       if text=='log':
          result=str(m.log10(float(num)))
       elif text=='ln':
           result=str(m.log(float(num)))
       elif text=='\u221Ax':
          result=str(m.sqrt(float(num)))
       elif text=='x!':
          result=str(m.factorial(float(num)))
       elif text=='sin':
           result=str(m.sin(m.radians(float(num))))
       elif text=='cos':
           result=str(m.cos(m.radians(float(num))))
       elif text=='tan':
           result=str(m.tan(m.radians(float(num))))
       elif text=='e':
           if num=='':
               result=str(m.e)
           else:
               result=str(m.e**float(num))
    except Exception as e:
        result="Error!"

    e1.delete(0,END)
    e1.insert(0,result)
def clear():
    e1.delete(0,END)
    return
def bksp():
    value=e1.get()
    value=value[0:len(value)-1]
    e1.delete(0,END)
    e1.insert(0,value)

def evaluate():
    try:
      ans=e1.get()
      ans=eval(ans)

    except Exception as e:
      ans = "Error!"
    e1.delete(0, END)
    e1.insert(0, ans)


root=Tk()
root.title('Calculator')
root.geometry('680x650')
root.iconbitmap('Calculator image.ico')
e1=Entry(root,borderwidth=2,font='Times 40 italic',justify=RIGHT,relief=SUNKEN)
e1.pack(fill=X,ipadx=8)
f=Frame(root)
bsin=Button(f,text='sin',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
bsin.bind('<Button-1>',fun)
bsin.pack(side=LEFT,padx=7,pady=8)
bcos=Button(f,text='cos',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
bcos.bind('<Button-1>',fun)
bcos.pack(side=LEFT,padx=7,pady=8)
btan=Button(f,text='tan',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
btan.bind('<Button-1>',fun)
btan.pack(side=LEFT,padx=7,pady=8)
bclear=Button(f,text='C',font='Times 25 bold',width=7,bg='light grey',command=clear,activebackground='black',activeforeground='white')
bclear.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
bln=Button(f,text='ln',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
bln.bind('<Button-1>',fun)
bln.pack(side=LEFT,padx=7,pady=8)
bbr1=Button(f,text='(',font='Times 25 bold',width=7,bg='light grey',command=lambda: click('('),activebackground='black',activeforeground='white')
bbr1.pack(side=LEFT,padx=7,pady=8)
bbr2=Button(f,text=')',font='Times 25 bold',width=7,bg='light grey',command=lambda :click(')'),activebackground='black',activeforeground='white')
bbr2.pack(side=LEFT,padx=7,pady=8)
bbk=Button(f,text='Bksp',font='Times 25 bold',width=7,bg='light grey',command=bksp,activebackground='black',activeforeground='white')
bbk.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
bfact=Button(f,text='x!',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
bfact.bind('<Button-1>',fun)
bfact.pack(side=LEFT,padx=7,pady=8)
broot=Button(f,text='\u221Ax',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
broot.pack(side=LEFT,padx=7,pady=8)
broot.bind('<Button-1>',fun)
be=Button(f,text='e',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white')
be.pack(side=LEFT,padx=7,pady=8)
be.bind('<Button-1>',fun)
bdiv=Button(f,text='/',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white',command=lambda:click('/'))
bdiv.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
b7=Button(f,text='7',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('7'))
b7.pack(side=LEFT,padx=7,pady=8)
b8=Button(f,text='8',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('8'))
b8.pack(side=LEFT,padx=7,pady=8)
b9=Button(f,text='9',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('9'))
b9.pack(side=LEFT,padx=7,pady=8)
bmul=Button(f,text='*',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white',command=lambda:click('*'))
bmul.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
b4=Button(f,text='4',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('4'))
b4.pack(side=LEFT,padx=7,pady=8)
b5=Button(f,text='5',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('5'))
b5.pack(side=LEFT,padx=7,pady=8)
b6=Button(f,text='6',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('6'))
b6.pack(side=LEFT,padx=7,pady=8)
bsub=Button(f,text='-',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white',command=lambda:click('-'))
bsub.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
b1=Button(f,text='1',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('1'))
b1.pack(side=LEFT,padx=7,pady=8)
b2=Button(f,text='2',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('2'))
b2.pack(side=LEFT,padx=7,pady=8)
b3=Button(f,text='3',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('3'))
b3.pack(side=LEFT,padx=7,pady=8)
badd=Button(f,text='+',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white',command=lambda:click('+'))
badd.pack(side=LEFT,padx=7,pady=8)
f.pack()
f=Frame(root)
blog=Button(f,text='log',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white')
blog.pack(side=LEFT,padx=7,pady=8)
blog.bind('<Button-1>',fun)
b0=Button(f,text='0',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('0'))
b0.pack(side=LEFT,padx=7,pady=8)
bdec=Button(f,text='.',font='Times 25 bold',width=7,bg='white',activebackground='black',activeforeground='white',command=lambda:click('.'))
bdec.pack(side=LEFT,padx=7,pady=8)
bequal=Button(f,text='=',font='Times 25 bold',width=7,bg='light grey',activebackground='black',activeforeground='white',command=evaluate)
bequal.pack(side=LEFT,padx=7,pady=8)
f.pack()
root.mainloop()
