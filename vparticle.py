# J. Morgan
# 1/1/2013
# vparticle.py - a particle class with some drawing stuff.  "Unnecessary inheritance"

from particle import *
from visual import *

class vparticle(particle):
    """A particle with attributes for drawing with vPython."""
    def __init__(self, charge, position, velocity, radius, color):
        particle.__init__(self, charge, position, velocity)
        # We need a way to verify initialization color is valid
        self.color = color
        self.radius = radius
        if( self.radius == 0.):
            self.draw = curve(pos = self.pos, color = self.color)
        else:
            self.draw = sphere(pos = self.pos, radius = self.radius, color = self.color)
            self.draw.trail = curve(color = (.3, .3, .3))

    def draw_again(self):
        if( self.radius == 0.):
            self.draw.append(pos = self.pos)
        else:
            self.draw.pos = self.pos
            self.draw.trail.append(pos = self.pos)

    def dump():
        particle.dump()
        print "color = ", self.color
        print "radius = ", self.radius
