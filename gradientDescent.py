import numpy as np
from numpy.linalg import inv
from sympy import *
import math
import plot

xArr = []
yArr = []

#CREATING BASIC SYMBOLS AND VARIABLES
x = symbols('x')
y = symbols('y')
l = symbols('l')

#DIFFERENTIATION FUNCTION
def deffFunctionXY(function):
	fx = diff(function,x)
	fy = diff(function,y)
	return [fx,fy]

def solveEqn(function,MaxMinFlag):
	lamda=solve(function,l,check=False)
	realvalue=complex(lamda[0]).real
	for i in range(len(lamda)):		
		temp=complex(lamda[i]).real
		if MaxMinFlag==1:
			if realvalue<temp:
				realvalue=complex(lamda[i]).real
		else:
			if realvalue>temp:
				realvalue=complex(lamda[i]).real
	return realvalue

def deffFunctionOfVar(function,var):
	return diff(function,var)

#MAIN EXECUTABLE
def main():
	function = 10.2+(x**2-10*cos(2*(22/7)*x))+(y**2-10*cos(2*(22/7)*y))
	deltaF = deffFunctionXY(function)
	maxMinFlag = -1 #-1 is MIN , 1 is MAX
	iterationFlag = 0 #1 is iteration enabled, 0 is stopping criteria enabled
	startPoint = [1,1]
	iterations = 1000
	oldPoint = np.array(startPoint)
	res = []
	roundVal = 5
	for i in range(iterations):
		valueOfDelta = np.array([deltaF[0].evalf(subs={x:oldPoint[0],y:oldPoint[1]}),deltaF[1].evalf(subs={x:oldPoint[0],y:oldPoint[1]})])
		lambdaEquation = oldPoint + maxMinFlag * l * valueOfDelta
		lambdaEvaluation = function.subs({x:lambdaEquation[0],y:lambdaEquation[1]})
		diffOfLambda = deffFunctionOfVar(lambdaEvaluation,l)
		print(valueOfDelta)
		lambdaF = solveEqn(diffOfLambda,l)
		newPoint = oldPoint + maxMinFlag * valueOfDelta * lambdaF
		oldPoint = newPoint
		res.append(oldPoint)
		stoppintcirteria = np.array([round(deltaF[0].evalf(subs={x:oldPoint[0],y:oldPoint[1]}),roundVal),round(deltaF[1].evalf(subs={x:oldPoint[0],y:oldPoint[1]}),roundVal)])
		xArr.append(newPoint[0])
		yArr.append(newPoint[1])
		if iterationFlag==0:
			if all(v==0 for v in stoppintcirteria):
				print "OPTIMUM REACHED !"
				break
		print "Iteration point" , str(i+1) , " is" , newPoint
	plot.plot3D(xArr,yArr)
	return res

#MAIN CALLER
if __name__=="__main__":
	main()