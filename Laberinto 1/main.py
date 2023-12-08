import pygame
import sys

# Dimensiones del laberinto (ancho y alto)
ANCHO = 600
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)  # Color azul
ROJO = (255, 0, 0)  # Color rojo
AMARILLO = (255, 255, 0)  # Color amarillo

# Laberinto
laberinto = [
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [0,1,0,1,0,0,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]
]

def dibujar_laberinto():
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == 0:
                pygame.draw.rect(screen, NEGRO, (columna * 40, fila * 40, 40, 40))
            else:
                pygame.draw.rect(screen, BLANCO, (columna * 40, fila * 40, 40, 40))

    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (3 * 40, 14 * 40, 40, 40))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (14 * 40, 1 * 40, 40, 40))

    # Dibujar el punto amarillo en la posición actual
    pygame.draw.rect(screen, AMARILLO, (posicion_x, posicion_y, 40, 40))
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto")

reloj = pygame.time.Clock()

# Coordenadas iniciales del punto amarillo (entrada)
posicion_x = 3 * 40
posicion_y = 14 * 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if posicion_x - 40 >= 0 and laberinto[posicion_y // 40][posicion_x // 40 - 1] == 1:
                    posicion_x -= 40
            elif event.key == pygame.K_RIGHT:
                if posicion_x + 40 < ANCHO and laberinto[posicion_y // 40][posicion_x // 40 + 1] == 1:
                    posicion_x += 40
            elif event.key == pygame.K_UP:
                if posicion_y - 40 >= 0 and laberinto[posicion_y // 40 - 1][posicion_x // 40] == 1:
                    posicion_y -= 40
            elif event.key == pygame.K_DOWN:
                if posicion_y + 40 < ALTO and laberinto[posicion_y // 40 + 1][posicion_x // 40] == 1:
                    posicion_y += 40

    dibujar_laberinto()
    reloj.tick(60)

    # Verificar si el cuadro amarillo llega al cuadro rojo
    if (posicion_x // 40, posicion_y // 40) == (14, 1):
        print("¡Laberinto resuelto!")