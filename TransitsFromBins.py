#This script will start with the inner/outer range of temperature bin and it will find transit time. depth, 
#and orbital period
import random
import math
#Inner orbital radius
def roi(temp):
	return (0.62817*temp**3)-(1235.15*temp**2)
#Outer orbital radius
def roo(temp):
	return (1.52*temp**3)-(2988.75*temp**2)

def starRadius(temp):
	return (temp*1.8395*10**5)-3.6169*10**8

def starMass(temp):
	return (2.85187*10**22*temp**2)+(3.70772*10**26*temp)-9.76855*10**29

def transitTime(starRadius,randOrbital,starMass):
	return (2*starRadius*math.sqrt((randOrbital*10**11)/(starMass*6.67)))

def transitDepth(planetRadius,starRadius):
	return (planetRadius**2)/(starRadius**2)

def orbitalPeriod(randOrbital,starMass):
	return (2*math.pi*randOrbital**1.5)*math.sqrt((randOrbital*10^11)/(starMass*6.67))

def BinAnalysis(inTemp,outTemp):
	midTemp=(inTemp+outTemp)/2

	#Setting variables with the average temperature of the bin

	roi2=roi(midTemp)
	roo2=roo(midTemp)
	randOrbital=random.randint(int(roi2),int(roo2)+1)
	planetRadius=random.randint(3390*10**3,11467*10**3)	
	starRadius2=starRadius(midTemp)
	starMass2=starMass(midTemp)

	#Calculating transit time, depth, and orbital period

	transitTime2=transitTime(starRadius2,randOrbital,starMass2)
	transitDepth2=transitDepth(planetRadius,starRadius2)
	orbitalPeriod2=orbitalPeriod(randOrbital,starMass2)

	#print out

	print(transitTime2)
	print(transitDepth2)
	print(orbitalPeriod2)
