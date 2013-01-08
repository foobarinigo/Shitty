# J. Morgan
# 12/27/2012
# cold_collapse.py - virialization of a cold cluster

from nbody_gravity import *

# Useful constants (SI)
m_sun = 1.9891e30
r_sun = 6.955e8
AU = 1.4959e11
pc = 3.0856e16

# Simulation parameters
num_stars = 5e2
star_mass = m_sun
# Draw each star as a curve so we don't have to waste so much time on lighting tiny spheres
star_radius = 0.
cluster_radius = 100 * pc
random.seed(12345)

scene.range = 1.5 * cluster_radius
cluster_mass = num_stars * star_mass
cluster_density = cluster_mass / (4. / 3. * pi * cluster_radius**3)
# Crossing time of the cluster when it's virialized (roughly).
cluster_timescale = cluster_radius**1.5 / sqrt(constants.G * cluster_mass)

# 1000 timesteps, 1 parsec of softening distance
cold_collapse = nbody_gravity(100, pc)
cold_collapse.time_step = (.01 * cluster_timescale)

# Populate our box with stars
total_mass = 0.0
while(total_mass < cluster_mass):
    if( random.random() * star_mass / pc**3 < cluster_density ):
        total_mass += star_mass
        # distribute the particles in a sphere of radius rand_radius
        rand_radius = cluster_radius * random.random()
        rand_phi = 2. * pi * random.random()
        rand_theta = pi * random.random()
        rand_position = rand_radius * array([sin(rand_theta) * cos(rand_phi), sin(rand_theta) * sin(rand_phi), cos(rand_theta)])
        rand_star = vparticle(star_mass, rand_position, [0., 0., 0.], star_radius, color.white)
        # Add the star to the simulation
        cold_collapse.add_particle(rand_star)

print "Entering simulation"
cold_collapse.go()
cold_collapse.dump()
