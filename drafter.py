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
 #should have the ability to put player up for acution and have teams bid on 
 #that player until they hit a cap or get to a level that makes drafting him unfavorable
 #Start with auctioned player
 
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
	#print(profile)
	stats = profile[0][2:8]
	#print(stats)
	position = profile[0][8]
	#print(position)
	
class Team:
	def __init__(self, hit, cap, roster = [], hit_roster= [], pitch_roster = [], 
	needs=['C', '1B', '2B', '3B','SS','OF', 'U', 'P'], money =250):
		self.hit = hit
		self.roster = roster
		self.hit_roster = hit_roster
		self.pitch_roster = pitch_roster
		self.cap = cap
		self.needs = needs
		self.money = money
		
	
#write draft function
'''def draft():
	x = 1
	total_need = ['C', '1B', '2B', '3B', 'SS', 'OF', 'U', 'P']
	total_drafted = []
	#all drafting the same players...
	while x <= 200:
		for team in team_list:
			if len(team.hit_roster) < len(team.pitch_roster):
				team.roster.append(avail_hit[1])
				team.hit_roster.append(avail_hit[1][8])
				del avail_hit[1]
				print(avail_hit[1])
			else:
				team.roster.append(avail_pitch[1])
				team.pitch_roster.append(avail_pitch[1][8])
				del avail_pitch[1]
			
			x+=1'''
		
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
		
	
	
def auction():
	player = avail_hit[1]
	position = avail_hit[1][8]
	bidders = []
	
	
	for team in team_list:
		if position in team.needs:
			bidders.append(team)
	high_bid = bidders[0]
	for team in bidders:
		if(team.cap * team.money) > (high_bid.cap * high_bid.money):
			high_bid = team
	print(high_bid.cap)
	m = high_bid.money
	high_bid.money = m - (high_bid.cap *high_bid.money)
		
	high_bid.hit_roster.append(position)
	high_bid.roster.append(player)
	del avail_hit[1]
	checkNeed(high_bid)


		
		
		
Team1 = Team(hit=.5,cap=.21)
Team2 = Team(hit=.5,cap=.22)
Team3 = Team(hit=.5,cap=.23)
Team4 = Team(hit=.5,cap=.24)
Team5 = Team(hit=.5,cap=.25)
Team6 = Team(hit=.5,cap=.26)
Team7 = Team(hit=.5,cap=.27, needs=['C','1B','2B','SS','3B','OF'])
Team8 = Team(hit=.5,cap=.2)
team_list = [Team1, Team2, Team3, Team4, Team5, Team6, Team7, Team8]
auction()

#while loop is not working all players still being added to all teams. 
'''x = 1
while x < 50:
	auction()
	x+=1'''
#print(Team7.roster)
#print(Team5.roster)

#print(Team1.roster)