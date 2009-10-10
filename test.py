import plot
import unittest

class TestPlot(unittest.TestCase):

    def test_origin(self):
        """A point's y coordinates have to be transposed to the bottom of the screen if the coordinate origin is at 0,0"""
        point=(0,0)
        self.assertEquals(
            plot.convert_point(point,xrange=(0,400),yrange=(0,400),screen_range=(400,400)),
            (0,400))

    
    def test_ranges(self):
        """When the coordinates range is a factor of the screen range, points have to be consequently scaled"""
        point=(50,100)
        self.assertEquals(
            plot.convert_point(point,xrange=(0,200),yrange=(0,200),screen_range=(400,400)),
            (100,200))
    

    def test_positive_offset(self):
        """A point has to be moved when the coordinate range has its origin below (0,0)"""
        point=(50,100)
        self.assertEquals(
            plot.convert_point(point,xrange=(-50,350), yrange=(-100,300), screen_range=(400,400)),
            (100,200))
                               

    def test_negative_offset(self):
        """A point has to be moved when the coordinate range has its origin above (0,0)"""
        point=(50,100)
        self.assertEquals(
            plot.convert_point(point,xrange=(100,500),yrange=(150,550),screen_range=(400,400)),
            (-50,450))
            

    def test_different_factors(self):
        """The x and y axis may have different ratios"""
        point=(40,60)
        self.assertEquals(
            plot.convert_point(point,xrange=(0,200),yrange=(0,320),screen_range=(400,400)),
            (80,325))


    def test_range_below_1(self):
        """When the plot coordinate range has higher resolution than the screen range, translated coordinates are approximated to the closest point"""
        point=(455,200)
        self.assertEquals(
            plot.convert_point(point,xrange=(0,800),yrange=(0,1200),screen_range=(400,400)),
            (round(227.5),round(333.3)))
