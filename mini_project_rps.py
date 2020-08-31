import random
def name_To_Number(name) :
    if (name == "rock"):
        return int (0)
    elif (name == "spock"):
        return int (1)
    elif (name == "paper"):
        return int (2)
    elif (name == "lizard"):
        return int (3)
    elif (name == "scissors"):
        return int (4)
    else:
        return "unknown"

def number_To_Name(num) :
    if (num == 0):
        return("Rock")
    elif (num == 1):
        return("spock")
    elif (num == 2):
        return("paper")
    elif (num == 3):
        return("lizard")
    elif (num == 4):
        return("scissors")
    else:
        return "unknown"

def rpssl(player_Choice):
    print("\n")
    
    comp_Choice = random.randrange(4)
    y = number_To_Name(comp_Choice)
    print("Player Choses " , player_Choice)
    z = name_To_Number(player_Choice)
    
    print("Computer choses ",y)
    
    
    x =  comp_Choice -  z
    if (x == 1 or x == 2):
        print("Computer Wins")
    elif (x < 0 or x >= 3):
        print("PLayer Wins")
    else:
        print("Its a Draw")
        

rpssl("paper")