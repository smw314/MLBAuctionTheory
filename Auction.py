import pandas as pd
import numpy as np

# Set up counting variables
Pot = 100
TeamAWins = 0
TeamABids = 0
TeamBWins = 0
TeamBBids = 0
TeamCWins = 0
TeamCBids = 0
TeamAValue = 0
TeamBValue = 0
TeamCValue = 0
BargainCounter = 0
TeamABargain = 0
TeamBBargain = 0
TeamCBargain = 0
TeamASurplus = 0
TeamBSurplus = 0
TeamCSurplus = 0
TeamABudget = 0.75
TeamBBudget = 0.92
TeamCBudget = 0.83

# Set up an iterative loop to run the following simulation 1,000,000 times
for i in range(1000000):
    # Creates a randomly distributed estimate for each team's model valuation of the pot, then creates bids based
    # on those values
    TeamAValue = Pot + np.random.normal() * 15
    TeamBValue = Pot + np.random.normal() * 15
    TeamCValue = Pot + np.random.normal() * 15
    TeamA = TeamAValue * TeamABudget
    TeamB = TeamBValue * TeamBBudget
    TeamC = TeamCValue * TeamCBudget

    # Determine which bid is highest, or which two if they are tied. Then add to the relevant counters.
    if TeamA > max(TeamB, TeamC):
        TeamAWins += 1
        TeamABids += TeamA
        TeamASurplus += TeamAValue - TeamA
        if TeamA <= 100:
            TeamABargain += 1
    elif TeamB > max(TeamA, TeamC):
        TeamBWins += 1
        TeamBBids += TeamB
        TeamBSurplus += TeamBValue - TeamB
        if TeamB <= 100:
            TeamBBargain += 1
    elif TeamC > max(TeamA, TeamB):
        TeamCWins += 1
        TeamCBids += TeamC
        TeamCSurplus += TeamCValue - TeamC
        if TeamC <= 100:
            TeamCBargain += 1
    elif TeamA == TeamB:
        TeamAWins += 0.5
        TeamBWins += 0.5
        TeamABids += TeamA / 2
        TeamBBids += TeamB / 2
        TeamASurplus += (TeamAValue - TeamA) / 2
        TeamBSurplus += (TeamBValue - TeamB) / 2
        if TeamA <= 100:
            TeamABargain += 0.5
            TeamBBargain += 0.5
    elif TeamA == TeamC:
        TeamAWins += 0.5
        TeamCWins += 0.5
        TeamABids += TeamA / 2
        TeamCBids += TeamC / 2
        TeamASurplus += (TeamAValue - TeamA) / 2
        TeamCSurplus += (TeamCValue - TeamC) / 2
        if TeamA <= 100:
            TeamABargain += 0.5
            TeamCBargain += 0.5
    elif TeamB == TeamC:
        TeamBWins += 0.5
        TeamCWins += 0.5
        TeamBBids += TeamB / 2
        TeamCBids += TeamC / 2
        TeamBSurplus += (TeamBValue - TeamB) / 2
        TeamCSurplus += (TeamCValue - TeamC) / 2
        if TeamB <= 100:
            TeamBBargain += 0.5
            TeamCBargain += 0.5
    if max(TeamA, TeamB, TeamC) < 100:
        BargainCounter += 1

# Calculate aggregates
TeamAWinRate = round(TeamAWins / 1000000, 3)
TeamAValue = round(TeamABids / (100 * TeamAWins), 3)
TeamBWinRate = round(TeamBWins / 1000000, 3)
TeamBValue = round(TeamBBids / (100 * TeamBWins), 3)
TeamCWinRate = round(TeamCWins / 1000000, 3)
TeamCValue = round(TeamCBids / (100 * TeamCWins), 3)
FinalBargain = round(BargainCounter / 1000000, 3)
ABargain = round(TeamABargain / TeamAWins, 3)
BBargain = round(TeamBBargain / TeamBWins, 3)
CBargain = round(TeamCBargain / TeamCWins, 3)

TeamASurplusWin = round(TeamASurplus / TeamAWins, 3)
TeamBSurplusWin = round(TeamBSurplus / TeamBWins, 3)
TeamCSurplusWin = round(TeamCSurplus / TeamCWins, 3)

TeamARelativeSurplus = round(TeamASurplus / TeamABudget, 3)
TeamBRelativeSurplus = round(TeamBSurplus / TeamBBudget, 3)
TeamCRelativeSurplus = round(TeamCSurplus / TeamCBudget, 3)

TeamARelativeSurplusWin = round(TeamARelativeSurplus / TeamAWins, 3)
TeamBRelativeSurplusWin = round(TeamBRelativeSurplus / TeamBWins, 3)
TeamCRelativeSurplusWin = round(TeamCRelativeSurplus / TeamCWins, 3)

# Print results
print(f"Team A Win Odds are {TeamAWinRate}")
print(f"Team B Win Odds are {TeamBWinRate}")
print(f"Team C Win Odds are {TeamCWinRate}\n")
print(f"Team A CostPaid is {TeamAValue}")
print(f"Team B CostPaid is {TeamBValue}")
print(f"Team C CostPaid is {TeamCValue}\n")
print(f"Bargain Counter is {FinalBargain}\n")
print(f"Bargain hit rate is, respectively, {ABargain} {BBargain} {CBargain}\n")
print(f"Team A Total Surplus is {round(TeamASurplus, 3)}")
print(f"Team B Total Surplus is {round(TeamBSurplus, 3)}")
print(f"Team C Total Surplus is {round(TeamCSurplus, 3)}\n")
print(f"Team A Surplus per Win is {round(TeamASurplusWin, 3)}")
print(f"Team B Surplus per Win is {round(TeamBSurplusWin, 3)}")
print(f"Team C Surplus per Win is {round(TeamCSurplusWin, 3)}\n")
print(f"Team A Relative Surplus is {TeamARelativeSurplus}")
print(f"Team B Relative Surplus is {TeamBRelativeSurplus}")
print(f"Team C Relative Surplus is {TeamCRelativeSurplus}\n")
print(f"Team A Relative Surplus per Win is {TeamARelativeSurplusWin}")
print(f"Team B Relative Surplus per Win is {TeamBRelativeSurplusWin}")
print(f"Team C Relative Surplus per Win is {TeamCRelativeSurplusWin}\n")
