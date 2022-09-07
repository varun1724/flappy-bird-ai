import bird
import base
import pipe
import pygame
import constant
import neat
import flappy_bird


def eval_genomes(genomes, config):
    bird1 = bird.Bird(230, 250)
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
            if event.type == pygame.QUIT:
                run = False

        # bird1.move()
        add_pipe = False
        rem = []
        for pipe1 in pipes:
            if pipe1.collide(bird1):
                pass

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

        if bird1.y + bird1.img.get_height() > 730:
            pass

        base1.move()
        flappy_bird.draw_window(win, bird1, pipes, base1, score)
    
    pygame.quit()
    quit()

def run(config_path):
    config = neat.Config
    (
        neat.DefaultGenome, 
        neat.DefaultReproduction, 
        neat.DefaultSpeciesSet, 
        neat.DefaultStagnation, 
        config_path
    )

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(eval_genomes(), 50)
    

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "neat_settings.txt")
    run(config_path)
