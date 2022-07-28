from Gamwo import *
import random

screen = Gamwo("Pong", 1280, 960)

class Ball(Entity):
    def __init__(self, window):
        super().__init__(window, "circle", 30, 30, window.width/2-15, window.height/2-15, (200, 200, 200))
        self.ballSpeedX = 7 * random.choice((1, -1))
        self.ballSpeedY = 7 * random.choice((1, -1))

    def movement(self):
        self.x += self.ballSpeedX
        self.y += self.ballSpeedY

        if self.top <= 0 or self.bottom >= self.window.height:
            self.ballSpeedY *= -1
        if self.left <= 0:
            self.respawn()
        elif self.right >= self.window.width:
            self.respawn()

        if self.checkCollision(player) or self.checkCollision(opponent):
            self.ballSpeedX *= -1

    def respawn(self):
        self.center = (self.window.width / 2, self.window.height / 2)
        self.ballSpeedY *= random.choice((1, -1))
        self.ballSpeedX *= random.choice((1, -1))

    def render(self):
        self.show()

class Paddle(Entity):
    def __init__(self, window, player):
        if player == 'player':
            super().__init__(window, "square", 10, 140, window.width - 20, window.height/2 - 70, (200, 200, 200))
        elif player == 'opponent':
            super().__init__(window, 'square', 10, 140, 10, window.height/2 - 70, (200, 200, 200))

        self.window = window
        self.player = player

    def movement(self):
        if self.player == 'player':
            if self.window.input.get_key_pressed(self.window.input.keys["UP"]):
                self.y -= 7
            if self.window.input.get_key_pressed(self.window.input.keys["DOWN"]):
                self.y += 7
        elif self.player == 'opponent':
            if self.y <= ball.y:
                self.y += 7
            elif self.y >= ball.y:
                self.y -= 7

        
        if self.top <= 0:
            self.top = 0
        if self.bottom >= self.window.height:
            self.bottom = self.window.height
        self.show()

ball = Ball(screen)
player = Paddle(screen, 'player')
opponent = Paddle(screen, 'opponent')

@screen.draw
def draw():
    screen.changeBackgroundColor("grey12")

    Line(screen, (screen.width/2, 0), (screen.width/2, screen.height), (200, 200, 200))

    ball.render()
    player.show()
    opponent.show()

@screen.update
def update():
    ball.movement()
    player.movement()
    opponent.movement()


screen.run() 
