
from Test.Network import Network
from Test.Screen import Screen

import tkinter as tk

from Test.Graph import Graph


class GUI:

    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Master")

        self.c = tk.Canvas(self.frame, width=800, height=600)
        self.c.pack()
        self.c.bind("<B1-Motion>", self.move)
        self.button1 = tk.Button(self.frame, text = 'Devices', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()


        self.ratio=25
        self.sep_cols = 200
        self.sep_rows = 150
        #self.node_list=[]
        #self.connection_list=[]
        #self.node_list_objects = []
        #self.names_list=[]
        self.count = 1
        self.graph = Graph()
        self.NET = Network(self.graph)
        self.create_graph()
        #self.master.mainloop()


    def new_window(self):
        geometries = ["400x300+0+0","400x300+410+0","400x300+820+0","400x300+0+350","400x300+410+350","400x300+820+350"]
        for i in range(6):
            self.newWindow = tk.Toplevel(self.master)
            self.app = Screen(self.newWindow, f"D{i+1}", geometries[i])

    def set_graph(self,graph):
        self.graph = graph

    def create_graph(self):
        count = 0
        cols = 2
        node_list = self.graph.node_list
        connections = self.graph.connections
        #self.graph = graph

        #Dibujar los nodos de la lista
        k = int(len(node_list)/cols)
        for i in range(1, k+1):
            for j in range(1, cols +1):
                self.create_node(self.sep_cols * j, self.sep_rows * i, node_list[count].name, node_list[count])
                count += 1
        #Dibujar los nodos faltantes de la lista
        i=k +1
        for j in range(1,len(node_list)%cols+1):
            self.create_node(self.sep_cols * j, self.sep_rows * i, node_list[count].name, node_list[count])
            count += 1

        for conn in connections:
            self.draw_connection(conn.node1,conn.node2)

    def create_node(self,x,y,name,node_o):
        node_graphic = self.c.create_oval(x, y, x + self.ratio * 2, y + self.ratio * 2, fill="blue")
        name_graphic = self.c.create_text(x + self.ratio, y - 10, text=f"Nodo {node_o.get_id()}")
        node_o.set_graphic_position_title(name_graphic)
        node_o.set_graphic_position_circle(node_graphic)
        #self.node_list_objects.append(node_o)
        #self.node_list.append(node_graphic)
        #self.names_list.append(name_graphic)

    # def delete_node(self,node):
    #     self.c.delete(node.get_graphic_position_circle())
    #     self.c.delete(node.get_graphic_position_title())

    def draw_connection(self,nodo1,nodo2):
        #Verificar que la conexion no exista aun

        # for conn in self.graph.get_edges_list():
        #     if nodo1.get_id() == conn[1] and nodo2.get_id() == conn[2]:
        #        return
        #     elif nodo1.get_id() == conn[2] and nodo2.get_id() == conn[1]:
        #         return
        #
        # self.connect_machines(nodo1, nodo2)

        nodo1_graphic = 0
        nodo2_graphic = 0
        #Obtener el numero grafico del nodo 1
        for node in self.graph.node_list:
            if node.name == nodo1.name:
                nodo1_graphic = node.graphic_position_circle
                break
        #Obtener el numero grafico del nodo 2
        for node in self.graph.node_list:
            if node.name == nodo2.name:
                nodo2_graphic = node.graphic_position_circle
                break
        #Centrar las puntas de la recta en los centros de los circulos
        x1 = self.c.coords(nodo1_graphic)[0] + self.ratio
        y1 = self.c.coords(nodo1_graphic)[1] + self.ratio
        x2 = self.c.coords(nodo2_graphic)[0] + self.ratio
        y2 = self.c.coords(nodo2_graphic)[1] + self.ratio

        connection_graphic = self.c.create_line(x1,y1,x2,y2,width=4,fill="blue")

        #Insertar posicion grafica en el grafo
        for conn in self.graph.connections:
            if conn.node1 == nodo1 and conn.node2 == nodo2:
                conn.connection_graphic = connection_graphic
                break
        #self.graph.insert_edge(connection_graphic,nodo1.get_id(),nodo2.get_id())

    # def connect_machines(self,node1,node2):
    #     #Decirle al nodo 1 que se conecte directamente al nodo 2
    #     self.IO.connect_to(node1.get_id(),node2.get_machine_address())


    # def delete_connection(self,connection):
    #     self.c.delete(connection[0])
    #     self.graph.delete_edge(connection)

    def move(self,event):
        i=0
        #print(len(self.graph.node_list))
        for node in self.graph.node_list:
            nodex,nodey =self.c.coords(node.graphic_position_circle)[0]+self.ratio, self.c.coords(node.graphic_position_circle)[1]+self.ratio
            #Mover los nodos con el movimiento del raton
            if abs(nodex-event.x)<self.ratio and abs(nodey-event.y) < self.ratio:
                self.c.coords(node.graphic_position_circle,event.x-self.ratio,event.y-self.ratio,event.x+self.ratio,event.y+self.ratio)
                self.c.coords(node.graphic_position_title,event.x-self.ratio+self.ratio,event.y-self.ratio-10)

                #Actualizar las aristas del grafo
                for conn in self.graph.connections:
                    if conn.node1.name == node.name:
                        x1 = self.c.coords(node.graphic_position_circle)[0] + self.ratio
                        y1 = self.c.coords(node.graphic_position_circle)[1] + self.ratio
                        x2 = self.c.coords(conn.connection_graphic)[2]
                        y2 = self.c.coords(conn.connection_graphic)[3]
                        self.c.coords(conn.connection_graphic,x1,y1,x2,y2)

                    elif conn.node2.name == node.name:
                        x2 = self.c.coords(node.graphic_position_circle)[0] + self.ratio
                        y2 = self.c.coords(node.graphic_position_circle)[1] + self.ratio
                        x1 = self.c.coords(conn.connection_graphic)[0]
                        y1 = self.c.coords(conn.connection_graphic)[1]
                        self.c.coords(conn.connection_graphic,x1,y1,x2,y2)
                #Buscar y eliminar aristas
                #self.quality()
                #self.search()
                break
            i=i+1



    # def quality(self):
    #     #Elimina conexiones debiles
    #     for connection in self.graph.get_edges_list():
    #         x1 = self.c.coords(connection[0])[0]
    #         y1 = self.c.coords(connection[0])[1]
    #         x2 = self.c.coords(connection[0])[2]
    #         y2 = self.c.coords(connection[0])[3]
    #         if sqrt((x2-x1)**2+(y2-y1)**2)>150.0:
    #             self.delete_connection(connection)
    #             self.IO.disconnect(connection[1],connection[2])
    #
    # def search(self):
    #     #Conecta terminales cercanos
    #     for i in range(len(self.node_list_objects)):
    #         for j in range(i + 1, len(self.node_list_objects)):
    #             x1 = self.c.coords(self.node_list_objects[i].get_graphic_position_circle())[0]+self.ratio
    #             y1 = self.c.coords(self.node_list_objects[i].get_graphic_position_circle())[1]+self.ratio
    #             x2 = self.c.coords(self.node_list_objects[j].get_graphic_position_circle())[0]+self.ratio
    #             y2 = self.c.coords(self.node_list_objects[j].get_graphic_position_circle())[1]+self.ratio
    #             if sqrt((x2-x1)**2+(y2-y1)**2)<150.0:
    #                 self.draw_connection(self.node_list_objects[i],self.node_list_objects[j])


def main():
    root = tk.Tk()
    root.title("Master")
    app = GUI(root)
    root.mainloop()

main()