#This is my geometry analysis code
import numpy
import os

def calculate_distance(atom1,atom2):
    x_distance=atom1[0]-atom2[0]
    y_distance=atom1[1]-atom2[1]
    z_distance=atom1[2]-atom2[2]
    distance=numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance

def bond_check(bond_distance,minimum_value, maximum_value):
    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False

file_location=os.path.join('data','data','water.xyz')

symbols=xyz_file[:,0]
coordinates=xyz_file[:,1:]
coordinates=coordinates.astype(numpy.float)

for numA, atomA in enumerate(coordinates):
    for numB,atomB in enumerate(coordinates):
        if numB<numA:
            distance_AB=calculate_distance(atomA,atomB)
            if bond_check(distance_AB,minimum_value=0, maximum_value=1.5) is True:
                print(F'{symbols[numA]} to {symbols[numB]} : {distance_AB:.3f}')
