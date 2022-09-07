import pygame
import constant


def draw_window(win, birds, pipes, base, score, gen=-1):
    # .blit() means draw
    win.blit(constant.BG_IMG, (0,0))

    text = constant.STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (constant.WIN_WIDTH - 10 - text.get_width(), 10))

    if gen > -1:
        text = constant.STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
        win.blit(text, (10, 10))

    for pipe1 in pipes:
        pipe1.draw(win)

    for bird1 in birds:
        bird1.draw(win)

    base.draw(win)

    pygame.display.update()



