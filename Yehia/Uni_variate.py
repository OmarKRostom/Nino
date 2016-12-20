#!usr/bin/env python
import numpy as np
from numpy.linalg import inv
from sympy import *
import math

#creating basic variables; x and y and l=lambda
x, y, l = symbols('x y l', real=True)

#given a function and the variables in it; x and y, return the value of that function
def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

#given a function and 2 variables, substitute the x and y in the function with the given variables
def subF(function,X,Y):
	return function.subs({x:X,y:Y})

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
	numberOfIterations=4
	#maximize or minimize; 1 for maximize or -1 for minimize (user defined) 
	MaxMinFlag=-1
	#probe length e (user defined)
	probLength=0.01

	pointOld=intialCondition
			
	for i in range(numberOfIterations):
		print("Iteration number "+ str(i+1) +" : ")
		if (i%2==0):
			direction=np.array([1,0])
		else: 
		 	direction=np.array([0,1])	

		positivePoint=pointOld+(probLength*direction)
		testFunctionPositive = f(function,positivePoint[0],positivePoint[1])

		negativePoint=pointOld-(probLength*direction)
		testFunctionNegative = f(function,negativePoint[0],negativePoint[1])

		if (MaxMinFlag==1):
			if testFunctionPositive<testFunctionNegative:
				direction = -1*direction	 
		else:
			if testFunctionPositive>testFunctionNegative:
				direction = -1*direction
			
		pointNew=pointOld + l*direction
		functionWithLamda=subF(function,pointNew[0],pointNew[1])
		dFunctionWithLamda=derivative(functionWithLamda)
		lamda=solveEqn(dFunctionWithLamda)
		pointNew=pointOld+(lamda*direction) 	
		
		pointOld=pointNew
		
		print "Point",(i+1)," : ",pointNew
		   	
	print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	

if __name__=="__main__":
	main()