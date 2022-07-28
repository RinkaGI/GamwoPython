import pygame, sys
from Gamwo.input import Input

class Gamwo:
    '''Main class, this create a window, draw, update, detect input and more, its very important.'''

    def __init__(self, title: str = "Gamwo 2D!", width: int = 800, height: int = 600):

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
        
        pygame.init()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.input = Input()

        self.draw_handlers = []
        self.update_handlers = []

    def _draw(self):
        for handler in self.draw_handlers:
            handler()

    def _update(self):
        for handler in self.update_handlers:
            handler()

    def changeBackgroundColor(self, color):
        self.window.fill(color)

    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.input.update()
            self._update()
            self._draw()

            pygame.display.flip()
            self.clock.tick(60)

    def draw(self, handler):
        self.draw_handlers.append(handler)

    def update(self, handler):
        self.update_handlers.append(handler)
