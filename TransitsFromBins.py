#This script will start with the inner/outer range of temperature bin and it will find transit time. depth, 
#and orbital period
import random
import math
#Inner orbital radius
def roi(temp):
	num=(0.62817*temp**3)-(1235.15*temp**2)
	return num
#Outer orbital radius
def roo(temp):
	num=(1.52*temp**3)-(2988.75*temp**2)
	return num

def starRadius(temp):
	num=(temp*1.8395*10**5)-3.6169*10**8
	return num

def starMass(temp):
	num=(2.85187*10**22*temp**2)+(3.70772*10**26*temp)-9.76855*10**29
	return num

def transitTime(starRadius,randOrbital,starMass):
	num=2*starRadius*math.sqrt((randOrbital*10**11)/(starMass*6.67))
	return num

def transitDepth(planetRadius,starRadius):
	num=(planetRadius**2)/(starRadius**2)
	return num

def orbitalPeriod(randOrbital,starMass):
	num=(2*math.pi*randOrbital**1.5)*math.sqrt((randOrbital*10^11)/(starMass*6.67))
	return num

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
