# J. Morgan
# 12/27/2012
# shitty.py - a shitty n-body program

from numpy import array, dot, sqrt
from scipy import constants
from particle import *
from dynamics import *

def force(c, p1, p2):
    """Compute the force on particle 1, from particle 2."""
    vec_r = p2.pos - p1.pos
    r = sqrt(dot(vec_r, vec_r))
    f_mag = c * p1.charge * p2.charge / r**2. 
    return f_mag * vec_r / r
    

def testing_program():
    x = particle(1., [1., 2., 3.], [0., 0., 0.])
    y = particle(1., [2., 3., 4.], [0., 0., 0.])

    print force(constants.G, x, y)


testing_program()
