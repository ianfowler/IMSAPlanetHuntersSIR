import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

temp = pd.read_csv('KeplerFinal.txt')
temp = temp.dropna()


plt.hist(temp['Teff'], bins=400)
plt.show()





