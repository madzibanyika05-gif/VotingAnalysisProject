import csv

class Constituency:
    def __init__(self, t):
        self.details = t

    def __str__(self):
        return self.details['CName'] + " " + self.details['Party']

    def GetCountry(self):
        return self.details['Country']

    def GetType(self):
        return self.details['CType']

    def GetVoterTurnout(self):
        total_voters = int(self.details['Total Voters'])
        actual_voters = int(self.details['Actual Voters'])
        if total_voters > 0:
            return (actual_voters / total_voters) * 100
        return 0

    def GetNonVoterPercentage(self):
        return 100 - self.GetVoterTurnout()

def analyze_voter_turnout(constituencies):
    total_turnout = 0
    total_non_voters = 0
    for con in constituencies:
        voter_turnout = con.GetVoterTurnout()
        non_voter_percentage = con.GetNonVoterPercentage()
        print(con)
        print(f"Voter Turnout: {voter_turnout:.2f}%")
        print(f"Non-Voter Percentage: {non_voter_percentage:.2f}%")
        
        total_turnout += voter_turnout
        total_non_voters += non_voter_percentage

    # Print overall averages
    num_constituencies = len(constituencies)
    if num_constituencies > 0:
        print(f"Average Voter Turnout: {total_turnout / num_constituencies:.2f}%")
        print(f"Average Non-Voter Percentage: {total_non_voters / num_constituencies:.2f}%")

options = [
    "Analyse the percentage of voters who voted and didn't vote",
    "List by constituency",
    "Analyse percentage by gender",
    "List the MPS",
    "List the parties"
]

print("Welcome to the election analysis software")
print("Choose your option - use the number")
print("Option Number\tOption")
optionNumber = 1
for option in options:
    print(optionNumber, "\t", option)
    optionNumber += 1

constituencies = []
parties = ["Lab", "Con", "LD", "RUK", "Green", "IND", "SNP", "PC", "DUP", "SF", "SDLP", "UUP", "APNI"]
mpCount = [0] * len(parties)
# making sure program recalls rows properlly
with open('Documents/GitHub/VotingAnalysisProject/edited.data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        constituency = {
            'CName': row['Constituency name'],
            'RName': row['Region name'],
            'Country': row['Country name'],
            'CType': row['Constituency type'],
            'Party': row['First party'],
        }
        con = Constituency(constituency)
        constituencies.append(con)
# Making sure program can list number the appropriate filter option according to number chosen
while True:
    choice = input("Enter the option number: ")
    if choice == '1':
        analyze_voter_turnout(constituencies)
    elif choice == '2':
        for con in constituencies:
            print(con)
    elif choice == '3':
        # Implement gender analysis here if needed
        pass
    elif choice == '4':
        counter1 = 0
        for party in parties:
            print(party, " got ", mpCount[counter1], " mps")
            counter1 += 1
    elif choice == '5':
        # Option to list the parties or any other relevant action
        print("List of Parties:", parties)
    else:
        print("Invalid option. Please try again.")
