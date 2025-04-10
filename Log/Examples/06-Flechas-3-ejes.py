"""
  Dibujar tres flechas, en los tres ejes, de diferentes colores
"""

import numpy as np
from fury import actor, window

# ------------------ Constantes
ORIGEN = np.array([0, 0, 0])
EJE_X = np.array([1, 0, 0])
EJE_Y = np.array([0, 1, 0])
EJE_Z = np.array([0, 0, 1])

# -- Colores
RED = np.array([1, 0, 0])
GREEN = np.array([0, 1, 0])
BLUE = np.array([0, 0, 1])

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ---- Construir las flechas
centers = np.array([ORIGEN, ORIGEN, ORIGEN])
colors = np.array([RED, GREEN, BLUE])
directions = np.array([EJE_X, EJE_Y, EJE_Z])

# --- Crear las flechas
flecha = actor.arrow(centers, directions, colors)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(flecha)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
