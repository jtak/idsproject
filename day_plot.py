import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('./resources/daily_averages2014.csv')
im =plt.imread('Seutukartta3.png')
plt.imshow(im)

colors = ['g','y', 'o', 'r', 'p']
plt.scatter([780],[800], c= 'r' )
plt.axis('off')
plt.savefig("test.png", transparent = True, bbox_inches = 'tight', pad_inches = 0, dpi= 600)