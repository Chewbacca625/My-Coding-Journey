# Problem Statement : Divide a group of 28 into four teams. What are the numbers for all 4 teams?

#teams lists
team0 = []
team1 = []
team2 = []
team3 = []
#looping over the number of the people in the group to get the number on their shirt
for number in range(1,29):
    #assigning the number to one of 4 teams 
    team_number = number % 4
    #these if statements check which team each person's number was assigned to and adds them to their respective team list
    if team_number == 0:
        team0.append(number)
    elif team_number == 1:
        team1.append(number)
    elif team_number == 2:
        team2.append(number)
    elif team_number == 3:
        team3.append(number)
#prints teams 
print(team0)
print(team1)
print(team2)
print(team3)
    