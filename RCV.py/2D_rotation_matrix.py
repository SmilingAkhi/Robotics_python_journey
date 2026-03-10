import math
import numpy as np
from scipy import linalg, optimize
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from spatialmath.base import sym
from spatialgeometry import *
from roboticstoolbox import *
from machinevisiontoolbox import *
import scipy as scc
from sympy import Symbol, Matrix, simplify
import machinevisiontoolbox.base as mvb


R = rot2(0.3) #creating a 2D matrix with 0.3 rad rotation
trplot2(R) #plots the rotation matrix
#plt.show() #shows the matrix visually using a graph

det_check = np.linalg.det(R) #check the determinant of the matrix using numpy linear algerbry
# print(det_check)

theta = Symbol("theta") #using Sympy to create the theta symbol

R = Matrix(rot2(theta)) #converts numpy 2d matrix to sympy matrix 
simplified = simplify(R * R) #simplify to check orthogonality of the rotation matric 
# print(simplified) 

determinant =  R.det() # determine the determinant of the matrix 
# print(determinant)

determinant_simplified =  R.det().simplify() #determined the determinant to get 1
# print(determinant_simplified)


#relationship between rotation matrix and exponenetial of skew symmetric matrix 

RM = rot2(0.3) # produces a 2 x 2 matrix  
L = scc.linalg.logm(RM) #using scipy to evaluate log of a rotation matrix whiich produces a skew symetric matrix
RMM = scc.linalg.expm(L) #this to evaluate the exponential of Skew symetric matrix to give rotation matrix
S = vex(L) # produces the magnitude of the skew symetric matrix, a digit  
# print(S)
construct_ssm = scc.linalg.expm(skew(S)) #construct a skew symetric matric from the magnitude 
# print(construct_ssm)
# print(L)
y = skew(2)
# print(y)
# print(RMM)

#homogenous transformation matrix for a rotation of 0.3rad 
htm = trot2(0.3)
print(htm)

TA = transl2(1, 2) @ trot2(30, "deg") 
print(TA)
# plotvol2([0,5])
trplot2(TA, frame="A" , color="b")


#reference frame
T0 = transl2(0,0)
trplot2(T0, frame="0", color="k")

#creating another refrence frame with translatio (2, 1)
TB = transl2(2,1)
trplot2(TB, frame="B", color="r")

#composing the two transformation 
TBA =  TA @ TB
trplot2(TBA, frame="AB", color="g")

P = np.array([3,2])
plot_point(P, "ko", text="P")


#rotating a coordinate frame 
plotvol2([-5, 4,-1, 5])

plt.show()








