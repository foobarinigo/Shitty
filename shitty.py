# J. Morgan
# 12/27/2012
# shitty.py - a shitty n-body program

from numpy import array

class dynamics:
    """Hold important information about this simulation."""
    def __init__(self, coupling_constant, max_iterations):
        self.coupling_constant = coupling_constant
        self.max_iterations = max_iterations
        
        self.distances = []
        self.forces = []
        self.min_distance = 1.0
        self.time_step = 1.0
        self.coupling_constant = 1.0
        self.iteration_counter = 0
    
    def add_distance(self, d):
        self.distances.append(d)

    def add_force(self, f):
        self.forces.append(f)

    def self_test(self):
        self.__init__(1.2, 3.4)
        self.add_distance(1.0)
        x = array([0.0, 1.0, 2.0])
        self.add_force(x)
        
        print "\nSelf Test:"
        print "==========\n"
        print "distances = ", self.distances
        print "forces = ", self.forces
        print "minimum distance = ", self.min_distance
        print "time step = ", self.time_step
        print "coupling constant = ", self.coupling_constant
        print "iteration counter = ", self.iteration_counter

x = dynamics(1.0, 2.0)
x.self_test()
