# import sys
# sys.path.append("E:/Universidad/Materias/Lenguajes de Programación/Proyecto")

from Machine.Resource_Admin.Distributed_System import Distributed_System
from PIL import Image
from PIL.ImageTk import PhotoImage
from Machine.IO import IO
from Machine.ALU import ALU
from Machine.CU import CU
from Machine.RAM import RAM
from utilities.GraphicObject import GraphicObject
import tkinter as tk
import numpy as np

class Screen:
    def __init__(self, master, name = "", geometry = ""):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()


        #self.window = tk.Tk()
        self.master.geometry(geometry)
        self.c = tk.Canvas(self.master, width=400, height=300)
        self.c.pack()

        self.ratio=25
        self.graphic_objects_list = []

        self.draw_something(20,20,"red","oval")
        self.draw_something(40,40,"green","rectangle")

        #self.RAM = RAM()
        #self.ALU = ALU()
        #self.CU = CU(RAM,ALU)
        #self.Distributed_System = Distributed_System(self.RAM, self.CU, self.ALU, node_id)
        #self.IO = IO(machine_address = machine_address, node_id = node_id, screen = self, DS = self.Distributed_System)


        self.c.bind("<B1-Motion>", self.move)
        self.master.title(f"Screen of {name}")

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
        self.c.create_image(20, 20, image=image, anchor="nw")
        print("show image")
        return image

    def draw_something(self,x1,y1,color,type):

        if type =="oval":
            canvas_pos = self.c.create_oval(x1, y1, x1 + self.ratio, y1 + self.ratio, fill=color)
            coords = self.c.coords(canvas_pos)
            go = GraphicObject(type=type, coords=coords, canvas_position=canvas_pos, color=color)
            self.graphic_objects_list.append(go)
        if type == "rectangle":
            canvas_pos = self.c.create_rectangle(x1, y1, x1 + self.ratio, y1 + self.ratio, fill=color)
            coords = self.c.coords(canvas_pos)
            go = GraphicObject(type=type, coords=coords, canvas_position=canvas_pos, color=color)
            self.graphic_objects_list.append(go)

    def draw_stream(self,graphics):

        for g in graphics:
            x1 = 20
            y1 = 20
            color = "red"
            self.c.coords(g.get_canvas_position(),g.get_coords()[0],g.get_coords()[1],g.get_coords()[2],g.get_coords()[3])

    def move(self,event):
        i=0
        for go in self.graphic_objects_list:
            gox,goy =self.c.coords(go.get_canvas_position())[0]+self.ratio,self.c.coords(go.get_canvas_position())[1]+self.ratio
            #Mover los nodos con el movimiento del raton
            if abs(gox-event.x)<self.ratio and abs(goy-event.y)<self.ratio:
                self.c.coords(go.get_canvas_position(),event.x-self.ratio,event.y-self.ratio,event.x+self.ratio,event.y+self.ratio)
                go.set_coords(self.c.coords(go.get_canvas_position()))
                #self.IO.stream(self.graphic_objects_list)
                break
            i=i+1

