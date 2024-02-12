import tkinter as tk
from tkinter import messagebox

class Greeting:
    def __init__(self, window):
        window.geometry('300x300')
        window.title("Greeting App")

        self.lb = tk.Label(text="Enter The temperature in Celsius:")
        self.lb.pack()

        self.text = tk.Entry(width=20)
        self.text.pack()

        self.btn = tk.Button(text="Convert", command=self.convert)
        self.btn.pack()

        self.lb1 = tk.Label(text="", width=50)
        self.lb1.pack()

        window.mainloop()

    def convert(self):
        inp = self.text.get()
        fah = (float(inp)*9)/5 + 32
        self.lb1.config(text = f"The temperature in fahrenheit is {fah}")
        messagebox.showinfo("Result", f"{inp} degrees Celsius is equal to {fah:.2f} degrees Fahrenheit.")


root = tk.Tk()
obj = Greeting(root)