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

class Constituency:
    def __init__(self,t):
        self.details = t
    def __str__(self):
        return self.details['CName']+" "+self.details['Party']
    def GetCountry(self):
        return self.details['Country']
    def GetType(self):
        return self.details['CType']
        

constituencies = []
#partyToCount = input("Party code to count, Lab, Con, LD, RUK, IND")
parties = ["Lab","Con","LD","RUK","Green","IND","SNP","PC","DUP","SF","SDLP","UUP","APNI"]
mpCount = []
for p in parties:
    mpCount.append(0)
#mpCount = [0,0,0,0,0,0]
#getting constituency data from csv file aka reading the csv file
with open('Documents/GitHub/VotingAnalysisProject/EditedData.csv', newline='') as csvfile:


    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        counter1 = 1
        for party in parties:
            if row['First party'].lower() == party.lower():
                mpCount[counter1] += 1
            counter1 += 1    
        constituency = {'CName':row['Constituency name'],'RName':row['Region name'],'Country':row['Country name'],'CType':row['Constituency type'],'Party':row['First party']}
        con = Constituency(constituency)
        constituencies.append(con)
    counter1 = 0
    for party in parties:
        print(party, " got ",mpCount[counter1], " mps")
        counter1 += 1
for con in constituencies:
    print(con)
plt.bar(parties,mpCount)
plt.show()
next =input()
plt.pie(mpCount)
plt.show()