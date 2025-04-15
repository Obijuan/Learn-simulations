"""
  Dibujar dos líneas
"""

import numpy as np
from fury import window, actor

# ------- Constantes
ORIGIN = np.array([0.0, 0.0, 0.0])
LIGHTBLUE = np.array([0.5, 0.5, 1])
YELLOW = np.array([1, 1, 0])
ORANGE = np.array([1, 0.5, 0])
MAGENTA = np.array([1, 0, 1])
# -- Tamaño de la ventana
PANTALLA = (600, 400)

# -- Definir los puntos de las dos líneas
lines = [
    np.array([[0, 0, 0], [1, 1, 0]]),  # -- Linea 1
    np.array([[0, 1, 0], [1, 2, 0]])   # -- Linea 2
]

# -- Actor con las líneas
lineas = actor.line(lines, colors=[ORANGE, ORANGE], linewidth=5)

# -- Obtener los puntos de las lineas
puntos0 = actor.point(lines[0], point_radius=0.05, colors=YELLOW)
puntos1 = actor.point(lines[1], point_radius=0.05, colors=MAGENTA)

# Crear la escena
scene = window.Scene()
scene.add(actor.axes())  # -- Ejes
scene.add(lineas)
scene.add(puntos0, puntos1)

# --- Cambiar la posición de la cámara
cam = scene.GetActiveCamera()
cam.SetPosition(5, -1, 5)
cam.SetViewUp(0, 0, 1)  # -- Eje Z hacia arriba
scene.SetBackground(LIGHTBLUE)
scene.zoom(1)

# ------- Crear la ventana (sin visualizar todavía)
showm = window.ShowManager(scene=scene, size=PANTALLA, reset_camera=False)

# -- Visualizar la escena. Que comience la fiesta!
showm.start()
