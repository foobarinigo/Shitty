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
        self.draw = sphere(pos = self.pos, radius = self.radius, color = self.color)
        self.draw.trail = curve(color = (.3, .3, .3))

    def dump():
        particle.dump()
        print "color = ", self.color
        print "radius = ", self.radius
