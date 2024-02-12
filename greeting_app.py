import tkinter as tk

class Greeting:
    def __init__(self, window):
        window.geometry('300x300')
        window.title("Greeting App")

        self.lb = tk.Label(text="Enter Your Name:")
        self.lb.pack()

        self.text = tk.Text(height=1, width=20)
        self.text.pack()

        self.btn = tk.Button(text="Submit", command=self.get_text)
        self.btn.pack()

        self.lb1 = tk.Label(text="", width=20)
        self.lb1.pack()

        window.mainloop()

    def get_text(self):
        inp = self.text.get(1.0, "end")
        print(inp)
        self.lb1.config(text=f"Hello, {inp}!!", width=40)

root = tk.Tk()
obj = Greeting(root)
