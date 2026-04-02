def main():
    difficulty=input("Hard or Easy? ")
    players=input("Multiplayer or Single player? ")

    if difficulty == "Hard":
         if players == "Multiplayer":
             recommend("Call of Duty")
         elif players == "Single player":
            recommend("Resident Evil")
         else:
             print("Enter valid no of players")
    elif difficulty == "Easy":
        if players == "Multiplayer":
            recommend("Clash of clans")
        elif players == "Single player":
            recommend("Granny")
        else:
            print("Enter valid no of players")
    else:
        print("Enter valid dificulty or players")

def recommend(game):
    print("We recommend you,",game)

main()
