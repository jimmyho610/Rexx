%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# This is a custom matplotlib style that I use for most of my charts
# plt.style.use('tableau10.mplstyle')

child_data = pd.read_csv('child.csv')
child_data.head()
