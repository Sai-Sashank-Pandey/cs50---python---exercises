difficulty=input("Hard or Easy? ")
players=input("Multiplayer or Single player? ")
if difficulty == "Hard":
    if players == "Multiplayer":
        recommend("Call of Duty")
    else:
        recommend("Resident Evil")
else:
    if players == "Multiplayer":
        recommend("Clash of clans")
    else:
        recommend("Granny")

def recommend(game):
    print("We recommend you",game)
