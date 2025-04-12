"""
  Dibujar un suelo en 3D con un sistema de coordenadas
  Cambiar el color del fondo del escenario
"""

import numpy as np
from fury import actor, window

# ------- Constantes
ORIGEN = np.array([0, 0, 0])

# -- Color blanco con transparencia
GREY = np.array([0.6, 0.6, 0.6])

# -- Dimensiones del suelo
GROUND_WIDTH = 5
GROUND_DEPTH = 5
GROUND_HEIGHT = 0.05

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ------- Construir los objetos a visualizar
centers = np.array([ORIGEN])
colors = np.array([GREY])
size = np.array([GROUND_WIDTH, GROUND_HEIGHT, GROUND_DEPTH])

# --- Crear el suelo
suelo = actor.cube(centers, colors=colors, scales=size)
suelo.SetPosition(GROUND_WIDTH/2, -GROUND_HEIGHT/2, GROUND_DEPTH/2)

# --- Crear el sistema coordenado
ejes = actor.axes()

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(suelo)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-50, 50, 80)

# --- Cambiar el color del fondo
scene.SetBackground(1, 1, 1)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
