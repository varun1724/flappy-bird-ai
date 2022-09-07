import bird
import base
import pipe
import pygame
import constant
import neat
import os
import flappy_bird

gen = 0

def eval_genomes(genomes, config):
    global gen
    gen += 1

    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        g.fitness = 0

        nets.append(net)
        birds.append(bird.Bird(230, 350))
        ge.append(g)

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
                pygame.quit()
                quit()

        # Might be more than one pipe on the screen at once. This makes the check be for the right pipe
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        for x, bird1 in enumerate(birds):
            bird1.move()
            ge[x].fitness += 0.1

            output = nets[x].activate((bird1.y, abs(bird1.y - pipes[pipe_ind].height), abs(bird1.y - pipes[pipe_ind].bottom)))
            
            if output[0] > 0.5:
                bird1.jump()

        add_pipe = False
        rem = []
        for pipe1 in pipes:
            for x, bird1 in enumerate(birds):
                if pipe1.collide(bird1):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe1.passed and pipe1.x < bird1.x:
                    pipe1.passed = True
                    add_pipe = True

            if pipe1.x + pipe1.PIPE_TOP.get_width() < 0:
                rem.append(pipe1)

            pipe1.move()

        if add_pipe:
            score += 1
            
            for g in ge:
                g.fitness += 5

            pipes.append(pipe.Pipe(700))

        for r in rem:
            pipes.remove(r)

        for x, bird1 in enumerate(birds):
            if bird1.y + bird1.img.get_height() >= 730 or bird1.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        if score > 50:
            break

        base1.move()
        flappy_bird.draw_window(win, birds, pipes, base1, score, gen=gen)




def run(config_path):

    p = neat.Population(neat.Config(
        neat.DefaultGenome, neat.DefaultReproduction, 
        neat.DefaultSpeciesSet, neat.DefaultStagnation, 
        config_path
        ))

    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    # will return the best genome when it stops running
    winner = p.run(eval_genomes, 50)

    print(winner)
    

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "neat_settings.txt")
    run(config_path)
