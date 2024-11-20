import csv
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

class Constituency:
    def __init__(self, t):
        self.details = t

    def __str__(self):
        return f"{self.details['CName']} - {self.details['Party']} ({self.details['RName']})"

    def GetCountry(self):
        return self.details['Country']

    def GetType(self):
        return self.details['CType']

    def GetVoterTurnout(self):
        valid_votes = int(self.details.get('Valid votes', 0))
        majority = int(self.details.get('Majority', 0))
        if valid_votes > 0:
            return (majority / valid_votes) * 100
        return 0

    def GetNonVoterPercentage(self):
        return 100 - self.GetVoterTurnout()


def calculate_valid_votes_per_party(constituencies):
    party_votes = {}

    # Calculate the total valid votes per party
    for con in constituencies:
        party = con.details['Party']
        valid_votes = int(con.details.get('Valid votes', 0))

        if party in party_votes:
            party_votes[party] += valid_votes
        else:
            party_votes[party] = valid_votes

    # Display the results
    print("Valid Votes per Party:")
    for party, votes in party_votes.items():
        print(f"{party}: {votes}")

    # Ask the user if they want to display this data as a bar chart
    show_chart = input("Would you like to display this data as a bar chart? (Y/N): ").strip().upper()
    if show_chart == 'Y':
        # Create a bar chart
        plt.bar(party_votes.keys(), party_votes.values())
        plt.xlabel('Parties')
        plt.ylabel('Valid Votes')
        plt.title('Valid Votes per Party')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to make room for labels
        plt.show()


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
    "Calculate the number of valid votes per party",
    "List by constituency",
    "Analyse percentage by gender",
    "List the MPS",
    "List the parties",
    "List constituencies by region",
    "List constituency details"
]

constituencies = []
parties = ["Lab", "Con", "LD", "RUK", "Green", "IND", "SNP", "PC", "DUP", "SF", "SDLP", "UUP", "APNI"]

with open('Documents/GitHub/VotingAnalysisProject/edited.data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        constituency = {
            'CName': row['Constituency name'],
            'RName': row['Region name'],
            'Country': row['Country name'],
            'CType': row['Constituency type'],
            'Party': row['First party'],
            'Valid votes': row.get('Valid votes', 0),
            'Majority': row.get('Majority', 0)
        }
        con = Constituency(constituency)
        constituencies.append(con)

while True:
    # Main Menu Title
    print("\n--- Main Menu ---")
    print("Choose your option - use the number")
    print("Option Number\tOption")
    
    for index, option in enumerate(options, 1):
        print(index, "\t", option)

    choice = input("Enter the option number: ")

    # Manage the choices
    if choice == '1':
        calculate_valid_votes_per_party(constituencies)  # This should work correctly
        last_action = '1'
    elif choice == '2':
        for con in constituencies:
            print(con)
        last_action = '2'
    elif choice == '3':
        # Implement gender analysis here if needed
        last_action = '3'
    elif choice == '4':
        # You might want to implement a counting of MPS here
        last_action = '4'
    elif choice == '5':
        print("List of Parties:", parties)
        last_action = '5'
    elif choice == '6':
        region = input("Enter the region name: ")
        print(f"Constituencies in {region}:")
        found_region = False
        for con in constituencies:
            if con.details['RName'].lower() == region.lower():
                print(con)
                found_region = True
        if not found_region:
            print("No constituencies found in that region.")
        last_action = '6'
    elif choice == '7':
        constituency_name = input("Enter the constituency name: ")
        found = False
        for con in constituencies:
            if con.details['CName'].lower() == constituency_name.lower():
                found = True
                print(con)
                print(f"Details for {constituency_name}:")
                print(f"Region: {con.GetType()}")
                print(f"Country: {con.GetCountry()}")
                print(f"Party: {con.details['Party']}")
                print(f"Valid Votes: {con.details.get('Valid votes', 'N/A')}")
                print(f"Majority: {con.details.get('Majority', 'N/A')}")
        if not found:
            print("Constituency not found.")
        last_action = '7'
    else:
        print("Invalid option. Please try again.")
        last_action = None  # No valid action taken

    # Prompt to Retry or Return to Main Menu
    if last_action is not None:
        retry_or_menu = input("Do you want to try again (Y) or return to the main menu (M)? ").strip().upper()
        if retry_or_menu == 'M':
            continue  # Loop restarts for the main menu
        elif retry_or_menu == 'Y':
            # Re-executing the last action based on last valid choice
            if last_action == '1':
                calculate_valid_votes_per_party(constituencies)
            elif last_action == '2':
                for con in constituencies:
                    print(con)
            elif last_action == '3':
                # Implement gender analysis here if needed
                pass
            elif last_action == '4':
                # You might want to implement a counting of MP's here
                pass
            elif last_action == '5':
                print("List of Parties:", parties)
            elif last_action == '6':
                region = input("Enter the region name: ")
                print(f"Constituencies in {region}:")
                found_region = False
                for con in constituencies:
                    if con.details['RName'].lower() == region.lower():
                        print(con)
                        found_region = True
                if not found_region:
                    print("No constituencies found in that region.")
            elif last_action == '7':
                constituency_name = input("Enter the constituency name: ")
                found = False
                for con in constituencies:
                    if con.details['CName'].lower() == constituency_name.lower():
                        found = True
                        print(con)
                        print(f"Details for {constituency_name}:")
                        print(f"Region: {con.GetType()}")
                        print(f"Country: {con.GetCountry()}")
                        print(f"Party: {con.details['Party']}")
                        print(f"Valid Votes: {con.details.get('Valid votes', 'N/A')}")
                        print(f"Majority: {con.details.get('Majority', 'N/A')}")
                if not found:
                    print("Constituency not found.")
        else:
            print("Invalid input. Returning to main menu.")
