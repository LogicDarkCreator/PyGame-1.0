#####################################################################################################
#                                                                                                   #
#   Project by JSD Dev Laboratories                                                                 #
#   Programmer: Ivan Karpov                                                                         #
#   Tested with PyCharm Community Edition by JetBrains                                              #
#   Debugged with PyCharm Community Edition by JetBrains                                            #
#   Re-Tested with PyCharm Community Edition by JetBrains                                           #
#   Download PyCharm Community Edition https://www.jetbrains.com/pycharm/download/?section=windows  #
#                                                                                                   #
#####################################################################################################

# Import libs
import pygame
import random
import time
from configs.colors import *
from configs.snake_set import *

# Create a game
pygame.init()

# Screen
dis_width = 1280
dis_height = 720
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

pygame.display.update()
pygame.display.set_caption("Snake Game")

# Main

font_style = pygame.font.SysFont("Aktiv Grotesk Ex Trial", 25)

def snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def mess(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def score(is_score):
    value = font_style.render("Score: " + str(score), True, blue)
    dis.blit(value, [1280,0])

def main():
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    LOS = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    game_over = False
    while not game_over:

        while game_close == True:
            dis.fill(black)
            mess("You lose! Press ESC for exit or E for new game", white)
            score(is_score=LOS - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change

            dis.fill(black)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > LOS:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            snake(snake_block, snake_List)
            score(is_score=LOS - 1)
            pygame.display.update()
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                LOS += 1
            clock.tick(snake_speed)
    pygame.quit()
    quit()

main()