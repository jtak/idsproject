import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = 0.8

data = pd.read_csv('./resources/daily_averages2014.csv')
plt.plot(data['Mannerheimintie'], color = 'red')
data = pd.read_csv('./resources/daily_averages2015.csv')
plt.plot(data['Mannerheimintie'], color = 'blue',alpha = a)
data = pd.read_csv('./resources/daily_averages2016.csv')
plt.plot(data['Mannerheimintie'], color = 'black', alpha = a)
data = pd.read_csv('./resources/daily_averages2017.csv')
plt.plot(data['Mannerheimintie'], color = 'green', alpha = a)
plt.savefig('testikuva.pdf')
plt.show()