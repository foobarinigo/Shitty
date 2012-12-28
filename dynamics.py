# J. Morgan
# 12/27/2012
# dynamics.py - a class to hold dynamical information

from numpy import array
from scipy import constants
from particle import *

class dynamics:
    """Hold important information about this simulation."""
    def __init__(self, max_iterations):
        self.max_iterations = max_iterations
        
        self.particles = []
        self.distances = []
        self.forces = []
        self.min_distance = 1.0
        self.time_step = 1.0
        self.iteration_counter = 0
    
    def add_particle(self, p):
        self.particles.append(p)

    def add_distance(self, d):
        self.distances.append(d)

    def add_force(self, f):
        self.forces.append(f)

    def force(c, p1, p2):
        """Compute the force on particle 1, from particle 2."""
        # Vector connecting two points
        vec_r = p2.pos - p1.pos
    
        # Distance between
        r = sqrt(dot(vec_r, vec_r))
    
        # Magnitude of force between
        f_mag = c * p1.charge * p2.charge / r**2. 

        # Return array 
        return f_mag * vec_r / r
    
    def go(self):
        for it in range(0:max_iterations):

            # Destroy the force object.  I told you this was shitty
            self.forces = []
        
            # Loop over all particles (keeping in mind f_ij = -f_ji    
            for i in range(0:len(self.particles)):
                temp_list = []
                for j in range(i+1:len(self.particles)):
                    temp_list.append(force(constants.G, self.particles[i], self.particles[j]))
                self.add_force(temp_list)

    
    def dump(self):
        print "\nContents:"
        print "========="
        for p in self.particles:
            print "particle: ", p.charge, p.pos, p.vel
        print "distances = ", self.distances
        print "forces = ", self.forces
        print "minimum distance = ", self.min_distance
        print "time step = ", self.time_step
        print "coupling constant = ", self.coupling_constant
        print "iteration counter = ", self.iteration_counter

    def self_test(self):
        self.__init__(30)
        self.add_distance(1.0)
        x = array([0.0, 1.0, 2.0])
        self.add_force(x)
        y = particle(1., [1., 1., 1.], [0., 0., 0.])
        self.add_particle(y)
        
        print "\nSelf Test:"
        print "==========\n"
        self.dump()

x = dynamics(30)
x.self_test()
