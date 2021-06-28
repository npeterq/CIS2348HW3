"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"11.27 CIS 2348 LAB*: Program: Soccer team roster (Dictionaries)"

players = dict()
numberOfPlayers = 5
for i in range(numberOfPlayers):
    jerseyNumber, rating = -1, -1
    while not 0 < jerseyNumber <= 99:
        jerseyNumber = int(input('Enter Jersey number (0-99) : '))
    while not 1 <= rating <= 9:
        rating = int(input('Enter player rating (1-9) : '))
    players[jerseyNumber] = rating
    print()

for key in sorted(players.keys()):
    print(key,' => ', players[key])
