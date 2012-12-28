# J. Morgan
# 12/27/2012
# particle.py - a simple particle class


class particle:
    """A particle."""
    def __init__(self, charge):
        self.charge = charge
        self.pos = ([0.0, 0.0, 0.0])
        self.vel = ([0.0, 0.0, 0.0])

    def set_positions(self, x, y, z):
        self.pos = ([x, y, z])

    def set_velocities(self, vx, vy, vz):
        self.vel = ([vx, vy, vz])

    def self_test(self):
        self.__init__(1.234)
        self.set_positions(1.0, 2.0, 3.0)
        self.set_velocities(4.0, 5.0, 6.0)

        print "\nSelf Test:"
        print "==========\n"
        print "charge = ", self.charge
        print "position = ", self.pos
        print "velocity = ", self.vel

x = particle(0.0)
x.self_test()
