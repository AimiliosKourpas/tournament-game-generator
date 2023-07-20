
print("Welcome to the tournament game generator")

def get_number_of_teams():
    while True:
        num_teams = int(input("Enter number of teams in the tournament: "))
        if num_teams >= 2:
            break
       
        print("The minimum number of teams is 2, try again.")
    return num_teams

def get_team_names(num_teams):
    teams = []
    for i in range(num_teams):
        while True:
            name_of_team = input(f"Enter name of team #{i+1}: ") 
            number_of_words = len(name_of_team.split(" ")) # the default split is " " so we don't need to specify it
            if number_of_words > 2:
                print("Team names may have at most 2 words, try again.")
            elif len(name_of_team) < 2:
                print("Team names must have at least 2 character, try again.")
            else:
                break
             
        teams.append(name_of_team)
        
    return teams

def get_number_of_games(num_teams):
    while True:
        num_games = int(input("Enter the number of games played by each team:"))
        if num_games >= num_teams-1:
            break
           
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        
    return num_games

def number_of_wins(teams, num_games):
    team_wins = []

    for team in teams:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))

            if wins > num_games:
                print(f"The maximum number of wins is {num_games}, try again.")
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                break

        team_wins.append((team, wins))

    return team_wins


def get_second_item(item):
    return item[1]
    
    
    

num_teams = get_number_of_teams()
teams = get_team_names(num_teams)
games = get_number_of_games(num_teams)
wins = number_of_wins(teams, games)


print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(wins, key=get_second_item)
game_pairings = []

games_to_make = len(sorted_teams)//2

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0]
    away_team = sorted_teams[num_teams - 1 - game_num][0]
    game_pairings.append([home_team, away_team])

for pairing in game_pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")
    
# NOTES FOR VALIDATION 

#The vailidate is simple
#While loop thats true 
#inside it we have input user
#we have an if statement that checks if the condition is true
#if its true we break out of the loop 
#if not the loop continues until the condition is true