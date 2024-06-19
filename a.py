class eachBall:
    def __init__(self, run, wicket):
        self.run = run
        self.wicket = wicket


class Batsman:
    def __init__(self, name, run, ball, four, six, strikerate, wicketBy, runTaken, wicket, economy, balls):
        self.name = name
        self.run = run
        self.ball = ball
        self.four = four
        self.six = six
        self.wicketBy = wicketBy
        self.runTaken = runTaken
        self.wicket = wicket
        self.balls = balls
        self.economy = 0
        
        
class Main:
    def print_scoreboard(self, team_name, team_list, total_runs, bowling_team_list):
        print(f"\n{team_name} Scoreboard:")
        print("Batsmen:")
        print("Player\t\tRuns\tBalls\t4s\t6s")
        for player in team_list:
            print(f"{player.name}\t\t{player.run}\t{player.ball}\t{player.four}\t{player.six}")

        print("\nBowlers:")
        print("Player\t\tOvers\tRuns\tWickets\tEconomy")
        for bowler in bowling_team_list:
            print(f"{bowler.name}\t\t{bowler.balls / 6}\t{bowler.runTaken}\t{bowler.wicket}\t{bowler.economy}")
        print("***************************************************************8")    
        print(f"Total Runs: {total_runs}")
    
        
        
    def determine_winner(self, team1_name, team1_runs, team2_name, team2_runs):
        if team1_runs > team2_runs:
            print(f"\n{team1_name} won by {team1_runs - team2_runs} runs!")
            print(f"{team1_name} scored {team1_runs} runs in the 1st inning and {team2_runs} runs in the 2nd inning.")
        elif team2_runs > team1_runs:
            print(f"\n{team2_name} won by {team2_runs - team1_runs} runs!")
            print(f"{team2_name} scored {team2_runs} runs in the 1st inning and {team1_runs} runs in the 2nd inning.")
        else:
            print("\nThe match ended in a tie!")
            print(f"Both teams scored {team1_runs} runs.")
    
    def play(self):
        team = []
        total=[0,0]
        team.append(input("Enter Name Of Team1: "))
        team.append(input("Enter Name Of Team2: "))
        teamList = []
        teamList.append([])
        teamList.append([])
        print("Enter Players Of", team[0])
        for i in range(1, 5):
            p = Batsman(input("Enter Player Name: "), 0, 0, 0, 0, 0, "", 0, 0, 0, 0)
            teamList[0].append(p)
        print("Enter Players Of", team[1])
        for i in range(1, 5):
            p = Batsman(input("Enter Player Name: "), 0, 0, 0, 0, 0, "", 0, 0, 0, 0)
            teamList[1].append(p)
        battingFirst = int(input(f"\n Which team is batting first \n For {team[0]}: 1  \n For {team[1]}: 2 \n"))
        if (battingFirst == 2):
            temp1 = team[0]
            team[0] = team[1]
            team[1] = temp1
            temp2 = teamList[0]
            teamList[0] = teamList[1]
            teamList[1] = temp2
        playersPlayed = []
        playersPlayed.append([])
        playersPlayed.append([])
        onStrike = 0
        eachBallPlayed = []
        eachBallPlayed.append([])
        eachBallPlayed.append([])
        batNumberPlayed = [0, 1]
        for j in range(0, 4):
            print(f" {teamList[0][j].name} for Enter {j + 1} ")
        while True:
            try:
                batName1 = int(input("Enter Number Of 1st Player: "))
                if batName1 not in range(1, 5):
                    raise ValueError
                if batName1 == "":
                    raise ValueError
                
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        while True:
            try:
                batName2 = int(input("Enter Number Of 2nd Player: "))
                if batName2 not in range(1, 5) or batName2 == batName1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4, and different from the first player.")
        bowl = []

        bat = []
        bat.append(teamList[0][batName1 - 1])
        bat.append(teamList[0][batName2 - 1])
        currentBowlNum = 0
        for i in range(1, 13):

            if (i == 1):
                for j in range(0, 4):
                    print(f" {teamList[1][j].name} for Enter {j + 1} ")
                currentBowlNum = int(input("Enter Bowler No."))
            if (i % 7 == 0):
                print(f"RUN : {currentBowler.runTaken}, WICKET : {currentBowler.wicket}, BALLS : {currentBowler.balls} ")
                for j in range(0, 4):
                    print(f" {teamList[1][j].name} for Enter {j + 1} ")
                currentBowlNum = int(input("Enter Bowler No."))
            currentBowler = teamList[1][currentBowlNum - 1]

            print(f"RUN : {currentBowler.runTaken}, WICKET : {currentBowler.wicket}, BALLS : {currentBowler.balls}")

            while True:
                try:
                    runOnEachBall = int(input(f"Enter Runs Scored On Ball no :{i} "))
                    if runOnEachBall not in range(0, 7):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")
            bat[onStrike].run += runOnEachBall
            bat[onStrike].ball += 1
            total[0]+=runOnEachBall
            currentBowler.runTaken += runOnEachBall
            currentBowler.balls += 1

            if (runOnEachBall == 4):
                bat[onStrike].four += 1
            if (runOnEachBall == 6):
                bat[onStrike].six += 1
            
            if runOnEachBall % 2 != 0:
                onStrike = (onStrike + 1) % 2


            if i == 6 and runOnEachBall % 2 != 0:  # Check if it's the last ball of the over and odd runs scored
                onStrike = (onStrike + 1) % 2  # Switch the strike
            elif i == 6 and runOnEachBall % 2 == 0:  # Check if it's the last ball of the over and even runs scored
                pass                
                
            if (runOnEachBall == 0):
                while True:
                    try:
                        wicketOnEachBall = int(input("Enter 1 If Wicket 0 If Not: "))
                        if wicketOnEachBall not in [0, 1]:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter either 0 or 1.")
                if (wicketOnEachBall == 1):
                    for j in range(0, 4):
                        if (not j in batNumberPlayed):
                            print((j + 1), teamList[0][j].name)
                    while True:
                        try:
                            noAfterWicket = int(input("Enter Number: "))
                            if noAfterWicket not in range(1, 5) or noAfterWicket in batNumberPlayed:
                                raise ValueError
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 and 4, and different from the previous batsman.")
                    bat[onStrike] = teamList[0][noAfterWicket - 1]
                    currentBowler.wicket += 1
                    batNumberPlayed.append(noAfterWicket)
                    
            else:
                wicketOnEachBall = 0
            print(f"BATSMAN : {bat[0].name}, RUN : {bat[0].run}")
            print(f"BATSMAN : {bat[1].name}, RUN : {bat[1].run}")
            eachBallPlayed[0].append(eachBall(runOnEachBall, wicketOnEachBall))
            currentBowler.economy = currentBowler.runTaken * 6 / currentBowler.balls
                       
        self.print_scoreboard(team[0], teamList[0], total[0],teamList[1])
        
        print("\n\nSecond Innings\n\n")

        for j in range(0, 4):
            print(f"{teamList[1][j].name} For Enter {j + 1}")
        while True:
            try:
                batName1 = int(input("Enter Number Of 1st Player: "))
                if batName1 not in range(1, 5):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        while True:
            try:
                batName2 = int(input("Enter Number Of 2nd Player: "))
                if batName2 not in range(1, 5) or batName2 == batName1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4, and different from the first player.")
        bowl = []

        bat = []
        bat.append(teamList[1][batName1 - 1])
        bat.append(teamList[1][batName2 - 1])
        currentBowlNum = 0

        for i in range(1, 13):
            if(total[1]>total[0]):
                break
            if (i == 1):
                for j in range(0, 4):
                    print(f"{teamList[0][j].name} for Enter {j+1}")
                currentBowlNum = int(input("Enter Bowler No."))
            if (i % 7 ==0):
                print(f"\nRUN : {currentBowler.runTaken}, WICKET : {currentBowler.wicket}, BALLS : {currentBowler.balls} \n")
                for j in range(0, 4):
                    print(f"{teamList[0][j].name} for Enter {j+1}")
                currentBowlNum = int(input("Enter Bowler No."))
            currentBowler = teamList[0][currentBowlNum - 1]

            print(
                f"\nRUN : {currentBowler.runTaken}, WICKET : {currentBowler.wicket}, BALLS : {currentBowler.balls} \n")

            runOnEachBall = int(input(f"Enter Runs Scored On Ball no.{i}"))
            bat[onStrike].run += runOnEachBall
            bat[onStrike].ball += 1
            total[1]+=runOnEachBall
            currentBowler.runTaken += runOnEachBall
            currentBowler.balls += 1

            if (runOnEachBall == 4):
                bat[onStrike].four += 1
            if (runOnEachBall == 6):
                bat[onStrike].six += 1
                
            if runOnEachBall % 2 != 0:  # Check if odd runs scored
                onStrike = (onStrike + 1) % 2  # Switch the strike

            if i == 6 and runOnEachBall % 2 != 0:  # Check if it's the last ball of the over and odd runs scored
                onStrike = (onStrike + 1) % 2  # Switch the strike
            elif i == 6 and runOnEachBall % 2 == 0:  # Check if it's the last ball of the over and even runs scored
                pass     
            if (runOnEachBall == 0):
                wicketOnEachBall = int(input("Enter 1 If Wicket 0 If Not: "))
                if (wicketOnEachBall == 1):
                    for j in range(0, 4):
                        if (not j in batNumberPlayed):
                            print((j + 1), teamList[1][j].name)
                    noAfterWicket = int(input("Enter Number: "))
                    bat[onStrike] = teamList[1][noAfterWicket - 1]
                    currentBowler.wicket += 1
                    batNumberPlayed.append(noAfterWicket)
                    
            else:
                wicketOnEachBall = 0
            print(f" BATSMAN : {bat[0].name}, RUN : {bat[0].run}")
            print(f" BATSMAN : {bat[1].name}, RUN : {bat[1].run}"
                  )
            eachBallPlayed[0].append(eachBall(runOnEachBall, wicketOnEachBall))
            currentBowler.economy = currentBowler.runTaken * 6 / currentBowler.balls

        # Print scoreboard after the second inning
        self.print_scoreboard(team[1], teamList[1], total[1],teamList[0])
        self.determine_winner(team[0], total[0], team[1], total[1])

m = Main()
m.play()
