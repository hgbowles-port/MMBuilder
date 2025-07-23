"""
March Madness Bracket Generator
Version 1: coin flip fill: each game is a perfect 50/50 for each team

Version 2: Added seed consideration: better seeded teams are more likely to win, First Four are still pure 50/50 games
"""

import random ## this is the only library outside of base Python needed here

def play(team1, weight1, team2, weight2): ## this function decides which team wins, with bias towards better seeds
  randVal = random.random()
  weightDiff = abs(weight1 - weight2)

  if weightDiff >= 15:
    decision = 0.05
  elif weightDiff >= 10:
    decision = 0.10
  elif weightDiff >= 5:
    decision = 0.25
  else:
    decision = 0.5

  if weight1 - weight2 >= 0:
    dominant_team = team2
    upset_team = team1
  else:
    dominant_team = team1
    upset_team = team2

  if randVal >= decision:
    return dominant_team
  else:
    return upset_team

def firstFour(fileName): ## runs predictions for the FF teams, stores them to send into the main bracket
  ff = open(fileName)
  f4 = []
  output = []
  for (team) in ff:
    f4.append((team))
  for i in range(0, len(f4), 2):
    output.append(play(f4[i], 0, f4[i+1],0))
  return output

def build(teams): ## compiles the bracket by iterating through each division and plays each team, then reports each round's winner

  roundWinners = []

  for i in range(0, len(teams), 2):
    roundWinners.append(play(teams[i][0], teams[i][1], teams[i+1][0], teams[i+1][1]))

  if len(roundWinners) > 1:
    print("The winners for this round are: ",roundWinners)
    build(roundWinners)
  else:
    print("The Grand Winner is: ",roundWinners) ## End case: one team remains

def main(): ## reads in the text files of teams and seeds and builds the bracket

  input = open("teams.txt")
  round1 = []

  first4 = firstFour("firstFour.txt")

  print("The winners of the First Four are: ", end="")
  for team in first4:
    print(team,end=" ")

  for x in input:
    if (x == "FF South\n"):
      round1.append(first4[0], 16)
    elif (x == "FF Midwest\n"):
      round1.append(first4[1], 16)
    elif (x == "FF East\n"):
      round1.append(first4[2], 16)
    elif (x == "FF West\n"):
      round1.append(first4[3], 16)
    else:
      round1.append(x)
  
  roundNoLines = []
  for (team,weight) in round1:
    roundNoLines.append((team,weight))
  print(build(roundNoLines))

if __name__ == '__main__':
  main()