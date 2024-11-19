
def start_game():
    print( "Hello explorer, you are in a fairy tale forest and adventure awaits you. Choose your destiny!! \n Choose your path!!")
    playerOneInput = input("Choose Your Path (write it as is!): \n Path 1: GO NORTH \n Path 2: CLIMB OAK TREE . . .")
    if playerOneInput == "GO NORTH":
        print("you choose the wrong path bumb")
        start_game()
    elif playerOneInput == "CLIMB OAK TREE":
        print("You found a map and the geeni Namira told you to go west")
        west()
    else:
        print("please choose between NORTH or CLIMB OAK TREE")
        start_game()


def west(): 
    print("Folllow west you are now faced with two options:")
    playerOneInput = input("\n PURPLE \n PINK \n both colors are fun but one is tricky so choose wisly ...")
    if playerOneInput == "PURPLE":
        print("You have found tresure and a ponyy")

    elif playerOneInput == "PINK":
        print("you have just met the spider that killed you!!! wrong choice boddy")
        while (playerOneInput == "PINK"):
            west()
        
    else:
        print("please choose between PINK or PURPLE")
        west()

def medicine(): 
    print("You were bitten by spider but you have 24 hours to find a cure, HURRY!!")
    print("Front of you lies a river with a boat, go with flow!!")
    print("The story of your life: You face going through two ")

print(start_game())


         





