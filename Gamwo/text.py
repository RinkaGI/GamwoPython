import pygame, sys

class Text:
    def __init__(self, window, text: str, fontFile = None, fontSize: int = 20, x = 0, y = 0, color = "white") -> None:
        self.window = window
        self.text = text
        self.fontFile = fontFile
        self.fontSize = fontSize
        self.x = x
        self.y = y
        self.color = color

        if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "win32" or sys.platform == "cygwin":
            self.font = pygame.font.SysFont(self.fontFile, self.fontSize)
        else:
            self.font = pygame.font.Font(self.fontFile, self.fontSize)

        self.text = self.font.render(self.text, True, self.color)

    def show(self):
        self.window.window.blit(self.text, (self.x, self.y))
        
