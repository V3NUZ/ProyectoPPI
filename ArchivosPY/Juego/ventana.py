import pygame
from personaje import personaje

# Inicializar ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])

jugando = True

# Crear personaje  de la clase personaje
personaje = personaje(100, 100)

# Funcion para gestionar el movimiento del personaje
def gestionar_movimiento(teclas):
    if teclas[pygame.K_w]:
        personaje.y -= personaje.velocidad
    if teclas[pygame.K_s]:
        personaje.y += personaje.velocidad
    if teclas[pygame.K_a]:
        personaje.x -= personaje.velocidad
    if teclas[pygame.K_d]:
        personaje.x += personaje.velocidad

# Bucle principal
while jugando:
    
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_movimiento(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

# Dibujar personaje
    VENTANA.fill((0, 0, 0))
    personaje.dibujar(VENTANA)
    pygame.display.update()

# Salir del juego
pygame.quit()