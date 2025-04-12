"""
  Poner una baldosa amarilla de 1x1 en el suelo
"""

import numpy as np
from fury import actor, window

# ------- Constantes
ORIGEN = np.array([0, 0, 0])

# -- Color blanco con transparencia
GREY = np.array([0.6, 0.6, 0.6])
YELLOW = np.array([1, 1, 0])

# -- Dimensiones del suelo
GROUND_WIDTH = 5
GROUND_DEPTH = 5
GROUND_HEIGHT = 0.05

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ------- Construir los objetos a visualizar
centers = np.array([ORIGEN])
ground_colors = np.array([GREY])
ground_size = np.array([GROUND_WIDTH, GROUND_HEIGHT, GROUND_DEPTH])

# --- Crear el suelo
suelo = actor.cube(centers, colors=ground_colors, scales=ground_size)
suelo.SetPosition(GROUND_WIDTH/2, -GROUND_HEIGHT/2, GROUND_DEPTH/2)

# --- Crear el sistema coordenado
ejes = actor.axes()

# -- Crear la baldosa amarilla de 1x1
baldosa_size = np.array([1, 0.1, 1])
centers = np.array([ORIGEN])
baldosa = actor.cube(centers, colors=YELLOW, scales=baldosa_size)

# -- Cambiar la orientación: Rotar 45 grados paralelamente al suelo (Eje y)
baldosa.SetOrientation(0, 40, 0)

# -- Cambiar la posición
baldosa.SetPosition(0.5, 0.05, 0.5)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(suelo)
scene.add(baldosa)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-50, 50, 80)

# --- Cambiar el color del fondo
scene.SetBackground(1, 1, 1)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
