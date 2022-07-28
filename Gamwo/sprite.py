import pygame

class Sprite:
    def __init__(self, window, picture: str, x = 0, y = 0, width: int = 200, height: int = 200):
        self.window = window
        self.picture = picture
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.image.load(self.picture)
        self.rect = pygame.Rect(0, 0, 0, 0)

        if width != None and height != None:
            self.image =  pygame.transform.scale(self.image, (width, height))

    def show(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.window.window.blit(self.image, (self.x, self.y))

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()

    def checkCollision(self, second_entity):
        try:
            if type(second_entity) != list:
                return self.rect.colliderect(second_entity.rect)
            elif type(second_entity) == list:
                return self.rect.collidelistall(second_entity.rect)
        except:
            raise AttributeError("Gamwo.Sprite.checkCollision: second_entity must be a Gamwo.Entity or a list of Gamwo.Entity or Gamwo.Sprite or a list of Gamwo.Sprite")
