# J. Morgan
# 12/27/2012
# shitty.py - a shitty n-body program

from numpy import array, dot, sqrt
from scipy import constants
from particle import *
from dynamics import *

mass_earth = 5.97219e24 # kg
r_earth = 6.3781e6 # m

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
    

def testing_program():
    # Mass of earth at origin
    x = particle(mass_earth, [0., 0., 0.], [0., 0., 0.])
    # Test mass at R_earth
    y = particle(1., [0., 0., r_earth], [0., 0., 0.])

    # Force of earth (x) on 1 kg (y) should be roughly -9.81 kg m s^-2
    print force(constants.G, y, x)


testing_program()
