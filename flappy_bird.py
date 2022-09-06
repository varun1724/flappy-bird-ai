import pygame
import neat
import time
import random
import bird
import constant


def draw_window(win, bird):
    # .blit() means draw
    win.blit(constant.BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()


def main():
    bird1 = bird.Bird(200, 200)
    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    
    run = True
    while run:
        # tracks whenever something happens in the window. Ex. User clicks the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bird1.move()
        draw_window(win, bird1)
    
    pygame.quit()
    quit()

main()



