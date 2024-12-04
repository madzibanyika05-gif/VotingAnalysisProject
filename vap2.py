import csv
# The csv module is imported to read data from the CSV file.
class Constituency:
    def __init__(self, t):
        self.details = t 
# Class to rperresnt one constituency with its details

    def __str__(self):
        return self.details['CName'] + " - " + self.details['Party'] + " (" + self.details['RName'] + ")"

    def GetCountry(self):
        return self.details['Country']

    def GetType(self):
        return self.details['CType']

    def GetValidVotes(self):
        return int(self.details.get('Valid votes', 0))

    def GetMemberGender(self):
        return self.details.get('Member gender', 'Unknown')
# Methods allow us to access specific details of a constituency

def analyze_valid_voters_per_party(constituencies):
    party_valid_votes = {}
    
    for con in constituencies:
        party = con.details['Party']
        valid_votes = con.GetValidVotes()
        
        if party not in party_valid_votes:
            party_valid_votes[party] = 0
        party_valid_votes[party] += valid_votes

    #Print results
    for party, votes in party_valid_votes.items():
        print(f"{party}: {votes} valid votes") # Function counts number of valid votes per party
def calculate_gender_percentages(constituencies):
    total_male = 0
    total_female = 0
    
# Count number of males and females
    for con in constituencies:
        gender = con.GetMemberGender() # Retrieves the gender from the Member Gender column
        if gender == "Male":
            total_male += 1
        elif gender == "Female":
            total_female += 1

    total_members = total_male + total_female # Total number of counted genders
    if total_members > 0:
        male_percentage = (total_male / total_members) * 100
        female_percentage = (total_female / total_members) * 100
        print(f"Male Members: {total_male} ({male_percentage:.2f}%)")
        print(f"Female Members: {total_female} ({female_percentage:.2f}%)")
    else:
        print("No member data available to calculate percentages.")

options = [
    "Analyse the number of valid voters per party",
    "List by constituency",
    "Calculate % of Male and Female Members",
    "List the MPS",
    "List the parties",
    "List constituencies by region",
    "List constituency details"
]
#List defines all options a user can choose from the program

constituencies = []
parties = ["Lab", "Con", "LD", "RUK", "Green", "IND", "SNP", "PC", "DUP", "SF", "SDLP", "UUP", "APNI"]
mpCount = [0] * len(parties)

# Update the file path as necessary
with open('/Users/mathewmadzibanyika/Documents/GitHub/VotingAnalysisProject/EditedData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        constituency = {
            'CName': row['Constituency name'],
            'RName': row['Region name'],
            'Country': row['Country name'],
            'CType': row['Constituency type'],
            'Party': row['First party'],
            'Valid votes': row.get('Valid votes', 0),
            'Majority': row.get('Majority', 0),
            'Member gender': row.get('Member gender', 'Unknown')  
        }
        con = Constituency(constituency)
        constituencies.append(con)
# CSV is read and extracts into a rows 

while True:
    # Main Menu Title
    print("\n--- Main Menu ---")
    print("Choose your option - use the number")
    print("Option Number\tOption")
# Displays menue and asks the user to choose
    
    for index, option in enumerate(options, 1):
        print(index, "\t", option) # Loops thorugh option list starting from 1 and displays them with their corresponding number
    choice = input("Enter the option number: ")
# Choice is taken from the user via input
    if choice == '1':
        analyze_valid_voters_per_party(constituencies)
        last_action = '1'
    elif choice == '2':
        for con in constituencies:
            print(con)
        last_action = '2'
    elif choice == '3':
        calculate_gender_percentages(constituencies)
        last_action = '3'
    elif choice == '4':
        counter1 = 0
        for party in parties:
            print(party, " got ", mpCount[counter1], " mps")
            counter1 += 1
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
# Options 1-6 checking if user entered option then printing details and remebering last action
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
# Option 7 checks for input and asks for constituency name and prints details

# Prompt to retry or Return to main menu
    if last_action is not None:
        retry_or_menu = input("Do you want to try again (Y) or return to the main menu (M)? ").strip().upper()
        if retry_or_menu == 'M':
            continue   # Loop restarts for the main menu
        elif retry_or_menu == 'Y':
            
            if last_action == '1':
                analyze_valid_voters_per_party(constituencies) # Based on the last valid action, repeat that action
            elif last_action == '2':
                for con in constituencies:
                    print(con)
            elif last_action == '3':
                calculate_gender_percentages(constituencies)  
            elif last_action == '4':
                counter1 = 0
                for party in parties:
                    print(party, " got ", mpCount[counter1], " mps")
                    counter1 += 1
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
                    print("Constituency not found.") # Option 1-7 repeats the last valid action if invalid input is given
        else:
            print("Invalid input. Returning to main menu.")
# Loop restarts for the main menu
