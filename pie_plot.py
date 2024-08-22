import matplotlib.pyplot as plt
india = [1, 20, 27, 35, 40, 45, 50]
srilanka = [1, 1, 6, 160, 161, 162, 206]
overs = [0, 10, 40, 65, 89, 160, 200]
plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1)
plt.pie(india, labels=overs, startangle=140, radius=0.7)
plt.title('India Performance')
plt.subplot(1, 2, 2)
plt.pie(srilanka, labels=overs, startangle=140, radius=0.7) 
plt.title('Sri Lanka Performance')
plt.show()
