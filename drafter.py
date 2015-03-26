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
	needs=['C', '1B', '2B', '3B','SS','OF', 'U', 'P']):
		self.hit = hit
		self.bid = bid
		self.roster = roster
		self.hit_roster = hit_roster
		self.pitch_roster = pitch_roster
		self.cap = cap
		self.needs = needs
		
	
#write draft function
def draft():
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
			
			x+=1
			
		

		
		
		
Team1 = Team(hit=.5,cap=.2)
Team2 = Team(hit=.5,cap=.2)
Team3 = Team(hit=.5,cap=.2)
Team4 = Team(hit=.5,cap=.2)
Team5 = Team(hit=.5,cap=.2)
Team6 = Team(hit=.5,cap=.2)
Team7 = Team(hit=.5,cap=.2)
Team8 = Team(hit=.5,cap=.2)
team_list = [Team1, Team2, Team3, Team4, Team5, Team6, Team7, Team8]

draft()

#print(Team7.roster)