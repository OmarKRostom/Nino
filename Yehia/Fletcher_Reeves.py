#!usr/bin/env python
import numpy as np
from numpy.linalg import inv
from sympy import *
import math

#creating basic variables; x and y and l=lambda
x, y, l = symbols('x y l', real=True)

#gradient vector (delta f) of the input function
deltaF = np.array([0,0])

#given a function and the variables in it; x and y, return the value of that function
def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

#given a function and 2 variables, substitute the x and y in the function with the given variables
def subF(function,X,Y):
	return function.subs({x:X,y:Y})

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

#given a function, return the derivative of that function
def derivative(function):
	return diff(function)

#given a function, solve the function in terms of lambda
def solveEqn(function):
	return solve(function,l)

#given 2 matrices; matrix1 and matrix2, return |matrix1|^2 / |matrix2|^2	
def getMagnitudes(matrix1,matrix2):
	 magnitudeOfMatrix1=math.pow(matrix1[0],2)+math.pow(matrix1[1],2)
	 magnitudeOfMatrix2=math.pow(matrix2[0],2)+math.pow(matrix2[1],2)
	 return magnitudeOfMatrix1/magnitudeOfMatrix2


def main():

	#function to be evaluated (user defined)
	function=6*(x**2)-6*x*y+2*(y**2)-x-2*y	
	#intial condition (user defined)
	intialCondition = np.array([0,0])
	#number of iterations (user defined) 
	numberOfIterations=2
	#maximum or minimum; 1 for maximize or -1 for minimize (user defined) 
	MaxMinFlag=-1 

	gradientF(function)
	pointOld=intialCondition
			
	for i in range(numberOfIterations):
		print("Iteration number "+ str(i+1) +" : ")
		if i==0:
			partialGradNew=partialGradient(pointOld[0],pointOld[1])
			directionNew=MaxMinFlag*partialGradNew			
		else:
			partialGradNew=partialGradient(pointOld[0],pointOld[1])
			directionNew=(MaxMinFlag*partialGradNew)+(getMagnitudes(partialGradNew,partialGradOld)*directionOld)

		pointNew=pointOld + l*directionNew
		functionWithLamda=subF(function,pointNew[0],pointNew[1])
		dFunctionWithLamda=derivative(functionWithLamda)
		lamda=solveEqn(dFunctionWithLamda)
		pointNew=pointOld+(lamda*directionNew) 	
		
		pointOld=pointNew
		directionOld=directionNew
		partialGradOld=partialGradNew

		print "Point",(i+1)," : ",pointNew
		   	
	print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	

if __name__=="__main__":
	main()