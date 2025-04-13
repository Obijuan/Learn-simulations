"""
  Dibujar una textura en el plano suelo (plano xz)
  La textura tiene un tamaño de 10x10
"""

import numpy as np
from fury import actor, window, io

# ------- Constantes
ORIGEN = np.array([0, 0, 0])
YELLOW = np.array([1, 1, 0])
LIGHTBLUE = np.array([0.9, 0.9, 1])
POS_BALDOSA = np.array([1, 0.05, 1])


# -- Nombre de fichero con la textura
# -- Tamaño: 2560x2560 pixeles
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
showm = window.ShowManager(
    scene=scene, size=PANTALLA,
)


# -- Funcion de retrollamada para realizar la animación
# -- Se ejecuta cada 200 ms
def timer_callback(_obj, _event):

    # -- Girar la baldosa
    baldosa.RotateY(5)

    # -- Actualizar la escena
    showm.render()


# -- Configurar la función de retrollamada
showm.add_timer_callback(True, 200, timer_callback)

# -- Visualizar la escena. Que comience la fiesta!
showm.start()
