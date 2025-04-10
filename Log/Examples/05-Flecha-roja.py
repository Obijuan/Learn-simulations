"""
  Dibujar una flecha roja apuntando hacia el eje X (sentido positivo)
"""

import numpy as np
from fury import actor, window

# ------------------ Constantes
ORIGEN = np.array([0, 0, 0])
EJE_X = np.array([1, 0, 0])

# -- Colores
RED = np.array([1, 0, 0])

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ---- Construir los objetos a visualizar
centers = np.array([ORIGEN])
colors = np.array([RED])
directions = np.array([EJE_X])

# --- Crear la flecha
flecha = actor.arrow(centers, directions, colors)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(flecha)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
