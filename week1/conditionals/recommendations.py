difficulty=input("Hard or Easy? ")
players=input("Multiplayer or Single player? ")
if difficulty == "Hard":
    if players == "Multiplayer":
        print("Call of Duty")
    else:
        print("Resident Evil")
else:
    if players == "Multiplayer":
        print("Clash of clans")
    else:
        print("Granny")

