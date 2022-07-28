import pygame, sys

class Entity(pygame.Rect):
    def __init__(self, window, shape = "square", width = 20, height = 20, x = 0, y = 0, color = "white"):
        self.window = window
        self.shape = shape
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        
    def show(self):
        if self.shape == "square" or self.shape == "rect" or self.shape == "rectangle":
            pygame.draw.rect(self.window.window, self.color, self)
        elif self.shape == "ellipse" or self.shape == "circle":
            pygame.draw.ellipse(self.window.window, self.color, self)

    def checkCollision(self, second_entity):
        try:
            if type(second_entity) != list:
                return self.colliderect(second_entity)
            elif type(second_entity) == list:
                return self.collidelistall(second_entity)
        except:
            raise AttributeError("Gamwo.Entity.checkCollision: second_entity must be a Gamwo.Entity or a list of Gamwo.Entity")
