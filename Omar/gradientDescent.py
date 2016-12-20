import numpy as np
from numpy.linalg import inv
from sympy import *
import math

#CREATING BASIC SYMBOLS AND VARIABLES
x = symbols('x')
y = symbols('y')
l = symbols('l')

#DIFFERENTIATION FUNCTION
def deffFunctionXY(function):
	fx = diff(function,x)
	fy = diff(function,y)
	return [fx,fy]

def deffFunctionOfVar(function,var):
	return diff(function,var)

#MAIN EXECUTABLE
def main():
	function = 6*(x**2)-6*(x*y)+2*(y**2)-x-2*y;
	deltaF = deffFunctionXY(function)
	maxMinFlag = -1 #-1 is MIN , 1 is MAX
	startPoint = [0,0]
	iterations = 4
	oldPoint = np.array(startPoint)
	for i in range(iterations):
		valueOfDelta = np.array([deltaF[0].evalf(subs={x:oldPoint[0],y:oldPoint[1]}),deltaF[1].evalf(subs={x:oldPoint[0],y:oldPoint[1]})])
		lambdaEquation = oldPoint + maxMinFlag * l * valueOfDelta
		lambdaEvaluation = function.subs({x:lambdaEquation[0],y:lambdaEquation[1]})
		diffOfLambda = deffFunctionOfVar(lambdaEvaluation,l)
		lambdaF = solve(diffOfLambda,l)
		newPoint = oldPoint + maxMinFlag * valueOfDelta * lambdaF
		oldPoint = newPoint
		print "Iteration point" , str(i+1) , " is" , newPoint


#MAIN CALLER
if __name__=="__main__":
	main()