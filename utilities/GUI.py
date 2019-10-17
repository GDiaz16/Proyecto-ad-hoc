from math import sqrt
from tkinter import *
from utilities.IO import IO
import threading
import numpy as np
class GUI:

    def __init__(self):
        self.window = Tk()
        self.c = Canvas(self.window,width=800,height=600)
        self.c.pack()
        self.ratio=25
        self.sep = 100
        self.node_list=[]
        self.connection_list=[]
        self.node_list_objects = []
        self.connection_list_objects =[]
        self.names_list=[]
        self.count = 1
        self.c.bind("<B1-Motion>", self.move)
        self.IO = IO(machine_address=10001, server_port=10000, node_id="N1",GUI=self)
        self.window.mainloop()


    def create_graph(self,node_list, node_edges):
        count = 0
        cols = 2
        #Dibujar los nodos de la lista
        k = int(len(node_list)/cols)
        for i in range(1, k+1):
            for j in range(1, cols +1):
                self.create_node(self.sep * j, self.sep * i, node_list[count].get_id(),node_list[count])
                count += 1
        #Dibujar los nodos faltantes de la lista
        i=k +1
        for j in range(1,len(node_list)%cols+1):
            self.create_node(self.sep * j, self.sep * i, node_list[count].get_id(),node_list[count])
            count += 1


    def create_node(self,x,y,name,node_o):
        node_graphic = self.c.create_oval(x, y, x + self.ratio * 2, y + self.ratio * 2, fill="blue")
        name_graphic = self.c.create_text(x + self.ratio, y - 10, text=f"Nodo {node_o.get_id()}")
        node_o.set_graphic_position_title(name_graphic)
        node_o.set_graphic_position_circle(node_graphic)
        self.node_list_objects.append(node_o)

        self.node_list.append(node_graphic)
        self.names_list.append(name_graphic)

    def delete_node(self,node):
        self.c.delete(node.get_graphic_position_circle())
        self.c.delete(node.get_graphic_position_title())

    def create_connection(self,nodo1,nodo2):
        #Verificar que la conexion no exista aun
        for conn in self.connection_list:
            if nodo1 == conn[1] and nodo2 == conn[2]:
               return

        nodo1_graphic = 0
        nodo2_graphic = 0
        #Obtener el numero grafico del nodo 1
        for node in self.node_list_objects:
            if node.get_id() == nodo1:
                nodo1_graphic = node.get_graphic_position_circle()
                break
        #Obtener el numero grafico del nodo 2
        for node in self.node_list_objects:
            if node.get_id() == nodo2:
                nodo2_graphic = node.get_graphic_position_circle()
                break
        #Centrar las puntas de la recta en los centros de los circulos
        x1 = self.c.coords(nodo1_graphic)[0] + self.ratio
        y1 = self.c.coords(nodo1_graphic)[1] + self.ratio
        x2 = self.c.coords(nodo2_graphic)[0] + self.ratio
        y2 = self.c.coords(nodo2_graphic)[1] + self.ratio


        connection_graphic =self.c.create_line(x1,y1,x2,y2,width=4,fill="blue")
        list = [connection_graphic,nodo1,nodo2]
        self.connection_list.append(list)



    def delete_connection(self,connection):
        self.c.delete(connection[0])
        self.connection_list.remove(connection)

    def move(self,event):
        i=0
        for node in self.node_list_objects:
            nodex,nodey =self.c.coords(node.get_graphic_position_circle())[0]+self.ratio,self.c.coords(node.get_graphic_position_circle())[1]+self.ratio
            #Mover los nodos con el movimiento del raton
            if abs(nodex-event.x)<self.ratio and abs(nodey-event.y)<self.ratio:
                self.c.coords(node.get_graphic_position_circle(),event.x-self.ratio,event.y-self.ratio,event.x+self.ratio,event.y+self.ratio)
                self.c.coords(node.get_graphic_position_title(),event.x-self.ratio+self.ratio,event.y-self.ratio-10)

                #Actualizar las aristas del grafo
                for connection in self.connection_list:
                    if connection[1]==node.get_id():
                        x1 = self.c.coords(node.get_graphic_position_circle())[0] + self.ratio
                        y1 = self.c.coords(node.get_graphic_position_circle())[1] + self.ratio
                        x2 = self.c.coords(connection[0])[2]
                        y2 = self.c.coords(connection[0])[3]
                        self.c.coords(connection[0],x1,y1,x2,y2)

                    elif connection[2]==node.get_id():
                        x2 = self.c.coords(node.get_graphic_position_circle())[0] + self.ratio
                        y2 = self.c.coords(node.get_graphic_position_circle())[1] + self.ratio
                        x1 = self.c.coords(connection[0])[0]
                        y1 = self.c.coords(connection[0])[1]
                        self.c.coords(connection[0],x1,y1,x2,y2)
                #Buscar y eliminar aristas
                self.quality()
                self.search()
                break
            i=i+1



    def quality(self):
        #Elimina conexiones debiles
        for connection in self.connection_list:
            x1 = self.c.coords(connection[0])[0]
            y1 = self.c.coords(connection[0])[1]
            x2 = self.c.coords(connection[0])[2]
            y2 = self.c.coords(connection[0])[3]
            if sqrt((x2-x1)**2+(y2-y1)**2)>180.0:
                self.delete_connection(connection)

    def search(self):
        #Conecta terminales cercanos
        for i in range(len(self.node_list_objects)):
            for j in range(i + 1, len(self.node_list_objects)):
                x1 = self.c.coords(self.node_list_objects[i].get_graphic_position_circle())[0]+self.ratio
                y1 = self.c.coords(self.node_list_objects[i].get_graphic_position_circle())[1]+self.ratio
                x2 = self.c.coords(self.node_list_objects[j].get_graphic_position_circle())[0]+self.ratio
                y2 = self.c.coords(self.node_list_objects[j].get_graphic_position_circle())[1]+self.ratio
                if sqrt((x2-x1)**2+(y2-y1)**2)<120.0:
                    self.create_connection(self.node_list_objects[i].get_id(),self.node_list_objects[j].get_id())
GUI = GUI()

