# J. Morgan
# 12/30/2012
# nbody.py - A class to do nbody gravity

from dynamics import *

class nbody_gravity(dynamics):

    def __init__(self, max_iterations):
        dynamics.__init__(self, max_iterations)

    def force(self, c, p1, p2):
        """Compute the force on particle 1, from particle 2."""
        # Vector connecting two points
        vec_r = p2.pos - p1.pos
    
        # Distance between
        r = sqrt(dot(vec_r, vec_r))
    
        if( r < self.min_distance ):
            self.min_distance = r

        # Magnitude of force between
        f_mag = c * p1.charge * p2.charge / r**2. 

        # Return array 
        return f_mag * vec_r / r
        
    def solve(self, idx):
        """Solve for the accelleration on particle p[idx]."""
        for j in range(idx + 1, len(self.particles)):
            f_temp = self.force(constants.G, self.particles[idx], self.particles[j])
            # For short times, the velocity depends linearly on the accelleration
            self.particles[idx].vel += f_temp / self.particles[idx].charge
            # Newton's 3rd law allows us to update the bottom triangle in the particle-particle matrix simultaneous with the top
            self.particles[j].vel -= f_temp / self.particles[j].charge 
        return

x = nbody_gravity(1)
x.go()
