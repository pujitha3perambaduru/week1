from matplotlib import pyplot as plt
import numpy as np
cars = ['AUDI', 'BMW', 'FORD',
        'toyota', 'HONDA', 'suzuki']
data = [20, 15, 45, 10, 39, 17]
fig = plt.figure(figsize=(10, 3))
plt.pie(data, labels=cars)
plt.show()
