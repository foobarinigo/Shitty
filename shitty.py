# J. Morgan
# 12/27/2012
# shitty.py - a shitty n-body program

from nbody_gravity import *

# SI units
m_sun = 1.9891e30
m_earth = 5.97219e24
m_moon = 7.34767309e22
m_mercury = 0.055 * m_earth
m_venus = .8150 * m_earth
m_mars = .107 * m_earth
m_jupiter = 317.8 * m_earth
m_saturn = 95.3 * m_earth
m_uranus = 14.6 * m_earth
m_neptune = 17.23 * m_earth

r_sun = 6.955e8
r_earth = 6.3781e6
r_moon = 1.7374e6
r_mercury = .382 * r_earth
r_venus = .949 * r_earth
r_mars = .532 * r_earth
r_jupiter = 11.19 * r_earth
r_saturn = 9.26 * r_earth
r_uranus = 4.01 * r_earth
r_neptune = 3.88 * r_earth

AU = 149597870700
d_moon = .0025 * AU
d_mercury = .387 * AU
d_venus = .723 * AU
d_mars = 1.524 * AU
d_jupiter = 5.203 * AU
d_saturn = 9.529 * AU
d_uranus = 19.19 * AU
d_neptune = 30.06 * AU

v_mercury = 4.79e4
v_venus = 3.5e4
v_earth = 2.98e4
v_mars = 2.41e4
v_jupiter = 1.31e4
v_saturn = 9.6e3
v_uranus = 6.8e3
v_neptune = 5.4e3

# Circular velocity speeds
# v_earth = sqrt(constants.G * m_sun / AU)
# v_moon = sqrt(constants.G * m_earth / d_moon)

sun = vparticle(m_sun, [0., 0., 0.], [0., 0., 0.], 50. * r_sun, color.yellow)
earth = vparticle(m_earth, [AU, 0., 0.], [0., v_earth, 0.], r_sun, color.blue)
mercury = vparticle(m_mercury, [d_mercury, 0., 0.], [0., v_mercury, 0.], .382 * r_sun, color.red)
venus = vparticle(m_venus, [d_venus, 0., 0.], [0., v_venus, 0.], .949 * r_sun, color.orange)
mars = vparticle(m_mars, [d_mars, 0., 0.], [0., v_mars, 0.], .532 * r_sun, color.red)
jupiter = vparticle(m_jupiter, [d_jupiter, 0., 0.], [0., v_jupiter, 0.], 11.19 * r_sun, color.orange)
saturn = vparticle(m_saturn, [d_saturn, 0., 0.], [0., v_saturn, 0.], 9.26 * r_sun, color.yellow)
uranus = vparticle(m_uranus, [d_uranus, 0., 0.], [0., v_uranus, 0.], 4.01 * r_sun, color.green)
neptune = vparticle(m_neptune, [d_neptune, 0., 0.], [0., v_neptune, 0.], 3.88 * r_sun, color.blue)

# Setup the camera
scene.range = 1.5 * AU
scene.forward = (AU, .1 * AU, -.5 * AU)
#label(pos = (0, -.025, 0), text = "Camera position: %1.5f %1.5f %1.5f" % (scene.forward[0], scene.forward[1], scene.forward[2]))

# Can't see it anyway 
# moon = vparticle(m_moon, [AU + d_moon, 0., 0.], [0., v_earth + v_moon, 0.], 10. * r_moon, color.white)

shitty = nbody_gravity(1000)
shitty.time_step = 43200 # .5 Day
shitty.add_particle(sun)
shitty.add_particle(earth)
shitty.add_particle(mercury)
shitty.add_particle(venus)
shitty.add_particle(mars)
shitty.add_particle(jupiter)
shitty.add_particle(saturn)
shitty.add_particle(uranus)
shitty.add_particle(neptune)
shitty.go()
