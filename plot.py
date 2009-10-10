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
    """Convert the coordinates of a point based on the plotting range and the screen size"""
    xfactor = screen_range[0] / float(xrange[1]-xrange[0])
    yfactor = screen_range[1] / float(yrange[1]-yrange[0])
    xoffset = -xrange[0] * xfactor
    yoffset = -yrange[0] * yfactor

    x =  point[0] * xfactor + xoffset
    y = point[1] * yfactor + yoffset

    # flip the y coord so the origin is at the bottom
    y = screen_range[1] - y

    return (x,y)


def draw_point(point):
    """draw a point in the screen"""
    pygame.draw.circle(screen,(255,0,0),point,2)


# just for testing purposes
if __name__ == "__main__":
    init()
    p
