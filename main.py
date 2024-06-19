class CricketScoreboard:
    def __init__(self, team1, team2, overs):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.team1_score = 0
        self.team2_score = 0
        self.team1_wickets = 0
        self.team2_wickets = 0
        self.current_over = 0

    def update_score(self, runs):
        if self.current_over % 2 == 0:
            self.team1_score += runs
        else:
            self.team2_score += runs

    def update_wicket(self):
        if self.current_over % 2 == 0:
            self.team1_wickets += 1
        else:
            self.team2_wickets += 1

    def display_scoreboard(self):
        print("\nCurrent Scoreboard:")
        print(f"{self.team1}: {self.team1_score}/{self.team1_wickets} in {self.current_over} overs")
        print(f"{self.team2}: {self.team2_score}/{self.team2_wickets} in {self.current_over} overs")

    def next_over(self):
        self.current_over += 1
        if self.current_over > self.overs * 2:
            print("Match ended.")
            self.display_scoreboard()
            return False
        else:
            print(f"\nStart of Over {self.current_over//2 + 1}")
            return True

# Example usage
scoreboard = CricketScoreboard("Team A", "Team B", 10)  # Creating a scoreboard for a 10-over match

while scoreboard.next_over():
    runs = int(input("Enter runs scored in this over: "))
    scoreboard.update_score(runs)
    if runs == -1:  # Assuming -1 indicates a wicket
        scoreboard.update_wicket()
    scoreboard.display_scoreboard()
