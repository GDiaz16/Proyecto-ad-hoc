from skimage import io, color
import numpy as np
img = io.imread('pikachu.jpg')
img = np.array(img)

ancho = img.shape[1]
alto = img.shape[0]
i = 1
j = 1
filas = 2
columnas = 3
for i in range(filas):
    for j in  range(columnas):
        img2 = img[(alto//filas)*i:(alto//filas)*(i+1),(ancho//columnas)*j:(ancho//columnas)*(j+1),:]
        io.imshow(img2)
        io.show()
        print(f"{i} {j}")

#img = img[(alto//filas)*i:(alto//filas)*(i+1),(ancho//columnas)*j:(ancho//columnas)*(j+1),:]

print (img.shape)
#io.imshow(img)
#io.show()

