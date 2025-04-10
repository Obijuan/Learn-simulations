"""
  Dibujar dos esferas, una blanca en el origen y otra amarilla
  en la posición (1, 1, 1)
"""

import numpy as np
from fury import actor, window

# -- Constantes
ORIGEN = np.array([0, 0, 0])
PUNTO = np.array([1, 1, 1])
WHITE = np.array([1, 1, 1])
YELLOW = np.array([1, 1, 0])

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# -- Crear las esferas
centers = np.array([ORIGEN, PUNTO])
colors = np.array([WHITE, YELLOW])
esfera1 = actor.sphere(centers, colors, radii=0.1)

# --- Crear el sistema coordenado
ejes = actor.axes()

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(esfera1)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
