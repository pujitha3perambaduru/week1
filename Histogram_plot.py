import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(100)
plt.hist(data, bins=10, edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
