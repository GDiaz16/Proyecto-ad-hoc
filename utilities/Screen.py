import numpy as np
from PIL import ImageTk, Image
import tkinter as tk

from PIL.ImageTk import PhotoImage

from utilities.IO import IO


class Screen:
    def __init__(self, machine_address="",node_id="",geometry=""):
        self.window = tk.Tk()
        self.window.geometry(geometry)
        self.canvas1 = tk.Canvas(self.window, width=400, height=300)
        self.canvas1.pack()
        self.IO = IO(machine_address=machine_address, node_id=node_id, screen=self)

        self.window.title(f"Screen of {node_id}")
        self.window.mainloop()

    def Split_Image(self,image):
        img = Image.open('pikachu.jpg')
        img = np.array(img)
        ancho = img.shape[1]
        alto = img.shape[0]
        filas = 2
        columnas = 3
        parts=[]
        #Separar la imagen en el numero de filas y columnas
        for i in range(filas):
            for j in range(columnas):
                img2 = img[(alto // filas) * i:(alto // filas) * (i + 1),
                       (ancho // columnas) * j:(ancho // columnas) * (j + 1), :]
                parts.append(img2)
        return parts

    def Show_Image(self,img_array=None):
        img = img_array
        #convertir arreglo a imagen
        img = Image.fromarray(img)
        #guardar el archivo localmente
        img.save("image.png")
        image = PhotoImage(file="image.png")
        self.canvas1.create_image(20, 20, image=image, anchor="nw")
        print("show image")
        return image

