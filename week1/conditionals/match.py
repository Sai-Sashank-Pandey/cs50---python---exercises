name=input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron" :
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("IDK")
