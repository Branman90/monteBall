import csv
import pickle

with open('raw_data.csv', 'rt') as f:
	reader = csv.reader(f)
	raw_data = list(reader)
exclude = ['Angels', 'Astros', 'Athletics', 'Blue Jays', 'Indians', 
			'Mariners', 'Orioles', 'Rangers', 'Rays','Red Sox','Royals',
			'Tigers','Twins', 'White Sox', 'Yankees', ' ']

with open('C.csv', 'rt') as c:
	reader = csv.reader(c)
	c_data = list(reader)

with open('1B.csv', 'rt') as fb:
	reader = csv.reader(fb)
	fb_data = list(reader)

with open('2B.csv', 'rt') as sb:
	reader = csv.reader(sb)
	sb_data = list(reader)	

with open('SS.csv', 'rt') as ss:
	reader = csv.reader(ss)
	ss_data = list(reader)	
	
with open('3B.csv', 'rt') as tb:
	reader = csv.reader(tb)
	tb_data = list(reader)
	
with open('OF.csv', 'rt') as of:
	reader = csv.reader(of)
	of_data = list(reader)

data = [row for row in raw_data if row[1] not in exclude]

'''for row in data:
	if row[0] == 'Charlie Blackmon':
		print(row)'''

for row in data:
	if row[0] in str(c_data).strip('[]'):
		row.append('C')
	elif row[0] in str(fb_data).strip('[]'):
		row.append('1B')
	elif row[0] in str(sb_data).strip('[]'):
		row.append('2B')
	elif row[0] in str(ss_data).strip('[]'):
		row.append('SS')
	elif row[0] in str(tb_data).strip('[]'):
		row.append('3B')
	elif row[0] in str(of_data).strip('[]'):
		row.append('OF')
		
appender = []

def remove(name):
	for row in data:
		if row[0] == name:
			appender.append(row)

my_file = open('hit_data.pk1', 'wb')
pickle.dump(data, my_file)
my_file.close()
	
	
