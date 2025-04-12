"""
  Array NxM de baldosas 1x1 en el suelo
  Los colores de las baldosas forman un patrón de ajedrez
  de colores blanco y amarillo
"""

import numpy as np
from fury import actor, window

# ------- Constantes
ORIGEN = np.array([0, 0, 0])

# -- Color blanco con transparencia
GREY = np.array([0.6, 0.6, 0.6])
YELLOW = np.array([1, 1, 0])
WHITE = np.array([1, 1, 1])
LIGHTBLUE = np.array([0.5, 0.5, 1])

# -- Numero de baldosas (N x M)
N = 5
M = 5

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ------- Construir los objetos a visualizar

# --- Crear el sistema coordenado
ejes = actor.axes()

# --- Crear las baldosas amarilla de 1x1
baldosa_size = np.array([1, 0.1, 1])
centers = np.array([[i, 0, j] for i in range(N) for j in range(M)])

# -- Color: Patron de ajedrez (Amarillo y blanco)
colors = np.array([WHITE if (i+j) % 2 else YELLOW
                   for i in range(N)
                   for j in range(M)])

baldosas = actor.cube(centers, colors=colors, scales=baldosa_size)

# -- Bajar las baldosas para que el origen esté a ras del suelo
baldosas.SetPosition(0, -0.05, 0)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(baldosas)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-50, 50, 80)

# --- Cambiar el color del fondo
scene.SetBackground(LIGHTBLUE)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
