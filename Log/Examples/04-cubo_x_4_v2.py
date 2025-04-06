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
ORIGEN = np.array([0, 0, 0])
POS_EJEX = np.array([2, 0, 0])
POS_EJEY = np.array([0, 2, 0])
POS_EJEZ = np.array([0, 0, 2])

# -- Colores
WHITE = np.array([1, 1, 1])
RED = np.array([1, 0, 0])
GREEN = np.array([0, 1, 0])
BLUE = np.array([0, 0, 1])

# -- Tamaño de la ventana
PANTALLA = (600, 600)

# ---- Construir los objetos a visualizar
# -- Array2 con las posiciones de los cubos y sus colores
#                   Cubo 1   Cubo 2     Cubo 3   Cubo 4
centers = np.array([ORIGEN, POS_EJEX, POS_EJEY, POS_EJEZ])
colors = np.array([WHITE,   RED,      GREEN,    BLUE])

# --- Crear los cubos
cubos = actor.cube(centers, colors=colors)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(cubos)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
