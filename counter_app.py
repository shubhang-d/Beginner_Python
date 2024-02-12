import tkinter as tk
root = tk.Tk()
root.geometry('300x300')
root.title("Counter App")
var = tk.IntVar(value = 0)
lb = tk.Label(text=str(var.get()), font=("Arial",50))
lb.place(x=300/2, y= 0)
def btn1func():
    if var.get() <10:
        data = var.get() + 1
        var.set(data)
        lb['text'] = data
        lb.config(fg = "black")
    else:
        lb.config(fg="red")
def btn2func():
    if var.get() > 0:
        data = var.get() -  1
        var.set(data)
        lb['text'] = data
        lb.config(fg = "black")
    else:
        lb.config(fg="red")
btn1 = tk.Button(text="Increase", command=btn1func)
# btn1.pack(side= 'left', padx=20)
btn1.place(x=10, y = 100)
btn2 = tk.Button(text="Decrease", command=btn2func)
# btn2.pack(side='right', padx=20)
btn2.place(x=200, y= 100)
root.mainloop()