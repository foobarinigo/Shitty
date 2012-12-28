Shitty
======

A (shitty) n-body gravity solver written in python
Requires vPython and numPy

Psuedocode

main():
  
  ## This object represents a single body
  class object:
    charge
    position
    velocities
    
  ## This object holds all the bodies
  list = []
    
  ## This object holds important dyamic information
  class dynamics411:
    catalog of distances
    catalog of forces
    minimum_distance
    time_step
    coupling constant
    Iteration_number
    Max_iterations
    
  ## Add stuff to simulation
  # now
  Add specified objects to list
  # later
  For each object in text_file, add to list
  
  ## Do physics
  For each object in list:
    Compute distances
    Compute local accelleration field
    Update object's acceleration
    Update object's velocity with last time step (store in iterable container)
    Display
    
  Find minimum v*delta_t
    if min(v*delta_t) ~ min(distance)
    Go back and update velocities
    Update positions
    
    
  
