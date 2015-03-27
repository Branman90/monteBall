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
 #how to make the amount of money bid equal to cap times hit % of money?????
 #
 
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
	needs = None, money= None, hit_money = None, pitch_money = None):
		if roster is None: roster = []
		if hit_roster is None: hit_roster = []
		if pitch_roster is None: pitch_roster = []
		if needs is None: needs = ['C', '1B', '2B', '3B','SS','OF', 'U', 'P']
		if money is None: money = 250
		if hit_money is None: hit_money = (money*hit)
		if pitch_money is None: pitch_money= (money*(1-hit))
		
		self.hit = hit
		self.roster = roster
		self.hit_roster = hit_roster
		self.pitch_roster = pitch_roster
		self.cap = cap
		self.needs = needs
		self.money = money
		self.hit_money = hit_money
		self.pitch_money = pitch_money
		
	
def checkNeed(team):
	if team.hit_roster.count('C') == 2 and 'C' in team.needs:
		del team.needs[team.needs.index('C')]
	if team.hit_roster.count('1B')==2 and '1B' in team.needs:
		del team.needs[team.needs.index('1B')]
	if team.hit_roster.count('2B') == 2 and '2B' in team.needs:
		del team.needs[team.needs.index('2B')]
	if team.hit_roster.count('SS') == 1 and 'SS' in team.needs:
		del team.needs[team.needs.index('SS')]
	if team.hit_roster.count('3B') == 1 and '3B' in team.needs:
		del team.needs[team.needs.index('3B')]
	if team.hit_roster.count('OF') == 4 and 'OF' in team.needs:
		del team.needs[team.needs.index('OF')]
	if team.hit_roster.count('U') == 4 and 'U' in team.needs:
		del team.needs[team.needs.index('U')]
	if team.pitch_roster.count('P') == 10 and 'P' in team.needs:
		del team.needs[team.needs.index('P')]
		
	
	
def hit_auction():
	player = avail_hit[1]
	position = avail_hit[1][8]
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
	
	#print(TeamA.hit_money)
	
	
	
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
	print(TeamG.pitch_money)			
		
	
			
TeamA = Team(hit=.5,cap=.2)
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
	
for line in TeamA.roster:
	print(line)

#for line in TeamB.roster:
#	print(line)