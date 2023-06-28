import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1024,650))

bg_ChooseFormat = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/choose_format.png')
bg_RankingType = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/ranking_type.png')
bg_t20_team = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/t20_team.png')
bg_t20_batting = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/t20_batting.png')
bg_t20_bowling = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/t20_bowling.png')
bg_odi_team = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/odi_team.png')
bg_odi_batting = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/odi_batting.png')
bg_odi_bowling = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/odi_bowling.png')
bg_test_team = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/test_team.png')
bg_test_batting = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/test_batting.png')
bg_test_bowling = pygame.image.load('C:/Users/Naveen/Desktop/MiniProject/graphics/test_bowling.png')


def ranking_loop():
    x = True
    pressed = 0
    executed = 0

    while x:
        screen.fill((0,0,0))
        if pressed == 0:
            screen.blit(bg_ChooseFormat,(0,0))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
                return 1
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                  t20_rankingType()
                if event.key == pygame.K_0:
                    x = False
                    return 1
                    pygame.quit()
                if event.key == pygame.K_2:
                    odi_rankingType()
                if event.key == pygame.K_3:
                    test_rankingType()

def t20_rankingType():

  while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_t20_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_t20_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_t20_bowling()

def display_t20_team():
    x = True
    while x:
     screen.blit(bg_t20_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def display_t20_batting():
    x = True
    while x:
     screen.blit(bg_t20_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def display_t20_bowling():
    x = True
    while x:
     screen.blit(bg_t20_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def odi_rankingType():

    while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_odi_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_odi_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_odi_bowling()

def display_odi_team():
    x = True
    while x:
     screen.blit(bg_odi_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def display_odi_batting():
    x = True
    while x:
     screen.blit(bg_odi_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def display_odi_bowling():
    x = True
    while x:
     screen.blit(bg_odi_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def test_rankingType():

    while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_test_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_test_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_test_bowling()

def display_test_team():
    x = True
    while x:
     screen.blit(bg_test_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()

                x = False

def display_test_batting():
    x = True
    while x:
     screen.blit(bg_test_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()
                x = False

def display_test_bowling():
    x = True
    while x:
     screen.blit(bg_test_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()
                x = False
                if event.key == pygame.K_2:
                  # choose odi ranking t
                   odi_rankingType()
                if event.key == pygame.K_3:
                  # choose test ranking type:
                  test_rankingType()


def t20_rankingType():

  while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_t20_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_t20_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_t20_bowling()

def display_t20_team():
    x = True
    while x:
     screen.blit(bg_t20_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def display_t20_batting():
    x = True
    while x:
     screen.blit(bg_t20_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def display_t20_bowling():
    x = True
    while x:
     screen.blit(bg_t20_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                t20_rankingType()
                x = False

def odi_rankingType():

    while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_odi_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_odi_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_odi_bowling()

def display_odi_team():
    x = True
    while x:
     screen.blit(bg_odi_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def display_odi_batting():
    x = True
    while x:
     screen.blit(bg_odi_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def display_odi_bowling():
    x = True
    while x:
     screen.blit(bg_odi_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                odi_rankingType()
                x = False

def test_rankingType():

    while True:
     screen.blit(bg_RankingType,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_0:
               ranking_loop()
           if event.key == pygame.K_1:
               display_test_team()
           if event.key == pygame.K_2:
                # display t20 batting ranking
                display_test_batting()
           if event.key == pygame.K_3:
                # display t20 bowling ranking
                display_test_bowling()

def display_test_team():
    x = True
    while x:
     screen.blit(bg_test_team,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()

                x = False

def display_test_batting():
    x = True
    while x:
     screen.blit(bg_test_batting,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()
                x = False

def display_test_bowling():
    x = True
    while x:
     screen.blit(bg_test_bowling,(0,0))
     pygame.display.update()
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                test_rankingType()
                x = False

def check(x):
    initial = 0
    if x == 1:
        intial = 1
    initial = 1
