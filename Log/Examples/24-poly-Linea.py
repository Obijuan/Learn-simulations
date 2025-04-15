"""
  Dibujar una poly-línea en el plano xy
"""

import numpy as np
from fury import window, actor

# ------- Constantes
ORIGIN = np.array([0.0, 0.0, 0.0])
LIGHTBLUE = np.array([0.5, 0.5, 1])
YELLOW = np.array([1, 1, 0])
ORANGE = np.array([1, 0.5, 0])
PANTALLA = (600, 400)

# -- Definir todos los puntos de la poli-linea
lines = [np.array([[0, 0, 0], [1, 1, 0], [1, 1, 1], [1, 2, 1]])]
linea = actor.line(lines, colors=[ORANGE], linewidth=5)

# -- Dibujar los puntos de la poli-línea
puntos = actor.point(lines[0], point_radius=0.05, colors=YELLOW)

# Crear la escena
scene = window.Scene()
scene.add(actor.axes())  # -- Ejes
scene.add(linea)
scene.add(puntos)

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
