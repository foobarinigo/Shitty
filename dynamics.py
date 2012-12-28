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
        self.distances = []
        self.forces = []
        self.time_step = 1.0
        self.iteration_counter = 0

    
    def add_particle(self, p):
        self.particles.append(p)


    def add_distance(self, d):
        self.distances.append(d)


    def add_force(self, f):
        self.forces.append(f)


    def force(self, c, p1, p2):
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
        for it in range(self.iteration_counter, self.max_iterations):

            print "iteration: ", self.iteration_counter

            # Destroy the lists.  "Shitty"
            self.forces = []
            self.distances = []
        
            # Loop over all particles (keeping in mind f_ij = -f_ji    
            for i in range(0, len(self.particles)):
                print "particle[", i, "]"

                f_temp_list = []
                d_temp_list = []

                for j in range(i+1, len(self.particles)):
                    print "particle[", j, "]"
                    d_temp_vec = self.particles[i].pos - self.particles[j].pos
                    d_temp = sqrt(dot(d_temp_vec, d_temp_vec))
                    d_temp_list.append(d_temp)
                    f_temp_list.append(self.force(constants.G, self.particles[i], self.particles[j]))

                self.add_force(f_temp_list)
                self.add_distance(d_temp_list)

            self.iteration_counter += 1
        
    
    def dump(self):
        print "\nContents:"
        print "========="
        print "Number of particles: ", len(self.particles)
        for p in self.particles:
            print "particle: ", p.charge, p.pos, p.vel
        print "distances = ", self.distances
        print "forces = ", self.forces
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

x = dynamics(0)
x.self_test()

