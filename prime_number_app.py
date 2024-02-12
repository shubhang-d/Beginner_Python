import tkinter as tk

class Greeting:
    def __init__(self, window):
        window.geometry('300x300')
        window.title("Greeting App")

        self.lb = tk.Label(text="Enter Your Name:")
        self.lb.pack()

        self.text = tk.Entry(width=20)
        self.text.pack()

        self.btn = tk.Button(text="Submit", command=self.checkPrime)
        self.btn.pack()

        self.lb1 = tk.Label(text="", width=20)
        self.lb1.pack()

        window.mainloop()

    def checkPrime(self) -> str:
        inp = self.text.get()
        get = 1
        print(inp)
        for i in range(2, int(inp)):
            if int(inp)%i==0:
                get = 0
                break
        if get ==0:
            self.lb1.config(text=f"The number is Not Prime")
        else:
            self.lb1.config(text="The number is Prime")
    
    def set_text(self):
        self.lb1.config(text=f"The number is {self.checkPrime}")
        print(f"The number is {self.checkPrime}")

root = tk.Tk()
obj = Greeting(root)
