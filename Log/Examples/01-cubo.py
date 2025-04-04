import numpy as np
import fury

# --------- Constantes
ORIGEN = np.zeros([1, 3])

# -- Crear un cubo en el origen. Por defecto es un cubo de 1x1x1
# -- y el color es rojo
cubo = fury.actor.cube(ORIGEN)

# -- Creamos una escena nueva vacia
# -- y añadimos el cubo
scene = fury.window.Scene()
scene.add(cubo)

# -- Mostrar la ventana principal
# -- Por defecto tiene un tamaño de 300x300
fury.window.show(scene)
