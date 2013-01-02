# J. Morgan
# 12/27/2012
# dynamics.py - a class to hold dynamical information

from numpy import array, dot, sqrt
from scipy import constants
from visual import color, sphere
from vparticle import *

class dynamics:
    """Hold important information about this simulation."""
    def __init__(self, max_iterations):
        self.max_iterations = max_iterations    
        self.particles = []
        self.time_step = 60.0 # We're going to draw at 60fps, so 1 frame = 1 sec
        self.min_distance = constants.c * 3.155e7 # light year.  Need to do something smarter later
        self.iteration_counter = 0

    
    def add_particle(self, p):
        self.particles.append(p)


    def force(self, c, p1, p2):
        """Compute the force on particle 1, from particle 2."""
        return array([0., 0., 0.])


    def solve(self, idx):
        """Update the position and velocity of self.particles[idx]."""
        return


    def go(self):
        for it in range(self.iteration_counter, self.max_iterations):

            for i in range(0, len(self.particles)):
                rate(60)
                self.solve(i)
                self.particles[i].draw.pos = self.particles[i].pos
                self.particles[i].draw.trail.append(pos = self.particles[i].pos)

            self.iteration_counter += 1
        
    
    def dump(self):
        print "\nContents:"
        print "========="
        print "Number of particles: ", len(self.particles)
        for p in self.particles:
            print "particle: charge: ", p.charge, "\tposition: ", p.pos, "\tvelocity: ", p.vel
        print "time step = ", self.time_step
        print "iteration counter = ", self.iteration_counter
        print "max iterations = ", self.max_iterations


    def self_test(self):
        mass_earth = 5.97219e24 # kg
        r_earth = 6.3781e6 # m

        self.__init__(2000)
        
        # Mass of earth at origin
        x = vparticle(mass_earth, [0., 0., 0.], [0., 0., 0.], .5 * r_earth, color.blue)
        # Test mass at R_earth moving orbital velocity
        y = vparticle(1., [r_earth, 0., 0.], [0., 0.6 * sqrt(constants.G * mass_earth / r_earth), 0.], .05 * r_earth, color.green)

        self.add_particle(x)
        self.add_particle(y)
        self.go()

        print "\nSelf Test:"
        print "==========\n"
        self.dump()
