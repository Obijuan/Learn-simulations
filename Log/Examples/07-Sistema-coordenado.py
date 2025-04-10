"""
  Dibujar un sistema de coordenadas en el origen
"""

from fury import actor, window

# -- Tamaño de la ventana
PANTALLA = (600, 400)

# --- Crear el sistema coordenado
ejes = actor.axes()

# --- Crear la escena con los elementos
scene = window.Scene()
scene.add(ejes)

# ---- Crear la ventana
window.show(scene, size=PANTALLA)
