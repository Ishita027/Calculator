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
       if text=='pi':
          if num=="":
             result=str(m.pi)
          else:
            result=str(float(num)*m.pi)
       if text=='\u221Ax':
          result=str(m.sqrt(float(num)))
       if text=='x!':
          result=str(m.factorial(float(num)))
       if text=='sin':
           result=str(m.sin(float(num)))
       if text=='cos':
           result=str(m.cos(float(num)))
       if text=='tan':
           result=str(m.tan(float(num)))
       if text=='e':
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
    length=len(value)-1
    e1.delete(length,END)

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
root.geometry('788x650')
root.iconbitmap('Calculator image.ico')
e1=Entry(root,borderwidth=2,font='Times 40 italic',width=29,relief=SUNKEN)
e1.grid(row=0,column=0,columnspan=4)
bsin=Button(root,text='sin',font='Times 30 bold',width=8,bg='light grey')
bsin.bind('<Button-1>',fun)
bsin.grid(row=1,column=0)
bcos=Button(root,text='cos',font='Times 30 bold',width=8,bg='light grey')
bcos.bind('<Button-1>',fun)
bcos.grid(row=1,column=1)
btan=Button(root,text='tan',font='Times 30 bold',width=8,bg='light grey')
btan.bind('<Button-1>',fun)
btan.grid(row=1,column=2)
bclear=Button(root,text='C',font='Times 30 bold',width=7,bg='light grey',command=clear)
bclear.grid(row=1,column=3)
bpi=Button(root,text='pi',font='Times 30 bold',width=8,bg='light grey')
bpi.bind('<Button-1>',fun)
bpi.grid(row=2,column=0)
bbr1=Button(root,text='(',font='Times 30 bold',width=8,bg='light grey',command=lambda: click('('))
bbr1.grid(row=2,column=1)
bbr2=Button(root,text=')',font='Times 30 bold',width=8,bg='light grey',command=lambda :click(')'))
bbr2.grid(row=2,column=2)
bbk=Button(root,text='Bksp',font='Times 30 bold',width=7,bg='light grey',command=bksp)
bbk.grid(row=2,column=3)

bfact=Button(root,text='x!',font='Times 30 bold',width=8,bg='light grey')
bfact.bind('<Button-1>',fun)
bfact.grid(row=3,column=0)
broot=Button(root,text='\u221Ax',font='Times 30 bold',width=8,bg='light grey')
broot.grid(row=3,column=1)
broot.bind('<Button-1>',fun)
be=Button(root,text='e',font='Times 30 bold',width=8,bg='light grey')
be.grid(row=3,column=2)
be.bind('<Button-1>',fun)
bdiv=Button(root,text='/',font='Times 30 bold',width=7,bg='light grey',command=lambda:click('/'))
bdiv.grid(row=3,column=3)
b7=Button(root,text='7',font='Times 30 bold',width=8,bg='white',command=lambda:click('7'))
b7.grid(row=4,column=0)
b8=Button(root,text='8',font='Times 30 bold',width=8,bg='white',command=lambda:click('8'))
b8.grid(row=4,column=1)
b9=Button(root,text='9',font='Times 30 bold',width=8,bg='white',command=lambda:click('9'))
b9.grid(row=4,column=2)
bmul=Button(root,text='*',font='Times 30 bold',width=7,bg='light grey',command=lambda:click('*'))
bmul.grid(row=4,column=3,)
b4=Button(root,text='4',font='Times 30 bold',width=8,bg='white',command=lambda:click('4'))
b4.grid(row=5,column=0)
b5=Button(root,text='5',font='Times 30 bold',width=8,bg='white',command=lambda:click('5'))
b5.grid(row=5,column=1)
b6=Button(root,text='6',font='Times 30 bold',width=8,bg='white',command=lambda:click('6'))
b6.grid(row=5,column=2)
bsub=Button(root,text='-',font='Times 30 bold',width=7,bg='light grey',command=lambda:click('-'))
bsub.grid(row=5,column=3)
b1=Button(root,text='1',font='Times 30 bold',width=8,bg='white',command=lambda:click('1'))
b1.grid(row=6,column=0)
b2=Button(root,text='2',font='Times 30 bold',width=8,bg='white',command=lambda:click('2'))
b2.grid(row=6,column=1)
b3=Button(root,text='3',font='Times 30 bold',width=8,bg='white',command=lambda:click('3'))
b3.grid(row=6,column=2)
badd=Button(root,text='+',font='Times 30 bold',width=7,bg='light grey',command=lambda:click('+'))
badd.grid(row=6,column=3)
blog=Button(root,text='log',font='Times 30 bold',width=8,bg='white')
blog.grid(row=7,column=0)
blog.bind('<Button-1>',fun)
b0=Button(root,text='0',font='Times 30 bold',width=8,bg='white',command=lambda:click('0'))
b0.grid(row=7,column=1)
bdec=Button(root,text='.',font='Times 30 bold',width=8,bg='white',command=lambda:click('.'))
bdec.grid(row=7,column=2)
bequal=Button(root,text='=',font='Times 30 bold',width=7,bg='light grey',command=evaluate)
bequal.grid(row=7,column=3)
root.mainloop()