import pygame, sys

class Line:
    def __init__(self, window, start, end, color) -> None:
        self.window = window
        self.start = start
        self.end = end
        self.color = color

        pygame.draw.aaline(self.window.window, self.color, self.start, self.end)
