from Gamwo import *
import random

screen = Gamwo("Pong", 1280, 960)

# Game rectangles
ball = Entity(screen, "square", 30, 30, screen.width/2 - 15, screen.height/2 - 15, (200, 200, 200))
player = Entity(screen, "square", 10, 140, screen.width - 20, screen.height/2 - 70, (200, 200, 200))
opponent = Entity(screen, "square", 10, 140, 10, screen.height/2 - 70, (200, 200, 200))

# Ball code
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
# Render entities
@screen.draw
def draw():
    screen.changeBackgroundColor("grey12")

    Line(screen, (screen.width/2, 0), (screen.width/2, screen.height), (200, 200, 200))

    ball.show()
    player.show()
    opponent.show()

# Update code
@screen.update
def update():
    global ball_speed_x, ball_speed_y

    def ball_restart():
        global ball_speed_x, ball_speed_y
        ball.center = (screen.width / 2, screen.height / 2)
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen.height:
        ball_speed_y  *= -1
    if ball.left <= 0:
        ball_restart()
    elif ball.right >= screen.width:
        ball_restart()

    if ball.checkCollision(player) or ball.checkCollision(opponent):
        ball_speed_x *= -1

    #################################################################3

    if screen.input.get_key_pressed(screen.input.keys["UP"]):
        player.y -= 7

    if screen.input.get_key_pressed(screen.input.keys["DOWN"]):
        player.y += 7

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen.height:
        player.bottom = screen.height

    ###################################################################33

    if opponent.top < ball.y:
        opponent.top += 7
    if opponent.bottom > ball.y:
        opponent.bottom -= 7

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen.height:
        opponent.bottom = screen.height


screen.run()
