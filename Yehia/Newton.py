#!usr/bin/env python
import numpy as np 
from numpy.linalg import inv
from sympy import *

#creating basic variables; x and y 
x, y = symbols('x y', real=True)

#gradient vector (delta f) of the input function
deltaF = np.array([0,0])

#given a function and the variables in it; x and y, return the value of that function
def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

#given a function, set the gradient (delta f) of that function 
def gradientF(function):
	fx=diff(function,x)
	fy=diff(function,y)
	global deltaF
	deltaF=np.array([fx,fy])

#given 2 points x and y, return the value of the gradient matrix at these points(delta f1)
def partialGradient(X,Y):
	global deltaF
	partial= np.array([deltaF[0].evalf(subs={x:X,y:Y}),deltaF[1].evalf(subs={x:X,y:Y})])
	return partial

#return the inverse of the hessian matrix of the input function
def getInverseOfHessianMatrix(X,Y):
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
	#function to be evaluated (user defined)
	function=6*(x**2)-6*x*y+2*(y**2)-x-2*y
	#intial condition (user defined)
	intialCondition = np.array([0,0])
	#number of iterations (user defined)
	numberOfIterations=1

	gradientF(function)
	pointOld=intialCondition
		
	for i in range(numberOfIterations):
		print("Iteration number "+ str(i+1) +" : ")
		pointNew = pointOld - (partialGradient(pointOld[0],pointOld[1]).dot(getInverseOfHessianMatrix(pointOld[0],pointOld[1])))
		pointOld = pointNew
		print "Point",(i+1)," : ",pointNew   
	
	print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	
if __name__=="__main__":
	main()