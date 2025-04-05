"""
  Dibujar cuatro cubos iguales:
  * Cubo 1: (BLANCO) en el origen
  * Cubo 2: (ROJO) en el eje X (2,0,0)
  * Cubo 3: (VERDE) en el eje Y (0,2,0)
  * Cubo 4: (AZUL) en el eje Z (0,0,2)
"""

import numpy as np
from fury import actor, window

# ------------------ Constantes
ORIGEN = np.zeros([1, 3])

# -- Colores
WHITE = np.array([1, 1, 1])
RED = np.array([1, 0, 0])
GREEN = np.array([0, 1, 0])
BLUE = np.array([0, 0, 1])

# -- Tamaño de la ventana
PANTALLA = (600, 600)

# ------------------- Construir los objetos a visualizar
# --- Crear los cubos
cubo1 = actor.cube(ORIGEN, colors=WHITE)
cubo2 = actor.cube(ORIGEN, colors=RED)
cubo3 = actor.cube(ORIGEN, colors=GREEN)
cubo4 = actor.cube(ORIGEN, colors=BLUE)

# --- Posicionar los cubos
cubo2.SetPosition(2, 0, 0)  # Cubo en el eje X
cubo3.SetPosition(0, 2, 0)  # Cubo en el eje Y
cubo4.SetPosition(0, 0, 2)  # Cubo en el eje Z

# -----------------  Crear la escena con los elementos
scene = window.Scene()
scene.add(cubo1)
scene.add(cubo2)
scene.add(cubo3)
scene.add(cubo4)

# ----------------- Crear la ventana
# -- Mostrar la ventana principal
# -- Por defecto tiene un tamaño de 300x300
window.show(scene, size=PANTALLA)
