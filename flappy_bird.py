import pygame
import constant


def draw_window(win, bird, pipes, base, score):
    # .blit() means draw
    win.blit(constant.BG_IMG, (0,0))

    for pipe1 in pipes:
        pipe1.draw(win)

    base.draw(win)
    bird.draw(win)

    text = constant.STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (constant.WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()



