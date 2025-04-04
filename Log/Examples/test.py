import numpy as np
import fury

# --------- Constantes
ORIGEN = np.zeros([1, 3])
BLUE = np.array([0, 0, 1])

# -- Crear un cubo en el origen. Por defecto es un cubo de 1x1x1
# -- y el color es rojo
obj1 = fury.actor.arrow(ORIGEN, (0, 0, 1), colors=BLUE)

# -- Creamos una escena nueva vacia
# -- y añadimos el cubo
scene = fury.window.Scene()
scene.add(obj1)

# -- Mostrar la ventana principal
# -- Por defecto tiene un tamaño de 300x300
fury.window.show(scene)
