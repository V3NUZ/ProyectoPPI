import pygame

# Clase del personaje
class personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 1
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

# Funcion para dibujar el personaje
    def dibujar(self, ventana):
       self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
       pygame.draw.rect(ventana, self.color, self.rect)


    