# Voting analysis project

# List of options and welcoming user
options = ["Analyse the percentage of voters who voted and didn't vote", "List by constituency", "Analyse percentage by gender","List the MPS","List the parties"]

print("Welcome to the election analysis software")
print("Choose your option - use the number")
print("Option Number\tOption")
optionNumber = 1
for option in options:
    print(optionNumber, "\t", option)
    optionNumber += 1

import csv

def load_data(filename):
    aylist = []
    with open(filename) as edited:
        edited_data = csv.reader(edited, delimiter=',')
        next(numbers_data) #skip the header