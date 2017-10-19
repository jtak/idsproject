import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = 0.8

data = pd.read_csv('./resources/daily_averages2014.csv')
plt.plot(data['Mannerheimintie'], color = 'red')
plt.show()