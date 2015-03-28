import pickle

data = open('10000_victors.pk1', 'rb')
victors = pickle.load(data)
data.close()
	
hit = []

for win in victors:
	hit.append(win[1])
	
print(len(hit))
print(max(hit))
print(min(hit))
print(sum(hit)/10001)