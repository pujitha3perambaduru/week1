import matplotlib.pyplot as plt
cities = ['ap', 'kerala', 'bangalore', 'punjab']
population = [8.4, 4.0, 2.7, 2.3]  
plt.bar(cities, population)
plt.title('Population of Cities')
plt.xlabel('City')
plt.ylabel('Population (Millions)')
plt.show()
