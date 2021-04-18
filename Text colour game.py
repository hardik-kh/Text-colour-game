from tkinter import *
import tkinter.messagebox
from time import *
import random
c=["Red","Yellow","Orange","Blue","Green","Brown","Pink","Purple","Black","White","Grey"]
cop=["red","yellow","orange","blue","green","brown","pink","purple","black","white","grey"]
a=[]
i=0
s=0
e=0
t=60
timer=0
check= 0
firse = 0
def enter():
    global i
    global s
    global a
    global timer
    global t
    global check
    global firse

    firse=0
    
    if check == 0:
        t=60
        check=1
    
    if timer ==0:
        root.after(1000, clock())
        timer=1


        
    ent['text']="Enter"
    i=random.randint(0,len(c)-1)
    j=random.randint(0,len(cop)-1)
    txt.config(text=c[i])
    txt.config(fg=cop[j])
    a.append(cop[j])
    v=uservalue.get()
    if(v==a[len(a)-2]):
        s=s+1
        sc.config(text="Score: "+str(s))
        ans.delete(0, END)
    else:
        ans.delete(0, END)
        
def stop():
    global s
    global timer
    global t
    global firse
    tkinter.messagebox.showinfo('Popup Window(Title)','Your Score is :'+str(s))
    txt.config(text="Colour")
    txt.config(fg="black")
    s=0
    sc.config(text="Score: "+str(s))
    ent['text']="Start"
    timer = 0
    t=60
    firse = 1

        
root=Tk()

def clock():
    global t
    global firse
    t = t-1
    ti.config(text="Time :"+str(t))
#    time = datetime.datetime.now().strftime("Time: %S")
#    lab.config(text = time)
    #lab['text'] = time
    if t>0 and firse == 0:
        root.after(1000, clock) # run itself again after 1000 ms
    else:
        s=0
        stop()


    
uservalue = StringVar()
root.geometry("300x280")
inf = Label(text=" Type in the colour of the words, and not the word text")
inf.grid(row=1)
sc = Label(text="Score :"+ str(s))
sc.grid(row=2)
ti = Label(root,text="Time :"+ str(t))
ti.grid(row=3,column=0)
txt = Label(root,text="Colour",bg="light grey",font="Arial 36 bold",pady=5)
txt.grid(row=4)
sp1= Label(root,height=1)
sp1.grid(row=5)
ans = Entry(root,textvariable = uservalue)
ans.grid(row=6)
sp2= Label(root,height=1)
sp2.grid(row=7)
st= Button(root,text="Reset",borderwidth=2,command=lambda: stop())
st.grid(row=10)
sp3= Label(root,height=1)
sp3.grid(row=9)
ent = Button(root,text="Start",borderwidth=2,command=lambda: enter())
ent.grid(row=8)
root.mainloop()
