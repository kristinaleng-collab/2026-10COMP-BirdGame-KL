# Kristina Leng

# start modules
import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
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
class Pipes():
    def __init__(self, x, center_y, gap):
        self.center_y = center_y
        self.x = x
        self.gap = gap

        self.top = Actor("top")
        self.bottom = Actor("bottom")

        self.top.x = x
        self.top.y = center_y - (150 + 110)

        self.bottom.x = x
        self.bottom.y = center_y + 150 + 110

# draw everything to screen
def draw(): 
    # draw background
    background.draw()
    # draw characters
    bird.draw()
# update everything
def update():
    bird.y = bird.y + 1
    # update bird

    # update pipes

    # bird hits bottom of screen
    if bird.y > 600:
        print("Game Over!")
        sys.exit()
    # bird hits pipes

# moving
def on_mouse_down():
    bird.y -= 50
# runs everything
pgzrun.go()