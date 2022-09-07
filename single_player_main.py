import bird
import base
import pipe
import pygame
import constant
import flappy_bird


best = 0
reset_val = True


def main():
    global best
    global reset_val

    bird1 = bird.Bird(230, 350)
    base1 = base.Base(730)
    pipes = [pipe.Pipe(625)]
    

    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0
    
    run = True
    while run:

        # sets it to 30 ticks every second (slows the while loop)
        clock.tick(30)

        # tracks whenever something happens in the window. Ex. User clicks the mouse
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird1.jump()
            if event.type == pygame.QUIT:
                run = False
                reset_val = False

        bird1.move()
        add_pipe = False
        rem = []
        for pipe1 in pipes:
            if pipe1.collide(bird1):
                if score > best:
                    best = score
                reset_val = True
                run = False

            if pipe1.x + pipe1.PIPE_TOP.get_width() < 0:
                rem.append(pipe1)

            if not pipe1.passed and pipe1.x < bird1.x:
                pipe1.passed = True
                add_pipe = True

            pipe1.move()

        if add_pipe:
            score += 1
            pipes.append(pipe.Pipe(700))

        for r in rem:
            pipes.remove(r)

        if bird1.y + bird1.img.get_height() > 730 or bird1.y < -30:
            if score > best:
                best = score
            reset_val = True
            run = False

        base1.move()
        flappy_bird.draw_window(win, [bird1], pipes, base1, score, best=best)
    
    if reset_val == False:
        pygame.quit()
        quit()
    else:
        main()



main()

