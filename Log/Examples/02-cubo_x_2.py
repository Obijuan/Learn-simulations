"""
  Dibujar dos cubos iguales, uno es blanco y el otro rojo, separados una
  distancia de 2 unidades en el eje X.
"""

import numpy as np
import fury

# ------------------ Constantes
ORIGEN = np.zeros([1, 3])

# -- Colores
BLANCO = np.array([1, 1, 1])
RED = np.array([1, 0, 0])
BLUE = np.array([0, 0, 1])

# -- Tamaño de la ventana
PANTALLA = (600, 600)

# ------------------- Construir los objetos a visualizar
# --- Primer cubo
cubo1 = fury.actor.cube(ORIGEN, colors=BLANCO)

# -- Crear el segundo cubo
cubo2 = fury.actor.cube(ORIGEN, colors=RED)
cubo2.SetPosition(2, 0, 0)  # -- Cambiamos la posicion del cubo2


# -----------------  Crear la escena con los elementos
scene = fury.window.Scene()
scene.add(cubo1)
scene.add(cubo2)

# -- Mostrar la ventana principal
# -- Por defecto tiene un tamaño de 300x300
fury.window.show(scene, size=PANTALLA)
