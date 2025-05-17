
import  pygame,sys
from pygame.examples.sprite_texture import clock
from simulation import Simulation

pygame.init()

grey = (29,29,29)
width = 750
height = 750
fps = 12
cell_size = 25
#store he screen size
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("PROJECT1","CONWAY'S GAME OF LIFE")

clock = pygame.time.Clock()
simulation = Simulation(width,height,cell_size)
# simulation loop
while True:
    #1 event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // cell_size
            col = pos[0] // cell_size
            simulation.toggle_cell(row, col)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.stat()
                pygame.display.set_caption("GAME OF LIFE")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("GAME OF LIFE STOPPED")
            elif event.key == pygame.K_f:
                fps += 2
            elif event.key == pygame.K_s:
                if fps > 5:
                    fps -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()

    #2 updating state
    simulation.update()

    #3 drawing
    window.fill(grey)
    simulation.draw(window)
# draw on image onto another
    #surface.blit(python,(200,200))
    pygame.display.update()
    clock.tick(fps)

# pygame.quit()












