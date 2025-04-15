"""
  Dibujar un grid de 10x10 líneas
"""

import numpy as np
from fury import window, actor

# ------- Constantes
ORIGIN = np.array([0.0, 0.0, 0.0])
GREEN = np.array([0, 1, 0])

# -- Semi-longitud de las líneas
L = 10

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# -- Definir los puntos de las dos líneas
lines = [
    # -- Lineas horizontales
    np.array([[-L, -10, 0], [L, -10, 0]]),
    np.array([[-L, -9, 0], [L, -9, 0]]),
    np.array([[-L, -8, 0], [L, -8, 0]]),
    np.array([[-L, -7, 0], [L, -7, 0]]),
    np.array([[-L, -6, 0], [L, -6, 0]]),
    np.array([[-L, -5, 0], [L, -5, 0]]),
    np.array([[-L, -4, 0], [L, -4, 0]]),
    np.array([[-L, -3, 0], [L, -3, 0]]),
    np.array([[-L, -2, 0], [L, -2, 0]]),
    np.array([[-L, -1, 0], [L, -1, 0]]),
    np.array([[-L,  0, 0], [L,  0, 0]]),
    np.array([[-L,  1, 0], [L,  1, 0]]),
    np.array([[-L,  2, 0], [L,  2, 0]]),
    np.array([[-L,  3, 0], [L,  3, 0]]),
    np.array([[-L,  4, 0], [L,  4, 0]]),
    np.array([[-L,  5, 0], [L,  5, 0]]),
    np.array([[-L,  6, 0], [L,  6, 0]]),
    np.array([[-L,  7, 0], [L,  7, 0]]),
    np.array([[-L,  8, 0], [L,  8, 0]]),
    np.array([[-L,  9, 0], [L,  9, 0]]),
    np.array([[-L, 10, 0], [L, 10, 0]]),

    # -- Lineas verticales
    np.array([[-10, -L, 0], [-10, L, 0]]),
    np.array([[-9, -L, 0], [-9, L, 0]]),
    np.array([[-8, -L, 0], [-8, L, 0]]),
    np.array([[-7, -L, 0], [-7, L, 0]]),
    np.array([[-6, -L, 0], [-6, L, 0]]),
    np.array([[-5, -L, 0], [-5, L, 0]]),
    np.array([[-4, -L, 0], [-4, L, 0]]),
    np.array([[-3, -L, 0], [-3, L, 0]]),
    np.array([[-2, -L, 0], [-2, L, 0]]),
    np.array([[-1, -L, 0], [-1, L, 0]]),
    np.array([[0, -L, 0], [0, L, 0]]),
    np.array([[1, -L, 0], [1, L, 0]]),
    np.array([[2, -L, 0], [2, L, 0]]),
    np.array([[3, -L, 0], [3, L, 0]]),
    np.array([[4, -L, 0], [4, L, 0]]),
    np.array([[5, -L, 0], [5, L, 0]]),
    np.array([[6, -L, 0], [6, L, 0]]),
    np.array([[7, -L, 0], [7, L, 0]]),
    np.array([[8, -L, 0], [8, L, 0]]),
    np.array([[9, -L, 0], [9, L, 0]]),
    np.array([[10, -L, 0], [10, L, 0]]),
]

# -- Actor con las líneas
lineas = actor.line(lines, colors=[GREEN]*len(lines), linewidth=3)

# Crear la escena
scene = window.Scene()
scene.add(actor.axes())  # -- Ejes
scene.add(lineas)

# --- Cambiar la posición de la cámara
cam = scene.GetActiveCamera()
cam.SetPosition(5, -1, 5)
cam.SetViewUp(0, 0, 1)  # -- Eje Z hacia arriba
scene.zoom(1)

# ------- Crear la ventana (sin visualizar todavía)
showm = window.ShowManager(scene=scene, size=PANTALLA, reset_camera=False)

# -- Visualizar la escena. Que comience la fiesta!
showm.start()
