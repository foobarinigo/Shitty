# J. Morgan
# 12/27/2012
# dynamics.py - a class to hold dynamical information

from numpy import array, dot, sqrt
from scipy import constants
from particle import *

class dynamics:
    """Hold important information about this simulation."""
    def __init__(self, max_iterations):
        self.max_iterations = max_iterations    
        self.particles = []
        self.time_step = 1.0
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

            # Loop over all particles (keeping in mind f_ij = -f_ji    
            for i in range(0, len(self.particles)):
                self.solve(i)

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

        self.__init__(1)
        
        # Mass of earth at origin
        x = particle(mass_earth, [0., 0., 0.], [0., 0., 0.])
        # Test mass at R_earth
        y = particle(1., [0., 0., r_earth], [0., 0., 0.])

        self.add_particle(x)
        self.add_particle(y)
        self.go()

        print "\nSelf Test:"
        print "==========\n"
        self.dump()

