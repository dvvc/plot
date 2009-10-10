import pygame
import math

# SETTINGS


screen=None
clock = pygame.time.Clock()

def init(screen_size):
    """Initialize graphics"""
    global screen
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
        
def plot(data,xrange=(0,400),yrange=(0,400),screen_range=(400,400)):
    global clock

    draw_axis(xrange,yrange,screen_range)

    for p in data:
        c = convert_point(p,xrange,yrange,screen_range)
        draw_point(c)

    while(True):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(20)


def draw_axis(xrange, yrange, screen_range):
    """draw the axis"""
    global screen
    xaxis_orig = (xrange[0], 0)
    xaxis_final = (xrange[1], 0)

    xaxis_orig_c = convert_point(xaxis_orig,xrange,yrange,screen_range)
    xaxis_final_c = convert_point(xaxis_final,xrange,yrange,screen_range)

    yaxis_orig = (0, yrange[0])
    yaxis_final = (0, yrange[1])

    yaxis_orig_c = convert_point(yaxis_orig,xrange,yrange,screen_range)
    yaxis_final_c = convert_point(yaxis_final,xrange,yrange,screen_range)

    pygame.draw.line(screen,(255,255,255),xaxis_orig_c,xaxis_final_c)
    pygame.draw.line(screen,(255,255,255),yaxis_orig_c,yaxis_final_c)

def convert_point(point, xrange, yrange, screen_range):
    """Convert the coordinates of a point based on the plotting range and the screen size"""
    xfactor = screen_range[0] / float(xrange[1]-xrange[0])
    yfactor = screen_range[1] / float(yrange[1]-yrange[0])
    xoffset = -xrange[0] * xfactor
    yoffset = -yrange[0] * yfactor

    x = round(point[0] * xfactor) + xoffset
    y = round(point[1] * yfactor) + yoffset

    # flip the y coord so the origin is at the bottom
    y = screen_range[1] - y

    return (x,y)


def draw_point(point):
    """draw a point in the screen"""
    pygame.draw.circle(screen,(255,0,0),point,2)


# Found in stackoverflow.com
def drange(start, stop, step):
    """Generate a range of points with a step smaller than 1"""
    r = start
    while r < stop:
        yield r
        r += step

# just for testing purposes
if __name__ == "__main__":
    screen_size=(400,400)

    init(screen_size)

    plot([(x,math.sin(x)) for x in drange(-2*math.pi,2*math.pi,step=0.2)],
         xrange=(-2*math.pi,2*math.pi),
         yrange=(-1,1),
         screen_range=screen_size)

