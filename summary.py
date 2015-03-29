import pickle
import matplotlib.pyplot as plt

data = open('10000_victors.pk1', 'rb')
victors = pickle.load(data)
data.close()
	
hit = []
cap = []

for win in victors:
	hit.append(win[1])
	cap.append(win[2])
	
'''n, bins, patches = plt.hist(hit, 50, normed = 1, facecolor='g', alpha=.75)

plt.xlabel('Hit')
plt.ylabel('Probablilty')
plt.title('Histogram of Hit %')
plt.grid(True)
plt.show()'''

plt.plot(hit,cap,'ro')
plt.xlabel('Hit')
plt.ylabel('Cap')

plt.show()