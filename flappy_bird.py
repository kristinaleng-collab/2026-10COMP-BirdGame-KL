# start modules
import pgzrun
import pygame
import sys
from random import*

font1 = pygame.font.Font("Fonts/04B_30__.TTF", 40)


# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False 
tick = 0
beep = tone.create('A3', 0.5)
outText = False
start = False
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
class pipe:
    def __init__(self, x, center_y, gap):
        self.x = x
        self.center_y = center_y
        self.gap = gap

        self.top = Actor("top")
        self.bottom = Actor("bottom")

        self.top.x = x
        self.top.y = center_y - (320 + gap / 2)
        self.bottom.x = x
        self.bottom.y = center_y + 320 + gap / 2
pipeslist = [
        pipe(466, 400, 220),
        pipe(732, 180, 220),
        pipe(998, 415, 220)
        ]

# draw everything to screen
def draw():
    if start == False:
        background.draw()
        screen.draw.text("Click the game to start!", center = (400, 300), color = 'black', fontsize = 60)
        startingfont = font1.render("Click the game to start!",True, 'black')
        screen.blit(startingfont, (300, 300))


    else:
        if gameOver == True:
            screen.fill((0, 0, 0))
            screen.draw.text("Game Over!", center=(400, 270), fontsize=60)
            screen.draw.text("Final Score: " + str(score), center=(400, 320), fontsize=40)
            screen.draw.text("High Score: ", center=(400, 370), fontsize=50)

        else:

        # draw background
            background.draw()
        # draw characters
            bird.draw()

        # draw actors
            for pipe in pipeslist:
                drawPipes(pipe)

        scorefont = font1.render(f"{score}", True, 'black')
        screen.blit(scorefont, (400, 20))


def updatePipes(self):
    self.top.x -= 1.5
    self.bottom.x -= 1.5
    if self.top.x < -44:
        self.top.x = 844
        self.bottom.x = 844
        self.gap = randint(160, 260)
        minimum = -200 + (320 // 2) + (self.gap // 2)
        maximum = 800 - ((320 // 2) + (self.gap // 2))
        self.center_y = randint(minimum, maximum)
        self.top.y = self.center_y - (300 + self.gap / 2)
        self.bottom.y = self.center_y + 300 + self.gap / 2
    for pipe in pipeslist:
            for part in [pipe.top, pipe.bottom]:
                if part.colliderect(bird):
                    gameOver = True
        
def drawPipes(self):
    self.top.draw()
    self.bottom.draw()


# update everything
def update():
    global score, gameOver, tick, outText
    if start == False:
        pass
    else:
        if gameOver == True:
            return

    # animate thingy
    tick += 1
    if tick == 31:
        tick = 0
    # update bird
    bird.y = bird.y + 2
    if tick == 15:
        bird.image = "bird_wingsdown"
    elif tick == 30:
        bird.image = "bird_wingsup"
    # update pipes
    for pipe in pipeslist:
        updatePipes(pipe)
        if pipe.top.x == 160:
            score += 1
        if bird.colliderect(pipe.top) or bird.colliderect(pipe.bottom):
            gameOver = True
    # bird hits bottom of screen
    if bird.y > 600 or bird.top < 0:
        gameOver = True
    # bird hits pipes
    
# moving
def on_mouse_down():
    global start
    if start == False:
        start = True
    else:
        bird.y -= 50
        beep.play()

# runs everything
pgzrun.go()