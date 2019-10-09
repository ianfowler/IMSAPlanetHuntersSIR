import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

temp = pd.read_csv('KeplerFinal.txt')
temp = temp.dropna().sort_values(by=['Teff'])
data = list(temp['Teff'])

binTempArr = [data[0]]

lastTemp = 0
numIndicies = 0

minTempDifference = 100
minNumIndicies = 100


for i in range(0,len(data)):
	numIndicies += 1
	if data[i] - lastTemp >= minTempDifference and numIndicies >= minNumIndicies:
		lastTemp = data[i]
		binTempArr.append(lastTemp)
		numIndicies = 0

plt.hist(data, edgecolor='white', bins=binTempArr)
plt.xlabel("Temperature of Star (K)")
plt.ylabel("Frequency")
plt.title("Temperatures of Stars from the Kepler Dataset")
plt.show()


