"""
  Situar una baldosa en el plano xz
  Hacer zoom y mostrar la escena
"""

import numpy as np
from fury import actor, window, io

# ------- Constantes
ORIGEN = np.array([0, 0, 0])
YELLOW = np.array([1, 1, 0])
LIGHTBLUE = np.array([0.9, 0.9, 1])

# -- Fichero con la textura de la baldosa
FICHERO = 'ground_grid_10x10.jpg'

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# ------- Construir los objetos a visualizar

# --- Crear el sistema coordenado
ejes = actor.axes()

# -- Cargar imagen de textura
try:
    image = io.load_image(FICHERO)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{FICHERO}'")
    exit()

# -------- Crear la textura
# -- El tamaño de cada cuadrícula de la textura es 256x256
texture = actor.texture(image)

# -- Como queremos que tenga tamaño de 1x1 lo escalamos
# -- dividiendo por 256
texture.SetScale(1/256, 1/256, 1)

# -- Por defecto la textura se coloca en el plano xy
# -- La queremos en el xy, por lo que rotamos alrededor de x 90 grados
texture.SetOrientation(90, 0, 0)

# --- Crear baldosa 1x1
baldosa_size = np.array([1, 0.1, 1])
centers = np.array([ORIGEN])
colors = np.array([YELLOW])
baldosa = actor.cube(centers, colors=colors, scales=baldosa_size)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(texture)
scene.add(baldosa)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-5, 5, 8)

# --- Cambiar el color del fondo
scene.SetBackground(LIGHTBLUE)

# ------- Crear la ventana (sin visualizar todavía)
showm = window.ShowManager(scene=scene, size=PANTALLA)

# -- Modificar el zoom
scene.zoom(5)

# -- Visualizar la escena. Que comience la fiesta!
showm.start()
