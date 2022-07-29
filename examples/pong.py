from gamwo import *
import random


screen = Gamwo("Pong", 800, 600)

class Ball(Entity):
        def __init__(self, window):
            super().__init__(window, "circle", 30, 30, window.width/2-15, window.height/2-15, (200, 200, 200))
            self.window = window

            self.ballSpeedX = 450 * random.choice((1, -1))
            self.ballSpeedY = 450 * random.choice((1, -1))

        def movement(self, dt):
            self.x += self.ballSpeedX  * dt
            self.y += self.ballSpeedY  * dt

            if self.top <= 0 or self.bottom >= self.window.height:
                self.ballSpeedY *= -1
            if self.left <= 0:
                player.player_counter += 1
                self.respawn()
            elif self.right >= self.window.width:
                opponent.opponent_counter += 1
                self.respawn()

            if self.checkCollision(player) or self.checkCollision(opponent):
                self.ballSpeedX *= -1


        def respawn(self):
            self.center = (self.window.width / 2, self.window.height / 2)
            self.ballSpeedY *= random.choice((1, -1))
            self.ballSpeedX *= random.choice((1, -1))

class Paddle(Entity):
        def __init__(self, window, player):
            if player == 'player':
                super().__init__(window, "square", 10, 140, window.width - 20, window.height/2 - 70, (200, 200, 200))
            elif player == 'opponent':
                super().__init__(window, 'square', 10, 140, 10, window.height/2 - 70, (200, 200, 200))

            self.window = window
            self.player = player

            self.player_counter = 0
            self.opponent_counter = 0

        def movement(self, dt):
            if self.player == 'player':
                if self.window.input.get_key_pressed(self.window.input.keys["UP"]):
                    self.y -= 450 * dt
                if self.window.input.get_key_pressed(self.window.input.keys["DOWN"]):
                    self.y += 450 * dt
            elif self.player == 'opponent':
                if self.y <= ball.y:
                    self.y += 450 * dt
                elif self.y >= ball.y:
                    self.y -= 450 * dt

            if self.top <= 0:
                self.top = 0
            if self.bottom >= self.window.height:
                self.bottom = self.window.height

ball = Ball(screen)
player = Paddle(screen, 'player')
opponent = Paddle(screen, 'opponent')

@screen.draw
def draw():
        player_text = Text(screen, "Player: " + str(player.player_counter), "Arial", 20, screen.width / 2 + 20, screen.height / 2 - 10, "cyan").show()
        opponent_text = Text(screen, "Opponent: " + str(opponent.opponent_counter), "Arial", 20, screen.width / 2 + 20, screen.height / 2 + 10, "cyan").show()

        Line(screen, (screen.width / 2, 0), (screen.width / 2, screen.height), "white")

        Text(screen, f"FPS: {str(int(screen.getFPS()))}").show()
        ball.show()
        player.show()
        opponent.show()

@screen.update
def update(dt):
        ball.movement(dt)
        player.movement(dt)
        opponent.movement(dt)

screen.run()
