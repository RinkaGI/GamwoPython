import pygame, sys
from gamwo.input import Input
from pygame.locals import *
import time

class Gamwo:
    '''Main class, this create a window, draw, update, detect input and more, its very important.'''

    def __init__(self, title: str = "Gamwo 2D!", width: int = 800, height: int = 600, target_fps: int = 60):

        '''To main class we have to give
        :param title: Window title
        :type title: str
        :param width: Window width
        :type width: int
        :param height: Window height
        :type height: int
        :return: None
        :rtype: None'''
        self.title = title
        self.width = width
        self.height = height
        self.target_fps = target_fps
        
        pygame.init()

        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        pygame.display.set_caption(self.title)
        pygame.event.set_allowed([QUIT])
        self.window.set_alpha(None)

        self.clock = pygame.time.Clock()

        self.dt = 0
        self.prev_time = time.time()

        self.input = Input()

        self.update_deltatime = 0
        self.draw_handlers = []
        self.update_handlers = []

    def _draw(self):
        for handler in self.draw_handlers:
            handler()

    def _update(self, deltatime):
        for handler in self.update_handlers:
            handler(deltatime)

    def changeBackgroundColor(self, color):
        self.window.fill(color)

    def getFPS(self):
        return self.clock.get_fps()

    def run(self):
        while True:
            self.clock.tick(self.target_fps)

            self.now = time.time()
            self.dt = self.now - self.prev_time
            self.prev_time = self.now

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.input.update()

            self._update(self.dt)
            self.changeBackgroundColor("black")
            self._draw()

            pygame.display.update()
            pygame.display.flip()

    def draw(self, handler):
        self.draw_handlers.append(handler)
        return handler

    def update(self, handler):
        self.update_handlers.append(handler)
        return handler
