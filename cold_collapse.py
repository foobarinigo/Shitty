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
num_stars = 1e2
star_mass = m_sun
star_radius = r_sun
cluster_radius = 100 * pc
random.seed(12345)

scene.range = 1.5 * cluster_radius
cluster_mass = num_stars * star_mass
cluster_density = cluster_mass / (4. / 3. * pi * cluster_radius**3)
# Crossing time of the cluster when it's virialized (roughly).
cluster_timescale = cluster_radius**1.5 / sqrt(constants.G * cluster_mass)

cold_collapse = nbody_gravity(1000)
cold_collapse.time_step = (.01 * cluster_timescale)

# Populate our box with stars
total_mass = 0.0
while(total_mass < cluster_mass):
    if( random.random() * star_mass / pc**3 < cluster_density ):
        total_mass += star_mass
        rand_position = cluster_radius * array([random.random() - .5, random.random() - .5, random.random() - .5])
        rand_star = vparticle(star_mass, rand_position, [0., 0., 0.], star_radius, color.white)
        cold_collapse.add_particle(rand_star)

print "Entering simulation"
cold_collapse.go()
