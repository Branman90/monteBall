#this file will simulate the draft of a League
import csv
import pickle

hit_data = open('hit_data.pk1', 'rb')
avail_hit = pickle.load(hit_data)
hit_data.close()

pitch_data = open('pitch_data.pk1', 'rb')
avail_pitch = pickle.load(pitch_data)
pitch_data.close()

 #need to develop draft program 
 #make analyzer that shows wich team has the best stats
 #
 
def stat_sum():	
	allw=[];allera=[];allsv=[];allip=[];allso=[];allwhip=[]
	allhr=[];allr=[];allrbi=[];allsb=[];allave=[];allobp=[]
	for team in team_list:
		pitch = []
		hit = []
		roster = team.roster
		w=0; era=0; sv=0; ip=0; so=0; whip=0
		hr=0; r=0; rbi=0; sb=0; ave=0; obp=0
		for player in team.roster:			 
			if player[8] == 'P':
				pitch.append(player[2:8])	
			else:
				hit.append(player[2:9])
				
		for line in pitch:
			w = w + int(line[0])
			era = era + float(line[1])/int(line[3])
			sv = sv + int(line[2])
			ip = ip + int(line[3])
			so = so + int(line[4])			
			whip = whip + float(line[5])/int(line[3])
		team.stats.append([w,era,sv,ip,so,whip])
		#print(team.stats)
		allw.append(w)
		allera.append(era)
		allsv.append(sv)
		allip.append(ip)
		allso.append(so)
		allwhip.append(whip)
		
		for line in hit:
			hr = hr + int(line[1])
			r = r + int(line[2])
			rbi = rbi + int(line[3])
			sb = sb + int(line[4])
			ave = ave + float(line[5])*int(line[0])
			obp = obp + float(line[6])*int(line[0])
		team.stats.append([hr,r,rbi,sb,ave,obp])
		allhr.append(hr)
		allr.append(r)
		allrbi.append(rbi)
		allsb.append(sb)
		allave.append(ave)
		allobp.append(obp)
	#print(sorted(allsv))
	for team in team_list:
		if team.stats[0][0] == sorted(allw)[0]:
			team.points+=1
		elif team.stats[0][0] == sorted(allw)[1]:
			team.points+=2
		elif team.stats[0][0] == sorted(allw)[2]:
			team.points+=3
		elif team.stats[0][0] == sorted(allw)[3]:
			team.points+=4
		elif team.stats[0][0] == sorted(allw)[4]:
			team.points+=5
		elif team.stats[0][0] == sorted(allw)[5]:
			team.points+=6
		elif team.stats[0][0] == sorted(allw)[6]:
			team.points+=7
		elif team.stats[0][0] == sorted(allw)[7]:
			team.points+=8
			
		if team.stats[0][1] == sorted(allera, reverse=True)[0]:
			team.points+=1
		elif team.stats[0][1] == sorted(allera, reverse= True)[1]:
			team.points+=2
		elif team.stats[0][1] == sorted(allera, reverse= True)[2]:
			team.points+=3
		elif team.stats[0][1] == sorted(allera, reverse= True)[3]:
			team.points+=4
		elif team.stats[0][1] == sorted(allera, reverse= True)[4]:
			team.points+=5
		elif team.stats[0][1] == sorted(allera, reverse= True)[5]:
			team.points+=6
		elif team.stats[0][1] == sorted(allera, reverse= True)[6]:
			team.points+=7
		elif team.stats[0][1] == sorted(allera, reverse= True)[7]:
			team.points+=8
		
		if team.stats[0][2] == sorted(allsv)[0]:
			team.points+=1
		elif team.stats[0][2] == sorted(allsv)[1]:
			team.points+=2
		elif team.stats[0][2] == sorted(allsv)[2]:
			team.points+=3
		elif team.stats[0][2] == sorted(allsv)[3]:
			team.points+=4
		elif team.stats[0][2] == sorted(allsv)[4]:
			team.points+=5
		elif team.stats[0][2] == sorted(allsv)[5]:
			team.points+=6
		elif team.stats[0][2] == sorted(allsv)[6]:
			team.points+=7
		elif team.stats[0][2] == sorted(allsv)[7]:
			team.points+=8
			
		if team.stats[0][3] == sorted(allip)[0]:
			team.points+=1
		elif team.stats[0][3] == sorted(allip)[1]:
			team.points+=2
		elif team.stats[0][3] == sorted(allip)[2]:
			team.points+=3
		elif team.stats[0][3] == sorted(allip)[3]:
			team.points+=4
		elif team.stats[0][3] == sorted(allip)[4]:
			team.points+=5
		elif team.stats[0][3] == sorted(allip)[5]:
			team.points+=6
		elif team.stats[0][3] == sorted(allip)[6]:
			team.points+=7
		elif team.stats[0][3] == sorted(allip)[7]:
			team.points+=8
		
		if team.stats[0][4] == sorted(allso)[0]:
			team.points+=1
		elif team.stats[0][4] == sorted(allso)[1]:
			team.points+=2
		elif team.stats[0][4] == sorted(allso)[2]:
			team.points+=3
		elif team.stats[0][4] == sorted(allso)[3]:
			team.points+=4
		elif team.stats[0][4] == sorted(allso)[4]:
			team.points+=5
		elif team.stats[0][4] == sorted(allso)[5]:
			team.points+=6
		elif team.stats[0][4] == sorted(allso)[6]:
			team.points+=7
		elif team.stats[0][4] == sorted(allso)[7]:
			team.points+=8
			
		if team.stats[0][5] == sorted(allwhip, reverse=True)[0]:
			team.points+=1
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[1]:
			team.points+=2
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[2]:
			team.points+=3
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[3]:
			team.points+=4
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[4]:
			team.points+=5
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[5]:
			team.points+=6
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[6]:
			team.points+=7
		elif team.stats[0][5] == sorted(allwhip, reverse= True)[7]:
			team.points+=8
			
		if team.stats[1][0] == sorted(allhr)[0]:
			team.points+=1
		elif team.stats[1][0] == sorted(allhr)[1]:
			team.points+=2
		elif team.stats[1][0] == sorted(allhr)[2]:
			team.points+=3
		elif team.stats[1][0] == sorted(allhr)[3]:
			team.points+=4
		elif team.stats[1][0] == sorted(allhr)[4]:
			team.points+=5
		elif team.stats[1][0] == sorted(allhr)[5]:
			team.points+=6
		elif team.stats[1][0] == sorted(allhr)[6]:
			team.points+=7
		elif team.stats[1][0] == sorted(allhr)[7]:
			team.points+=8
		
		if team.stats[1][1] == sorted(allr)[0]:
			team.points+=1
		elif team.stats[1][1] == sorted(allr)[1]:
			team.points+=2
		elif team.stats[1][1] == sorted(allr)[2]:
			team.points+=3
		elif team.stats[1][1] == sorted(allr)[3]:
			team.points+=4
		elif team.stats[1][1] == sorted(allr)[4]:
			team.points+=5
		elif team.stats[1][1] == sorted(allr)[5]:
			team.points+=6
		elif team.stats[1][1] == sorted(allr)[6]:
			team.points+=7
		elif team.stats[1][1] == sorted(allr)[7]:
			team.points+=8
		
		if team.stats[1][2] == sorted(allrbi)[0]:
			team.points+=1
		elif team.stats[1][2] == sorted(allrbi)[1]:
			team.points+=2
		elif team.stats[1][2] == sorted(allrbi)[2]:
			team.points+=3
		elif team.stats[1][2] == sorted(allrbi)[3]:
			team.points+=4
		elif team.stats[1][2] == sorted(allrbi)[4]:
			team.points+=5
		elif team.stats[1][2] == sorted(allrbi)[5]:
			team.points+=6
		elif team.stats[1][2] == sorted(allrbi)[6]:
			team.points+=7
		elif team.stats[1][2] == sorted(allrbi)[7]:
			team.points+=8
		
		if team.stats[1][3] == sorted(allsb)[0]:
			team.points+=1
		elif team.stats[1][3] == sorted(allsb)[1]:
			team.points+=2
		elif team.stats[1][3] == sorted(allsb)[2]:
			team.points+=3
		elif team.stats[1][3] == sorted(allsb)[3]:
			team.points+=4
		elif team.stats[1][3] == sorted(allsb)[4]:
			team.points+=5
		elif team.stats[1][3] == sorted(allsb)[5]:
			team.points+=6
		elif team.stats[1][3] == sorted(allsb)[6]:
			team.points+=7
		elif team.stats[1][3] == sorted(allsb)[7]:
			team.points+=8
			
		if team.stats[1][4] == sorted(allave)[0]:
			team.points+=1
		elif team.stats[1][4] == sorted(allave)[1]:
			team.points+=2
		elif team.stats[1][4] == sorted(allave)[2]:
			team.points+=3
		elif team.stats[1][4] == sorted(allave)[3]:
			team.points+=4
		elif team.stats[1][4] == sorted(allave)[4]:
			team.points+=5
		elif team.stats[1][4] == sorted(allave)[5]:
			team.points+=6
		elif team.stats[1][4] == sorted(allave)[6]:
			team.points+=7
		elif team.stats[1][4] == sorted(allave)[7]:
			team.points+=8
		
		if team.stats[1][5] == sorted(allobp)[0]:
			team.points+=1
		elif team.stats[1][5] == sorted(allobp)[1]:
			team.points+=2
		elif team.stats[1][5] == sorted(allobp)[2]:
			team.points+=3
		elif team.stats[1][5] == sorted(allobp)[3]:
			team.points+=4
		elif team.stats[1][5] == sorted(allobp)[4]:
			team.points+=5
		elif team.stats[1][5] == sorted(allobp)[5]:
			team.points+=6
		elif team.stats[1][5] == sorted(allobp)[6]:
			team.points+=7
		elif team.stats[1][5] == sorted(allobp)[7]:
			team.points+=8
		print(team.points)
		
		
#need to add compare of all stats to award point
def rank_stats():
	for team in team_list:
		f=0;s=0;t=0;f=0;ft=0;s=0;st=0;e=0
		for stat in team.stats[1]:
			f = stat
			if stat > f:
				e=st
				st=s
				s=ft
				ft=f
				f=t
				t=s
				s=f
				f=stat
			print(f,s,t,f,ft,s,st,e)
		
def auctionPlayer(name):
	profile = []
	for row in avail_hit:
		if name in row[0]:
			profile.append(row)
		else:
			for row in avail_pitch:
				if name in row[0]:
					profile.append(row)
				else:
					pass
	
	stats = profile[0][2:8]
	position = profile[0][8]
	
	
class Team:
	def __init__(self, hit, cap, roster = None, hit_roster = None, pitch_roster = None, 
	needs = None, money= None, hit_money = None, pitch_money = None, stats = None, points=0):
		if roster is None: roster = []
		if hit_roster is None: hit_roster = []
		if pitch_roster is None: pitch_roster = []
		if needs is None: needs = ['C', '1B', '2B', '3B','SS','OF', 'U', 'P']
		if money is None: money = 250
		if hit_money is None: hit_money = (money*hit)
		if pitch_money is None: pitch_money= (money*(1-hit))
		if stats is None: stats = []
		self.hit = hit
		self.roster = roster
		self.hit_roster = hit_roster
		self.pitch_roster = pitch_roster
		self.cap = cap
		self.needs = needs
		self.money = money
		self.hit_money = hit_money
		self.pitch_money = pitch_money
		self.stats = stats
		self.points=points
		
	
def checkNeed(team):
	if team.hit_roster.count('C') == 1 and 'C' in team.needs:
		del team.needs[team.needs.index('C')]
	if team.hit_roster.count('1B')==2 and '1B' in team.needs:
		del team.needs[team.needs.index('1B')]
	if team.hit_roster.count('2B') == 1 and '2B' in team.needs:
		del team.needs[team.needs.index('2B')]
	if team.hit_roster.count('SS') == 1 and 'SS' in team.needs:
		del team.needs[team.needs.index('SS')]
	if team.hit_roster.count('3B') == 1 and '3B' in team.needs:
		del team.needs[team.needs.index('3B')]
	if team.hit_roster.count('OF') == 4 and 'OF' in team.needs:
		del team.needs[team.needs.index('OF')]
	if team.hit_roster.count('U') == 5 and 'U' in team.needs:
		del team.needs[team.needs.index('U')]
	if team.pitch_roster.count('P') == 10 and 'P' in team.needs:
		del team.needs[team.needs.index('P')]
		
	
	
def hit_auction():
	player = avail_hit[1]
	position = avail_hit[1][9]
	bidders = []
		
	for team in team_list:
		if position in team.needs or 'U' in team.needs:
			bidders.append(team)
			
	if bidders:
		high_bid = bidders[0]
		second_bid = None
		#change the draft bid parameters here
		for team in bidders:
			if(team.cap * team.hit_money) > (high_bid.cap * high_bid.hit_money):
				second_bid = (high_bid.cap * high_bid.hit_money)
				high_bid = team
	
		hm = high_bid.hit_money
		
		if second_bid:
			high_bid.hit_money = hm - second_bid
		else:
			high_bid.hit_money = hm - (high_bid.cap * high_bid.hit_money)
		if position in high_bid.needs:
			high_bid.hit_roster.append(position)
		else:
			high_bid.hit_roster.append('U')
			
		high_bid.roster.append(player)
		drafted.append(position)
		del avail_hit[1]
		checkNeed(high_bid)		

	else:
		del avail_hit[1]
	
		
def pitch_auction():
	player = avail_pitch[1]
	position = 'P'
	bidders = []
	
	for team in team_list:
		if position in team.needs:
			bidders.append(team)
	
	high_bid = bidders[0]
	second_bid = None
	
	for team in bidders:
		if (team.cap *team.pitch_money) > (high_bid.cap * high_bid.pitch_money):
			second_bid = (high_bid.cap * high_bid.pitch_money)
			high_bid = team
			
	m = high_bid.pitch_money
	
	if second_bid:
		high_bid.pitch_money = m - second_bid
	else:
		high_bid.pitch_money = m - (high_bid.cap *high_bid.pitch_money)
	
	high_bid.pitch_roster.append(position)
	high_bid.roster.append(player)
	drafted.append(position)
	del avail_pitch[1]
	checkNeed(high_bid)
	
			
TeamA = Team(hit=.6,cap=.2)
TeamB = Team(hit=.5,cap=.12)
TeamC = Team(hit=.5,cap=.3)
TeamD = Team(hit=.5,cap=.10)
TeamE = Team(hit=.5,cap=.15)
TeamF = Team(hit=.5,cap=.26)
TeamG = Team(hit=.5,cap=.27)
TeamH = Team(hit=.5,cap=.2)
team_list = [TeamA, TeamB, TeamC, TeamD, TeamE, TeamF, TeamG, TeamH]

drafted = []

while len(drafted) < 120:
	hit_auction()
	

while len(drafted) < 200:
	pitch_auction()

#for line in avail_hit:
#	print(line)
	
stat_sum()	
#rank_stats()
#for team in team_list:
#	print(team.needs)


#for line in TeamF.stats:
#	print(line)