"""
  Dibujo un triángulo apoyado en el plano XY,
  a partir de un fichero STL
"""

import numpy as np
from fury import window, io, utils, actor

# ------- Constantes
ORIGIN = np.array([0.0, 0.0, 0.0])
LIGHTBLUE = np.array([0.5, 0.5, 1])
YELLOW = np.array([1, 1, 0])
ORANGE = np.array([1, 0.5, 0])
PANTALLA = (600, 400)

# -- Crear el triángulo a partir del fichero stl
polydata = io.load_polydata("triangle.stl")
triangulo = utils.get_actor_from_polydata(polydata)

# -- Establecer el color del triángulo
triangulo.GetProperty().SetColor(ORANGE)

# -- Obtener los vértices del triángulo
# -- Es para dibujarlos también
vertices = utils.get_polydata_vertices(polydata)

# -- Obtener los vértices como un actor para visualizarlo
puntos = actor.point(vertices, point_radius=0.05, colors=YELLOW)

# --- Crear el sistema coordenado
ejes = actor.axes()

# Crear la escena
scene = window.Scene()
scene.add(triangulo)
scene.add(puntos)
scene.add(ejes)

# --- Cambiar la posición de la cámara
cam = scene.GetActiveCamera()
cam.SetPosition(5, -1, 5)
cam.SetViewUp(0, 0, 1)  # -- Eje Z hacia arriba
scene.SetBackground(LIGHTBLUE)
scene.zoom(2)

# ------- Crear la ventana (sin visualizar todavía)
showm = window.ShowManager(scene=scene, size=PANTALLA, reset_camera=False)

# -- Visualizar la escena. Que comience la fiesta!
showm.start()
