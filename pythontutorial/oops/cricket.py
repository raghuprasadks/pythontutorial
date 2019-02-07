class player():
    def __init__(self,name,team,matches,run,wicket):
        self.name = name
        self.team = team
        self.matches = matches
        self.run = run
        self.wicket = wicket
    def runs(self,r):
        self.r = r
        self.run = self.run + self.r
        return self.run
    def wickets(self,w):
        self.w = w
        self.wicket = self.wicket + self.w
        return self.wicket
    
name = input("Enter the name of the player\n")
team = input("Enter the team that you play for\n")
matches = int(input("Enter the total number of matches that you've played\n"))
run = int(input("Enter the number of runs you've earned\n"))
wickets = int(input("Enter the number of wickets you've taken\n"))
c1 = player(name,team,matches,run,wickets)
r = int(input("Enter the runs you've scored in the current match\n"))
w = int(input("Enter the wickets taken in the current match\n"))
wi = c1.wickets(w)
ru = c1.runs(r)
print("Total runs scored = ",ru)
print("Total wickets taken over your entire career is",wi)

        
