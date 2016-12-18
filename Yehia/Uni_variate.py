#!usr/bin/env python
import numpy as np
from numpy.linalg import inv
from sympy import *
import math

x, y, l = symbols('x y l', real=True)
deltaF = np.array([0,0])


def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

def subF(function,X,Y):
	return function.subs({x:X,y:Y})

def deltaPartial(function):
	fx=diff(function,x)
	fy=diff(function,y)
	global deltaF
	deltaF=np.array([fx,fy])

def partialDerivative(X,Y):
	global deltaF
	partial= np.array([deltaF[0].evalf(subs={x:X,y:Y}),deltaF[1].evalf(subs={x:X,y:Y})])
	return partial

def derivative(function):
	return diff(function)

def solveEqn(function):
	return solve(function,l)

	'''
	temp = solve(function,x)
	seko1=temp[0]
	seko = seko1.evalf(subs={y:1})
	print seko
	#print seko
	'''
def getMagnitudes(arr1,arr2):
	 magnitudeOfDeltaF1=math.pow(arr1[0],2)+math.pow(arr1[1],2)
	 magnitudeOfDeltaF2=math.pow(arr2[0],2)+math.pow(arr2[1],2)
	 return magnitudeOfDeltaF1/magnitudeOfDeltaF2


def main():

	function=6*(x**2)-6*x*y+2*(y**2)-x-2*y	#function to be evaluated (user defined)

	intialCondition = np.array([0,0]) #intial condition (user defined)
	numberOfIterations=4 #number of iterations (user defined)
	MaxMinFlag=-1 #1 for maximize or -1 for minimize (user defined)
	probLength=0.01 #(user defined)

	deltaPartial(function)
	pointOld=intialCondition
			
	for i in range(numberOfIterations):
		print("Iteration number "+ str(i+1) +" : ")
		if (i%2==0):
			direction=np.array([1,0])
		else: 
		 	direction=np.array([0,1])	

		#testFunction = f(pointOld[0],pointOld[1])
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