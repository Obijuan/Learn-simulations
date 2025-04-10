"""
  Poner un Cubo en el origen de color blanco con transparencia
  También un sistema de coordenadas
  Posicionar la cámara
"""

import numpy as np
from fury import actor, window

# ------- Constantes
ORIGEN = np.array([0, 0, 0])

# -- Color blanco con transparencia
WHITE_TRANS = np.array([1, 1, 1, 0.8])

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ------- Construir los objetos a visualizar
centers = np.array([ORIGEN])
colors = np.array([WHITE_TRANS])

# --- Crear los cubos
cubos = actor.cube(centers, colors=colors)

# --- Crear el sistema coordenado
ejes = actor.axes()

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(cubos)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-50, 30, 80)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
