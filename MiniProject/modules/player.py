import pygame
import random
import time
import sys
from pygame.locals import *
# from pygame.locals import *

pygame.font.init()
pygame.init()

#setting screen dimensions:
screen = pygame.display.set_mode((1024,650))

#setting caption. displays top of the screen:
pygame.display.set_caption("Cricket Zone")

# assingning batsman image
batsman = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/player1.png')

# loading batsman image before short:
batsman_short = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/short_batsman.png')

#setting icon at top
pygame.display.set_icon(batsman)

# loading ball image in ball variable
ball = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/ball.png')

# loading pitch image in pitch variable
pitch = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/pitch.png')

# loading bold image
bg_bold = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/pitch_bold.png')

# loading wide image
bg_wide = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/wide.png')

# loading no run image
bg_nr = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/NoRun.png')

# declaring variables which decides the path of ball after short

x_direction = 0
y_direction = 0

# loading images for screen change animation
bg_br = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/be_ready.png')
countdown3 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/ready_3.png')
countdown2 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/ready_2.png')
countdown1 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/ready_1.png')
SwitchScreen = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/lets_play.png')

# loading images for loading animation
bg_load1 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading.png')
bg_load2 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading1.png')
bg_load3 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading2.png')
bg_load4 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading3.png')
bg_load5 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading4.png')
bg_load6 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/loading5.png')

# creating scoreboard

score_board = 0
font = pygame.font.SysFont('freesansbold.ttf',50)
font2 = pygame.font.SysFont('freesansbold.ttf',30)


def Score_Update(x,y):
    score_display = font.render(str(score_board),True,(255,255,255))
    screen.blit(score_display,(x,y))

def BallSpeed_display(x):
    if x==0:
        speed_display = font.render("N/A",True,(0,0,0))
        screen.blit(speed_display,(945,607))
        pygame.display.update()
    else:
        s= str(x)+" km/h"
        speed_display = font2.render(s,True,(0,0,0))
        screen.blit(speed_display,(945,607))




def balling(p,q):
    screen.blit(ball,(p,q))

def player(x,y):
    screen.blit(batsman,(x,y))

def display_pitch():
    screen.blit(pitch,(0,0))


def bold():
     x = True
     screen.fill((0,0,0))

     while x:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 x=False
         screen.blit(bg_bold,(0,0))
         player(480,10)
         pygame.display.update()
         time.sleep(3)
         x = False

def wide():
     x = True
     screen.fill((0,0,0))
     while x:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 x=False
         screen.blit(bg_wide,(0,0))
         pygame.display.update()
         time.sleep(2)
         x = False

def No_Run():
     x = True
     screen.fill((0,0,0))
     while x:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 x=False
         screen.blit(bg_nr,(0,0))
         pygame.display.update()
         time.sleep(2)
         x = False

def short(x,y,px,py):
    global x_direction
    global y_direction
    x_direction = random.randint(-20,20)
    y_direction = random.randint(-10,10)
    while x>=-50 and x<=1040 and y>=-50 and y<=680:
        x += x_direction
        y += y_direction
        display_pitch()
        screen.blit(batsman_short,(px,py))
        screen.blit(ball,(x,y))
        pygame.display.update()
    time.sleep(1)

def ready_animation():
    screen.fill((0,0,0))
    screen.blit(bg_br,(0,0))
    pygame.display.update()
    time.sleep(0.7)
    screen.blit(countdown3,(0,0))
    pygame.display.update()
    time.sleep(0.7)
    screen.blit(countdown2,(0,0))
    pygame.display.update()
    time.sleep(0.7)
    screen.blit(countdown1,(0,0))
    pygame.display.update()
    time.sleep(0.7)
    screen.blit(SwitchScreen,(0,0))
    pygame.display.update()
    time.sleep(1)

def loading_animation():
    screen.blit(bg_load1,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(bg_load2,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(bg_load3,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(bg_load4,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(bg_load5,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(bg_load6,(0,0))
    pygame.display.update()
    time.sleep(1)

def check():
    x = True
    while x:

     screen.blit(pitch,(0,0))
     screen.blit(batsman,(450,-20))
     pygame.display.update()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             x = False
             pygame.quit()
