import tkinter as tk

from Test.Screen import Screen


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Screen(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.title("H")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("F")
    app = Demo1(root)
    root.mainloop()

#main()
p = ["a", "b", "c"]
if p.__contains__("b"):
    print("ok")