import csv
# The csv module is imported to read data from the CSV file.
class Constituency:
    def __init__(self, t):
        self.details = t 
# Class to represent one constituency with its details

    def __str__(self):
        return self.details['CName'] + " - " + self.details['Party'] + " (" + self.details['RName'] + ")"

    def GetCountry(self):
        return self.details['Country']

    def GetType(self):
        return self.details['CType']

    def GetValidVotes(self):
        return int(self.details.get('Valid votes', 0))

    def GetMemberGender(self):
        return self.details.get('Member gender', 'Unknown') # This first part from Peters code
# Methods allow us to access specific details of a constituency

def analyze_valid_voters_per_party(constituencies):
    party_valid_votes = {}
    
    for con in constituencies:
        party = con.details['Party']
        valid_votes = con.GetValidVotes()
        
        if party not in party_valid_votes:
            party_valid_votes[party] = 0
        party_valid_votes[party] += valid_votes

    # Print results
    for party, votes in party_valid_votes.items():
        print(f"{party}: {votes} valid votes")  # Function counts number of valid votes per party

def calculate_gender_percentages(constituencies):
    total_male = 0
    total_female = 0
    
    # Count number of males and females
    for con in constituencies:
        gender = con.GetMemberGender()  # Retrieves the gender from the Member Gender column
        if gender == "Male":
            total_male += 1
        elif gender == "Female":
            total_female += 1

    total_members = total_male + total_female  # Total number of counted genders
    if total_members > 0:
        male_percentage = (total_male / total_members) * 100
        female_percentage = (total_female / total_members) * 100
        print(f"Male Members: {total_male} ({male_percentage:.2f}%)")
        print(f"Female Members: {total_female} ({female_percentage:.2f}%)")
    else:
        print("No member data available to calculate percentages.") # Got help from a year 3 with % calculation function and calling it later on

def list_mps_per_party(constituencies):
    """Function to count and display the number of MPs for each party."""
    mp_count_dict = {party: 0 for party in parties}

    for con in constituencies:
        party = con.details['Party']
        if party in mp_count_dict:
            mp_count_dict[party] += 1  # Function to add number of MPs for each party

    # Print the number of MPs for each party
    print("\nNumber of MPs in each party:")
    for party, count in mp_count_dict.items():
        print(f"{party}: {count} MPs") # Got help from Mrs Zakai and a year 3 student with this function and mpCount list as well as calling it later on

options = [
    "Analyse the number of valid voters per party",
    "List by constituency",
    "Calculate % of Male and Female Members",
    "List the MPs",
    "List the parties",
    "List constituencies by region",
    "List constituency details",
    "Exit"  # Exit option to terminate the program
]
# List defines all options a user can choose from the program

constituencies = []
parties = ["Lab", "Con", "LD", "RUK", "Green", "IND", "SNP", "PC", "DUP", "SF", "SDLP", "UUP", "APNI"]
mpCount = [0] * len(parties) # This is from petters code, but added functions inbetween and option list

# Update the file path as necessary
with open('/Users/mathewmadzibanyika/Documents/GitHub/VotingAnalysisProject/EditedData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: # help with opening csv also from peters code
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

print("Welcome to my voting analysis software, you can choose from a number of options to analyse and filter the 2024 UK election results. To terminate software, return to the main menu and choose option 8. Have fun!")
input("Please press the enter key on your device to continue...")
# Welcome message and user input to continue

while True:
    # Main Menu Title
    print("\n--- Main Menu ---")
    print("Choose your option - use the number")
    print("Option Number\tOption")
    
    for index, option in enumerate(options, 1):
        print(index, "\t", option)  # Loops through option list starting from 1 and displays them with their corresponding number
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
        list_mps_per_party(constituencies)
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
    elif choice == '7': # Option 1-7 calling functions based on user input
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
    elif choice == '8':  # Option to exit program
        print("Thank you for using my software, goodbye!!!")
        break
    else:
        print("Invalid option. Please enter a valid option and try again.")
        last_action = None  # No valid action taken

    # Prompt to retry or Return to main menu
    if last_action is not None:
        retry_or_menu = input("Do you want to try again (Y) or return to the main menu (M)? ").strip().upper()
        if retry_or_menu == 'M':
            continue  # Loop restarts for the main menu
        elif retry_or_menu == 'Y':
            if last_action == '1':
                analyze_valid_voters_per_party(constituencies)  # Based on the last valid action, repeat that action
            elif last_action == '2':
                for con in constituencies:
                    print(con)
            elif last_action == '3':
                calculate_gender_percentages(constituencies)  
            elif last_action == '4':
                list_mps_per_party(constituencies)
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
                    print("Constituency not found.")  # Option 1-7 repeats the last valid action if invalid input is given
        else:
            print("Invalid input. Returning to main menu.")
csvfile.close() # Gets rid of end error message
# Loop restarts for the main menu

# refrences
# https://realpython.com/python-csv/
# https://realpython.com/videos/reading-csvs-pythons-csv-module/
# https://now.ntu.ac.uk/d2l/le/content/1046185/viewContent/13287022/View
# https://realpython.com/python3-object-oriented-programming/
# https://now.ntu.ac.uk/d2l/le/content/1046185/viewContent/13314606/View
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# https://www.w3schools.com/python/python_functions.asp
# https://www.youtube.com/watch?v=9Os0o3wzS_I
# https://realpython.com/primer-on-python-decorators/
# https://olympus.ntu.ac.uk/CMP3BLANCP/OneLastTime/blob/4b9dbbe96e16550a2a65cce99e3c5b0de0058809/MyPythonProject.py
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
# https://realpython.com/python-debugging-pdb/
# https://www.youtube.com/watch?v=6XrL5jXmTwM&t=132s
