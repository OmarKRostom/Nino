#!usr/bin/env python
import numpy as np
from numpy.linalg import inv
from sympy import *


x, y = symbols('x y', real=True)
deltaF = np.array([0,0])

'''
To get derivative
z=diff(f,x)
print(z)
print(z.evalf(subs={x:1,y:1}) )
'''

def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

def deltaPartial(function):
	fx=diff(function,x)
	fy=diff(function,y)
	global deltaF
	deltaF=np.array([fx,fy])

def partialDerivative(X,Y):
	global deltaF
	partial= np.array([deltaF[0].evalf(subs={x:X,y:Y}),deltaF[1].evalf(subs={x:X,y:Y})])
	return partial

def getInverse(X,Y):
	
	fxx=diff(deltaF[0],x)
	xx=float(fxx.evalf(subs={x:X,y:Y}))
	fxy=diff(deltaF[0],y)
	xy=float(fxy.evalf(subs={x:X,y:Y}))

	fyx=diff(deltaF[1],x)
	yx=float(fyx.evalf(subs={x:X,y:Y}))
	fyy=diff(deltaF[1],y)
	yy= float(fyy.evalf(subs={x:X,y:Y}))

	hessain=np.array([[xx,xy],[yx,yy]])
	return inv(hessain)
	
def main():

	function=6*(x**2)-6*x*y+2*(y**2)-x-2*y	#function to be evaluated (user defined)
	intialCondition = np.array([0,0]) #intial condition (user defined)
	numberOfIterations=1 #number of iterations (user defined)

	deltaPartial(function)
	pointOld=intialCondition
		
	for i in range(numberOfIterations):
		print("Iteration number "+ str(i+1) +" : ")
		pointNew = pointOld - (partialDerivative(pointOld[0],pointOld[1]).dot(getInverse(pointOld[0],pointOld[1])))
		pointOld = pointNew   
	
	print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	
if __name__=="__main__":
	main()