import cv2
import numpy as np
import random


# Configuración de la imagen
width, height = 800, 350
img = np.zeros((height, width, 3), dtype=np.uint8)

# Configuración de la función seno
amplitude_x = 3
frequency_x = 0.1  # Frecuencia de la onda seno en el eje x

amplitude_y = 5
frequency_y = 0.5  # Frecuencia de la onda seno en el eje y

# Dibujar la función seno repetidas veces en el eje x y el eje y
for y in range(0, height, 20):  # Incremento de 80 píxeles en el eje y
    for x in range(width):
        y_value = int(amplitude_y * np.sin(frequency_y * x) + y)
        x_value = int(amplitude_x * np.cos(frequency_x * y) + x)
        cv2.circle(img, (x_value, y_value), 1, (255, 255, 0), -1)


        # Agregar aleatoriedad a la posición de los puntos
    if random.random() < 0.001:  # Probabilidad del 8% de dibujar un punto
        cv2.circle(img, (x_value, y_value), 10, (255, 255, 255), -1)
# Mostrar la imagen
cv2.imshow('Función Seno Repetida en el Eje X e Y', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
