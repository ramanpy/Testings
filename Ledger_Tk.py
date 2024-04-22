from tkinter import*

root = Tk()
root.geometry("800x2000")
root.title("LedgerPro")


#Addition of two number

num1=IntVar()
num2=IntVar()

def Add():
    Sum=num1.get() + num2.get()
    Lab.config(text="Result: "+str(Sum))

def Clear():
    num1.set("")
    num2.set("")
    Lab.config(text="Result: 0")
Label(text="First number",font=23).place(x=50,y=200)
Label(text="Second number",font=23).place(x=50,y=250)
    
Entry(root,textvariable=num1,width=10,bd=3,font=20).place(x=200,y=200)
Entry(root,textvariable=num2,width=10,bd=3,font=20).place(x=200,y=250)

Button(root,text="ADD",font=20,bg='yellow',fg='black',command=Add).place(x=150,y=300)
Button(root,text="CLEAR",font=20,bg='yellow',fg='black',command=Clear).place(x=250,y=300)

Lab=Label(root,text = "Result: 0",font = 23)
Lab.place(x=50,y=350)


root.mainloop()
