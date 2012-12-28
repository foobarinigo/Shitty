# J. Morgan
# 12/27/2012
# particle.py - a simple particle class

from numpy import array

class particle:
    """A particle."""
    def __init__(self, charge, position, velocity):
        self.charge = charge
        # position and velocity don't need to be array's (which is clumsy syntax), we'll promote them internally by picking off the indices 
        self.pos = array([position[0], position[1], position[2]])
        self.vel = array([velocity[0], velocity[1], velocity[2]])

    def set_position(self, position):
        self.pos = array([position[0], position[1], position[2]])

    def set_velocity(self, velocity):
        self.vel = array([velocity[0], velocity[1], velocity[2]])

    def self_test(self):
        self.__init__(1.234, array([0.0, 0.0, 0.0]), array([0.0, 0.0, 0.0]))
        self.set_position(array([1.0, 2.0, 3.0]))
        self.set_velocity(array([4.0, 5.0, 6.0]))

        print "\nSelf Test:"
        print "==========\n"
        print "charge = ", self.charge
        print "position = ", self.pos
        print "velocity = ", self.vel

    #   pos = [0.0, 0.0, 0.0]
    #   vel = [0.0, 0.0, 0.0]
    #   x = particle(0.0, pos, vel)
    #   x.self_test()
