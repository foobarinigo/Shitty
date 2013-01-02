# J. Morgan
# 12/30/2012
# nbody.py - A class to do nbody gravity

from dynamics import *

class nbody_gravity(dynamics):

    def __init__(self, max_iterations, soften_distance = 0.):
        dynamics.__init__(self, max_iterations)
        self.softening = soften_distance

    def force(self, c, p1, p2):
        """Compute the force on particle 1, from particle 2."""
        # Vector connecting two points
        vec_r = p1.pos - p2.pos
    
        # Distance between
        r = sqrt(dot(vec_r, vec_r))
    
        if( r < self.min_distance ):
            self.min_distance = r

        # Magnitude of force between.  There's no softening here, so shit will get crazy if the particles get too close
        f_mag = - c * p1.charge * p2.charge / (r**2. + self.softening**2.)

        # Return array 
        return f_mag * vec_r / r
        
    def solve(self, idx):
        """Solve for the accelleration on particle p[idx]."""
        # This is a direct nbody solver, so we loop over all other particles to find the force on particle[idx]
        for j in range(idx + 1, len(self.particles)):
            f_temp = self.force(constants.G, self.particles[idx], self.particles[j]) * self.time_step
            # v(t+dt) = v(t) + a*dt
            self.particles[idx].vel += f_temp / self.particles[idx].charge
            # Newton's 3rd law allows us to update the bottom triangle in the particle-particle matrix simultaneous with the top
            self.particles[j].vel -= f_temp / self.particles[j].charge 

        # We can update particle[idx]'s position safely as the influence on particle[j; j>idx] has already been accounted for above
        self.particles[idx].pos += self.particles[idx].vel * self.time_step

        return

