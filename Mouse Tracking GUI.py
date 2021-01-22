import pygame
import sys
import random
from pygame.locals import *
import time

# sys.stdout = open("text.txt", 'w')

wrong = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
flag = True
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


intro_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('Arial', 25)
text = font.render('Click \'START\' to begin', True, (0, 255, 0), (0, 0, 255))
text2 = font.render('START', True, (0, 255, 0), (0, 0, 255))
textRect2 = text2.get_rect()
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//4)
textRect2.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5)
running = True



# print("center: {}, {}".format(rect_x_origin+width/2, rect_y_origin+height/2))
while running:
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    pygame.display.update()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and textRect2.left < event.pos[0] < textRect2.right and textRect2.top < event.pos[1] < textRect2.bottom:
        det_button = random.randint(0, 2)
        width = 50
        height = 50
        rect_x_origin = random.randint(200, 400)
        rect_y_origin = random.randint(200, 400)
        screen.fill((0, 0, 0))
        square = pygame.draw.rect(screen, (0, 0, 255), ((rect_x_origin, rect_y_origin), (width, height)))
        if det_button == 0:
            screen.blit(font.render('L', True, (255, 255, 255)),
                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
        elif det_button == 1:
            screen.blit(font.render('M', True, (255, 255, 255)),
                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
        elif det_button == 2:
            screen.blit(font.render('R', True, (255, 255, 255)),
                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
        pygame.display.update()
        start = time.time()
        while flag:
            pygame.display.update()
            event = pygame.event.poll()
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_y_origin + height > event.pos[1] > rect_y_origin and rect_x_origin + width > event.pos[0] > rect_x_origin:
                    if pygame.mouse.get_pressed()[0] and det_button == 0:
                        end = time.time()
                        print("{} {}".format(pygame.mouse.get_pressed(), wrong))
                        print("time: {}".format((end - start)))
                        wrong = 0
                        screen.fill((0, 0, 0))
                        rect_x_origin = random.randint(200, 600)
                        rect_y_origin = random.randint(200, 400)
                        pygame.draw.rect(screen, (0, 0, 255), ((rect_x_origin, rect_y_origin), (width, height)))
                        det_button = random.randint(0, 2)
                        if det_button == 0:
                            screen.blit(font.render('L', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 1:
                            screen.blit(font.render('M', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 2:
                            screen.blit(font.render('R', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        start = time.time()
                    elif pygame.mouse.get_pressed()[1] and det_button == 1:
                        end = time.time()
                        print("{} {}".format(pygame.mouse.get_pressed(), wrong))
                        print("time: {}".format((end - start)))
                        wrong = 0
                        screen.fill((0, 0, 0))
                        rect_x_origin = random.randint(200, 600)
                        rect_y_origin = random.randint(200, 400)
                        pygame.draw.rect(screen, (0, 0, 255), ((rect_x_origin, rect_y_origin), (width, height)))
                        det_button = random.randint(0, 2)
                        if det_button == 0:
                            screen.blit(font.render('L', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 1:
                            screen.blit(font.render('M', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 2:
                            screen.blit(font.render('R', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        start = time.time()
                    elif pygame.mouse.get_pressed()[2] and det_button == 2:
                        end = time.time()
                        print("{} {}".format(pygame.mouse.get_pressed(), wrong))
                        print("time: {}".format((end - start)))
                        wrong = 0
                        screen.fill((0, 0, 0))
                        rect_x_origin = random.randint(200, 600)
                        rect_y_origin = random.randint(200, 400)
                        pygame.draw.rect(screen, (0, 0, 255), ((rect_x_origin, rect_y_origin), (width, height)))
                        det_button = random.randint(0, 2)
                        if det_button == 0:
                            screen.blit(font.render('L', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 1:
                            screen.blit(font.render('M', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        elif det_button == 2:
                            screen.blit(font.render('R', True, (255, 255, 255)),
                                        (rect_x_origin + (width / 2.5), rect_y_origin + height / 5))
                        start = time.time()
                    else:
                        wrong += 1
                        # print(wrong)
                else:
                    wrong += 1 #TODO: Penalizes user for click outside box. Subject to change
                    # print(wrong)
# sys.stdout.close()
