from math import sqrt
from tkinter import *
import numpy as np
window = Tk()
c = Canvas(window,width=800,height=600)
c.pack()
ratio=25
sep = 100
node_list=[]
connection_list=[]
names_list=[]
count = 1
for i in range(1,3):
    for j in range(1,5):
        node = c.create_oval(sep*i,sep*j,sep*i+ratio*2,sep*j+ratio*2,fill="blue")
        name = c.create_text(sep*i+ratio,sep*j-10,text=f"Nodo {count}")
        node_list.append(node)
        names_list.append(name)
        count += 1
def create_connection(nodo1,nodo2):
    x1=c.coords(node_list[nodo1-1])[0]+ratio
    y1=c.coords(node_list[nodo1-1])[1]+ratio
    x2=c.coords(node_list[nodo2-1])[0]+ratio
    y2=c.coords(node_list[nodo2-1])[1]+ratio

    for i in range(len(connection_list)):
        if nodo1-1==connection_list[i][1] and nodo2-1==connection_list[i][2]:
           return
    connection=c.create_line(x1,y1,x2,y2,width=4,fill="blue")
    list = [connection,nodo1-1,nodo2-1]
    connection_list.append(list)

def move(event):
    i=0
    for node in node_list:
        nodex,nodey =c.coords(node)[0]+ratio,c.coords(node)[1]+ratio
        if abs(nodex-event.x)<ratio and abs(nodey-event.y)<ratio:
            c.coords(node,event.x-ratio,event.y-ratio,event.x+ratio,event.y+ratio)
            c.coords(names_list[i],event.x-ratio+ratio,event.y-ratio-10)
            for connection in connection_list:
                if connection[1]==i:
                    x1 = c.coords(node_list[i])[0] + ratio
                    y1 = c.coords(node_list[i])[1] + ratio
                    x2 = c.coords(connection[0])[2]
                    y2 = c.coords(connection[0])[3]
                    c.coords(connection[0],x1,y1,x2,y2)
                    #break
                elif connection[2]==i:
                    x2 = c.coords(node_list[i])[0] + ratio
                    y2 = c.coords(node_list[i])[1] + ratio
                    x1 = c.coords(connection[0])[0]
                    y1 = c.coords(connection[0])[1]
                    c.coords(connection[0],x1,y1,x2,y2)
                    #print(connection_list)
                    #break
            quality()
            search()
            break
        i=i+1

def delete_connection(connection):
    c.delete(connection[0])
    connection_list.remove(connection)

def quality():
    for connection in connection_list:
        x1 = c.coords(connection[0])[0]
        y1 = c.coords(connection[0])[1]
        x2 = c.coords(connection[0])[2]
        y2 = c.coords(connection[0])[3]
        if sqrt((x2-x1)**2+(y2-y1)**2)>180.0:
            delete_connection(connection)

def search():
    for i in range(len(node_list)):
        for j in range(i + 1, len(node_list)):
            x1 = c.coords(node_list[i])[0]+ratio
            y1 = c.coords(node_list[i])[1]+ratio
            x2 = c.coords(node_list[j])[0]+ratio
            y2 = c.coords(node_list[j])[1]+ratio
            if sqrt((x2-x1)**2+(y2-y1)**2)<120.0:
                create_connection(i+1,j+1)

create_connection(1,2)
create_connection(1,3)
create_connection(2,4)
create_connection(4,5)
create_connection(5,6)
c.bind("<B1-Motion>",move)
window.mainloop()