from tkinter import *

root=Tk()
root.geometry("380x500+200+100")
root.title("Manmeet Moudgill's Calculator")
root.resizable(False,False)
#-------------Functions--------------
#-----this function takes 1,2,3,4,5,6,7,8,9 as argument ------------------------
def enter_number(x):
    if entry_box.get()=="0":
        entry_box.delete(0,END)
        entry_box.insert(0,str(x))
    else:
        length=len(entry_box.get())    
        entry_box.insert(length,str(x))



def enter_operators(x):
    if entry_box.get() !="0":
        length=len(entry_box.get())
        s1=entry_box.get()
        last_ch=s1[-1:]
        if last_ch in ["+","-","/"] or s1[-2:]=="**":
            pass
        else:
            entry_box.insert(length,btn_operator[x]["text"])
    



def clearf():
        entry_box.delete(0,END)
        entry_box.insert(0,0)

b=0
history=[]#---------we have created a list to store the operation history-----
def equal_func():
    
    a=entry_box.get()
    b=eval(a)
    entry_box.delete(0,END)
    entry_box.insert(0,b)
    history.append(str(b))
  #------------it is used to pack the recent operation data-----------------------
    label1.configure(text="History: " + '|'.join(history[0:4]),font="verdana 11 bold")

def del_func():
    length=len(entry_box.get())
    entry_box.delete(length-1,END)
    if length==1:
        entry_box.insert(0,"0")


#-----for creating entry box
entry_box=Entry(root,font="verdana 16 bold",width=22,bd=6,justify=RIGHT)
entry_box.insert(0,"0")
entry_box.place(x=20,y=10)




#--------creating zero Button-------
button1=Button(root,width=15,text="0",bd=6,command=lambda x=0:enter_number(x))
button1.place(x=40,y=280)

# #--------creating dot Button---------
button2=Button(root,width=4,font="times 14 bold",text=".",bd=6,command=lambda x=".":enter_number(x))
button2.place(x=120,y=340)

#-------------creating clear Button------------------
button3=Button(root,width=4,font="times 14 bold",text="C",bd=6,command=clearf)
button3.place(x=40,y=340)

#--------------------creating equals to button---------------------
button4=Button(root,width=4,font="times 14 bold",text="=",bd=6,command=equal_func)
button4.place(x=200,y=340)

#---------------------creating a delete button---------------
button5=Button(root,width=4,font="times 14 bold",text="Del",bd=6,command=del_func)
button5.place(x=280,y=340)


#-----for loop for creating buttons
btn=[]# i have created a list in which i am going to store the numbers from 1 to 9
for i in range(10):
    btn.append(Button(width=5,text=str(i),bd=6,command=lambda x=i:enter_number(x)))

btn_text=1
for i in range(0,3):
    for j in range(0,3):
        btn[btn_text].place(x=40+j*90,y=70+i*70)
        btn_text+=1

#-----for loop for creating operators button
btn_operator=[]
for i in range(4):
    btn_operator.append(Button(width=5,bd=6,command=lambda x=i:enter_operators(x)))#in x it will give you tell you what button did you press

btn_operator[0]["text"]="+"
btn_operator[1]["text"]="-"
btn_operator[2]["text"]="/"
btn_operator[3]["text"]="*"

for i in range(4):
    btn_operator[i].place(x=290,y=70+i*70)




#-----------------creating status bar --------------------
label1=Label(root,text="History",anchor="w",height=3,font="verdana 11 bold",relief=SUNKEN)
label1.pack(side=BOTTOM,fill=X)

label2=Label(root,text="Manmeet's Calculator",anchor="se",height=3,font="verdana 10 bold")
label2.pack(side=BOTTOM)

root.mainloop()