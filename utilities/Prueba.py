from tkinter import *
import threading

class App(threading.Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()
        t = threading.Thread(target=self.p)
        t.start()

    def run(self):
        loop_active = True
        while loop_active:
            user_input = input("Give me your command! Just type \"exit\" to close: ")
            label = Label(self.root, text=user_input)
            label.pack()
            print("Hola")


    def p(self):
        while True:
            #print("a")
            pass


ROOT = Tk()
APP = App(ROOT)

LABEL = Label(ROOT, text="Hello, world!")
LABEL.pack()
ROOT.mainloop()
