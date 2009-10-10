import pygame

# SETTINGS
screen_width = 400
screen_height = 400


screen=None
clock = pygame.time.Clock()

def init():
    """Initialize graphics"""
    global screen, screen_width, screen_height
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
        
def plot(data,yrange=(0,200)):
    global clock
    for p in data:
        draw_point(p)

    while(True):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(20)

def convert_point(point, xrange, yrange, screen_range):
    xfactor = screen_range[0] /
    yfactor = screen_range[1]


def draw_point(pair):
    pygame.draw.circle(screen,(255,0,0),pair,2)


if __name__ == "__main__":

    init()
    plot([(100,100),(200,100),(300,150)])





