import player
import pygame
import time
import random
import ranking
import math
from pygame.locals import *
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1024,650))

bg_FirstInterface = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/interface1.png')
bg_about = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/about_page.png')

# importing images for decision pending ready_animation
dp_1 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_1.png')
dp_2 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_2.png')
dp_3 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_3.png')
dp_4 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_4.png')
dp_5 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_5.png')
dp_6 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_6.png')
dp_7 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_7.png')
dp_8 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_8.png')
dp_9 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_9.png')
dp_10 = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/dp_10.png')

# sort execution
run_execution = 0
font = pygame.font.SysFont('freesansbold.ttf',50)

def Run_Update(x,y):
    run_display = font.render(str(run_display),True,(255,255,255))
    screen.blit(score_display,(x,y))

# importing scoreboard images

one_run = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/one_run.png')
two_run = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/two_run.png')
three_run = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/three_run.png')
four_run = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/four_run.png')
six_run = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/six_run.png')


# declaring variables to update statistics and score_board
bg_statistics = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/statistics.png')
total_balls = 0
fours_count = 0
six_count = 0
speed = 2

def gameloop():
 global speed
 global total_balls
 global fours_count
 global six_count
 total_balls+=1
 player.ready_animation()
 '''
 player.Score_Update(150,290)
 pygame.display.update()'''

 played = 0
 #defining initial position of player
 px = 450
 py = -20
 #defining initial position of player
 bx=430
 by=650
 x=True

 turn = random.randint(-5,5)
 speed=random.randint(5,15)
 turn = float(turn/4)
 while x:
    screen.fill((0,0,0))

    by-=speed
    bx+=turn
    # condition of ball hitting stumps:
    '''
    if by <= 55 and bx >= 463 and bx <= 536:
    '''
    if by <=70 and bx>= 470 and bx <= 527:
        player.bold()
        x = False
        break

    # condition of ball getting wide:
    if  (by<=50 and bx<=310) or (by<=50 and bx>=620):
        player.wide()
        player.score_board+=1
        gameloop()
        break

    # condition of missing ball:
    if by < 1:
        player.No_Run()
        gameloop()
        x=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          x = False
         # KEYDOWN type means that any of the key is pressed by user:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              if (bx>=350 and bx<=650) and (by>=70 and by<=150):
                player.short(bx,by,px,py)
                run_decider = random.randint(1,5)
                short_output(run_decider)
                if run_decider!=5:
                 if run_decider==4:
                     fours_count+=1
                 player.score_board+=run_decider
                else:
                  six_count+=1
                  player.score_board+=6
                gameloop()
                played = 1
                x = False
                continue
              else:
               played = 1
               continue
          if event.key == pygame.K_RIGHT:
              px+=4
          if event.key == pygame.K_LEFT:
              px-=4
    player.display_pitch()
    if played==1:
     screen.blit(player.batsman_short,(px,py))
    else:
     player.player(px,py)
    if x==True:
     player.balling(bx,by)
    player.Score_Update(150,600)
    if total_balls>1:
         player.BallSpeed_display(100+(speed*3))
    else:
         player.BallSpeed_display(0)
    pygame.display.update()
 #if x==False:
 '''
 if total_balls>1:
      player.BallSpeed_display(random.randint(90,156))
      pygame.display.update()
 else:
      player.BallSpeed_display(0)
      pygame.display.update()
      #statistics()
'''

def statistics():
    global total_balls
    global fours_count
    global six_count
    x = True
    while x:
        screen.blit(bg_statistics,(0,0))
        font = pygame.font.SysFont('freesansbold.ttf',80)
        your_score = str(player.score_board)+"("+str(total_balls)+")"
        your_score_display = font.render(your_score,True,(0,0,0))
        screen.blit(your_score_display,(620,80))
        font = pygame.font.SysFont('freesansbold.ttf',40)
        run_rate=player.score_board/total_balls
        run_rate = round(run_rate,3)
        rr_display = font.render(str(run_rate),True,(0,0,0))
        screen.blit(rr_display,(580,330))
        fours_display = font.render(str(fours_count),True,(0,0,0))
        screen.blit(fours_display,(580,400))
        sixes_display = font.render(str(six_count),True,(0,0,0))
        screen.blit(sixes_display,(580,480))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 x = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    x = False
                    total_balls = fours_count = six_count =  0





def mainloop():
    player.loading_animation()
    first_interface()


def first_interface():
    x = True
    while x:
      screen.blit(bg_FirstInterface,(0,0))
      pygame.display.update()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              x = False
              pygame.quit()
          if event.type == pygame.KEYDOWN:
              '''
              if event.key == pygame.K_1:
                  # play game
                  '''
              if event.key == pygame.K_2:
                  # Icc ranking
                  check = 0
                  check = ranking.ranking_loop()
                  if check == 1:
                   first_interface()
                   check = 0
              if event.key == pygame.K_3:
                  # about
                  about_screen()
              if event.key == pygame.K_0:
                  x = False
                  pygame.quit()


def about_screen():
    x = True
    while x:
     screen.blit(bg_about,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             x = False
             pygame.quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_0:
                 first_interface()


def short_output(x):
    if x==1:
        # 1 run
        shot_result_animation()
        screen.blit(one_run,(0,0))
        pygame.display.update()
        time.sleep(2)
    if x==2:
        # 2 run
        shot_result_animation()
        screen.blit(two_run,(0,0))
        pygame.display.update()
        time.sleep(2)
    if x==3:
        # 3 run
        shot_result_animation()
        screen.blit(three_run,(0,0))
        pygame.display.update()
        time.sleep(2)
    if x==4:
        # four
        shot_result_animation()
        screen.blit(four_run,(0,0))
        pygame.display.update()
        time.sleep(2)
    if x==5:
        # six
        shot_result_animation()
        screen.blit(six_run,(0,0))
        pygame.display.update()
        time.sleep(2)

def shot_result_animation():
     screen.blit(dp_1,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_2,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_3,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_4,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_5,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_6,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_7,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_8,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_7,(0,0))
     pygame.display.update()
     time.sleep(0.2)
     screen.blit(dp_9,(0,0))
     pygame.display.update()
     time.sleep(0.2)


