import tkinter as tk

class Greeting:
    def __init__(self, window):
        window.geometry('300x300')
        window.title("Greeting App")

        self.lb = tk.Label(text="Enter Your Name:")
        self.lb.pack()

        self.text = tk.Entry(width=20)
        self.text.pack()

        self.btn = tk.Button(text="Submit", command=self.generatePattern)
        self.btn.pack()

        self.lb1 = tk.Label(text="", width=20)
        self.lb1.pack()

        window.mainloop()

    def generatePattern(self) -> str:
        inp = self.text.get()
        str = ""
        for i in range(int(inp)):
            temp = "*"*i
            temp = temp + "\n"
            str = str+temp
            self.lb1.config(text = str, anchor="w", justify="left")


root = tk.Tk()
obj = Greeting(root)