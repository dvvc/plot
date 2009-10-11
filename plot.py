import pygame
import math

# SETTINGS


screen=None
clock = pygame.time.Clock()
all_points=[]
all_functions=[]

def init(screen_size):
    """Initialize graphics"""
    global screen
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
        
def add_points(data, color=(255,0,0)):
    """Add a list of points for plotting"""
    global all_points
    all_points.append((data,color))

def add_function(f, color=(0,0,255)):
    """Add a function for plotting"""
    global all_functions
    all_functions.append((f,color))
    

def plot(xrange=(0,400),yrange=(0,400),screen_range=(400,400)):
    """Plot all the stored data"""
    global clock, all_points, all_functions

    draw_axis(xrange,yrange,screen_range)

    for (points,color) in all_points:
        for p in points:
            cp = convert_point(p,xrange,yrange,screen_range)
            draw_point(cp, color)

    for (f,color) in all_functions:
        # get the points for the function
        points = generate_points(f,xrange,yrange,screen_range)
        for p in points:
            cp = convert_point(p,xrange,yrange,screen_range)
            draw_point(cp,color)


    while(True):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(20)

def generate_points(f,xrange=(0,400),yrange=(0,400),screen_range=(400,400)):
    """Generate all required points to draw a function and call plot"""
    npoints = screen_range[0]
    xrange_length = xrange[1]-xrange[0]
    increment = xrange_length/float(npoints)

    data = [(x,f(x)) for x in drange(xrange[0],xrange[1],increment)]
    
    return data


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


def draw_point(point,color):
    """draw a point in the screen"""
    pygame.draw.circle(screen,color,point,2)


# Found in stackoverflow.com
def drange(start, stop, step):
    """Generate a range of points with a step smaller than 1"""
    r = start
    while r < stop:
        yield r
        r += step



# just for testing purposes
if __name__ == "__main__":
    screen_size=(800,200)

    init(screen_size)

    add_function(lambda x: math.sin(2*x*math.pi), (255,0,0))
    add_function(lambda x: 0.5, (0,255,0))
    
    add_points([(1,1),(2,0.5), (3,0)],(0,0,255))

    plot(xrange=(-math.pi,math.pi),
         yrange=(-1,1),
         screen_range=screen_size)
    
