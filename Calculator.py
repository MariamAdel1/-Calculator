
from tkinter import *
root=Tk()
root.geometry("306x343")
root.configure(bg="#FFFFFF")
root.title("Calculator")
root.resizable("False","False")
lab=Entry(root,bg="#FFFFFF",font="Arial 22",width=18,bd=10)#"lightGrey
lab.grid(row=0,column=0,columnspan=4)
font1="Arial 20 bold"
btn_color="#FAB7E0" #"grey"
btn_tas="#C2C0C0"
def click(value):
   lab.insert(END,value)
def clear():
   lab.delete(0,END)
def Equle():
   screen=lab.get()
   if screen.find("+")!=-1:
      l1=screen.split("+")
      result=sum(map(int,l1))
      clear()
      lab.insert(END,result)
   elif screen.find("-")!=-1:
      l2=screen.split("-")
      l2=list(map(int,l2))
      result=l2[0]-l2[1]
      if len(l2)>2:
         i=2
         while i<len(l2):
            result-=l2[i]
            i+=1
      clear() 
      lab.insert(END,result)
   elif screen.find("*")!=-1:
      l3=screen.split("*")
      l3=list(map(int,l3))
      result=l3[0]*l3[1]
      if len(l3)>2:
         i=2
         while i<len(l3):
            result*=l3[i]
            i+=1
      clear()
      lab.insert(END,result)
   elif screen.find("/")!=-1:
      l4=screen.split("/")
      l4=list(map(int,l4))
      result=l4[0]/l4[1]
      if len(l4)>2:
         i=2
         while i<len(l4):
            result /=l4[i]
            i+=1
      clear()
      lab.insert(END,round(result,2))      

      
            

b7=Button(root,text="7",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(7))
b7.grid(row=1,column=0)
b8=Button(root,text="8",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(8))
b8.grid(row=1,column=1)
b9=Button(root,text="9",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(9))
b9.grid(row=1,column=2)
b4=Button(root,text="4",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(6))
b6.grid(row=2,column=2)
add=Button(root,text="+",font=font1,bg=btn_tas,bd=10,height=1,width=3,command=lambda:click('+'))
add.grid(row=1,column=3)
b1=Button(root,text="1",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(1))
b1.grid(row=3,column=0)
b2=Button(root,text="2",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(2))
b2.grid(row=3,column=1)
b3=Button(root,text="3",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(3))
b3.grid(row=3,column=2)
mun=Button(root,text="-",font=font1,bg=btn_tas,bd=10,height=1,width=3,command=lambda:click('-'))
mun.grid(row=2,column=3)
mult=Button(root,text="x",font=font1,bg=btn_tas,bd=10,height=1,width=3,command=lambda:click('*'))
mult.grid(row=3,column=3)
b0=Button(root,text="0",font=font1,bg=btn_color,bd=10,height=1,width=3,command=lambda:click(0))
b0.grid(row=4,column=0)
bClear=Button(root,text="C",font=font1,bg="#A3A2A2",bd=10,height=1,width=3,command=clear)
bClear.grid(row=4,column=1)
bEqule=Button(root,text="=",font=font1,bg="#C295BA",bd=10,height=1,width=3,command=Equle)
bEqule.grid(row=4,column=2)
bDivg=Button(root,text="/",font=font1,bg=btn_tas,bd=10,height=1,width=3,command=lambda:click('/'))
bDivg.grid(row=4,column=3)






root.mainloop()