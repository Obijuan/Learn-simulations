"""
  Dibujar una textura en el plano suelo (plano xz)
  La textura tiene un tamaño de 1x1
"""

import numpy as np
from fury import actor, window, io

# ------- Constantes
ORIGEN = np.array([0, 0, 0])
YELLOW = np.array([1, 1, 0])
LIGHTBLUE = np.array([0.9, 0.9, 1])
POS_BALDOSA = np.array([1, 0.05, 1])


# -- Nombre de fichero con la textura
# -- Tamaño: 256x256 pixeles
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
# -- El tamaño de la textura es de 256x256, igual que el de la imagen
# -- en píxeles
texture = actor.texture(image)

# -- Como queremos que tenga tamaño de 1x1 lo escalamos
# -- dividiendo por 256
texture.SetScale(1/256, 1/256, 1)

# -- Por defecto la textura se coloca en el plano xy
# -- La queremos en el xy, por lo que rotamos alrededor de x 90 grados
texture.SetOrientation(90, 0, 0)

# --- Crear baldosa 1x1
baldosa_size = np.array([1, 0.1, 1])
centers = np.array([POS_BALDOSA])
colors = np.array([YELLOW])
baldosa = actor.cube(centers, colors=colors, scales=baldosa_size)

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)
scene.add(texture)
scene.add(baldosa)

# --- Cambiar la posición de la cámara
scene.GetActiveCamera().SetPosition(-50, 50, 80)

# --- Cambiar el color del fondo
scene.SetBackground(LIGHTBLUE)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
