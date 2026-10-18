# Kristina Leng

# start modules
import pgzrun
import sys
from random import Random
# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False

# print welcome
print('Welcome!\nThe game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')
# make background
background = Actor("bg")
background.x = 400
background.y = 300
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300
# make pipes
class pipes():
    def __init__(self, x, center_y, gap):
        self.center_y = center_y
        self.x = x
        self.gap = gap

        self.top = Actor("top")
        self.bottom = Actor("bottom")

        self.top.x = x
        self.top.y = center_y - (300 + 110)

        self.bottom.x = x
        self.bottom.y = center_y + 300 + 110

PipesList = [
    pipes(266, 400, 220),
    pipes(532, 180, 220),
    pipes(798, 415, 220)
] 

# draw everything to screen
def draw(): 

    # Creating gameOver Screen
    if gameOver == True:
        screen.fill((0, 0, 0))
        screen.draw.text("Game Over!" ,  center = (400,300), fontsize = 75)
        screen.draw.text("Final Score: " +str(score), center = (400, 370), fontsize = 55)
    else:

    # draw background
        background.draw()

    # draw characters
        bird.draw()
    # draw actors
        for pipes in PipesList:
            pipes.top.draw()
            pipes.bottom.draw()


# update everything
def update():
    global score, gameOver
    if gameOver == True:
        return
    
    # update bird
    bird.y = bird.y + 1

    # update pipes
    for pipes in PipesList:
        pipes.top.x -= 1
        pipes.bottom.x -= 1
        if pipes.top.x < -44:
            pipes.top.x = 844
            pipes.bottom.x = 844

    # bird hits bottom of screen
        if bird.y > 600:
            print("Game Over!")
            gameOver = True
    # bird hits pipes
        if bird.colliderect (pipes.top):
            print("Hit!\nGame Over!")
            gameOver = True
        if bird.colliderect (pipes.bottom):
            print("Hit!\nGame Over!")
            gameOver = True

        # creating gameOver
    if bird.colliderect (pipes.top) or bird.colliderect (pipes.bottom) or bird.bottom > 600 or bird.top < 0:
        gameOver = True

        # update score
    if pipes.top.x >= -44:
        score = score + 1


# moving
def on_mouse_down():
    bird.y -= 50
# runs everything
pgzrun.go()