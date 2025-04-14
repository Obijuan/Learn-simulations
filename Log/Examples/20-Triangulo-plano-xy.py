"""
  Dibujo de un triángulo en el plano xy, a partir de sus vértices.
"""

import numpy as np
from fury import window, lib, utils, actor

# ------- Constantes
ORIGIN = np.array([0.0, 0.0, 0.0])
LIGHTBLUE = np.array([0.5, 0.5, 1])
YELLOW = np.array([1, 1, 0])
PANTALLA = (600, 400)

# -- Definir los vértices del triángulo
vertices = np.array(
    [
        [0, 0, 0],  # Vértice 0
        [1, 0, 0],  # Vértice 1
        [0, 1, 0],  # Vertice 2
    ]
)

# -- El triángulo está formado por 3 vértices. El orden determina la normal,
# -- y por tanto qué lado es visible y cuál no
triangles = np.array(
    [
        [0, 1, 2],
    ],
)

# -- En Fury usamos esta clase para crear un objeto a partir de
# -- de sus vértices
polydata = lib.PolyData()

# -- Añadir los vértices y triángulos al objeto
utils.set_polydata_vertices(polydata, vertices)
utils.set_polydata_triangles(polydata, triangles)

# -- Obtener el triángulo listo para usarse
triangulo = utils.get_actor_from_polydata(polydata)

# -- Además del triángulo queremos visualizar los vértices
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
