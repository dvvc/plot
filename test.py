import plot
import unittest

class TestPlot(unittest.TestCase):

    def test_origin(self):
        """A point's y coordinates have to be transposed to the bottom of the screen if the coordinate origin is at 0,0"""
        point=(0,0)
        self.assertEquals(
            plot.convert_point(point,xrange=(0,100),yrange=(0,100),screen_range=(400,400)),
            (0,400))

    
                               
