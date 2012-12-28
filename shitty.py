# J. Morgan
# 12/27/2012
# shitty.py - a shitty n-body program

from numpy import array, dot, sqrt
from scipy import constants
from particle import *
from dynamics import *

mass_earth = 5.97219e24 # kg
r_earth = 6.3781e6 # m


def testing_program():
    # Mass of earth at origin
    x = particle(mass_earth, [0., 0., 0.], [0., 0., 0.])
    # Test mass at R_earth
    y = particle(1., [0., 0., r_earth], [0., 0., 0.])

    z = dynamics(30)
    z.add_particle(x)
    z.add_particle(y)
    
    # Force of earth (x) on 1 kg (y) should be roughly -9.81 kg m s^-2
    print force(constants.G, y, x)


testing_program()
