import numpy as np
from PIL import ImageTk, Image
import tkinter as tk
from utilities.IO import IO


class Screen:
    def __init__(self, machine_address="",node_id=""):
        self.window = tk.Tk()
        self.canvas1 = tk.Canvas(self.window, width=700, height=500)
        self.canvas1.grid(column=0, row=0)
        self.canvas1.pack()
        self.IO = IO(machine_address=machine_address, node_id=node_id)

        #self.canvas1.create_oval(10,10,100,100,fill="blue")
        img = self.Split_Image("")
        #print(img)

        image=self.Show_Image(img)
        self.window.title(f"Screen of {node_id}")
        self.window.mainloop()

    def Split_Image(self,image):
        img = Image.open('pikachu.jpg')
        img = np.array(img)
        ancho = img.shape[1]
        alto = img.shape[0]
        i = 1
        j = 0
        filas = 2
        columnas = 1
        img = img[(alto // filas) * i:(alto // filas) * (i + 1), (ancho // columnas) * j:(ancho // columnas) * (j + 1),:]
        return img

    def Show_Image(self,img_array=None):
        img = Image.open('pikachu.jpg')
        img = np.array(img)
        #img = img_array
        img = Image.fromarray(img)
        img.save("image.png")
        image = tk.PhotoImage(file="image.png")
        self.canvas1.create_image(30, 100, image=image, anchor="nw")

        return image

