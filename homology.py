from __future__ import division
from pylab import *

A = []
b = []

# A - radius, luminosity, temperature, pressure, density, opacity, energy generation
# b - mass

#A.append([ 0, 0,-1, 1,-1, 0, 0]); b.append( 0); # Ideal gas pressure
A.append([ 0, 0,-4, 1, 0, 0, 0]); b.append( 0); # Radiation pressure
#A.append([ 0, 0, 0, 1,-5/3, 0, 0]); b.append( 0); # Polytrope

A.append([ 4,-1, 4, 0, 0,-1, 0]); b.append( 1); # Radiative diffusion
#A.append([ 1, 0, 1, 0, 0, 0, 0]); b.append( 1); # Convection

A.append([ 0, 0, 0, 0, 0, 1, 0]); b.append( 0); # Thomson scattering
#A.append([ 0, 0,3.5, 0,-1, 1, 0]); b.append( 0); # Kramers opacity

#A.append([ 0, 0,-4, 0,-1, 0, 1]); b.append( 0); # pp-chain
A.append([ 0, 0,-15, 0,-1, 0, 1]); b.append( 0); # CNO cycle

A.append([ 3, 0, 0, 0, 1, 0, 0]); b.append( 1); # mass continuity
A.append([ 1, 0, 0, 1,-1, 0, 0]); b.append( 1); # hydrostatic equilibrium
A.append([-3, 1, 0, 0,-1, 0,-1]); b.append( 0); # energy conservation

A = array(A)
b = array(b)

print A
print b
print linalg.solve(A,b)

