print("Hello Adventurer!")
acceptance = input("Are you ready to go on a tour? Y or N? ")
if acceptance == "Y":
    print("You find yourself in a stone room with four pillars. Each wall has a tapestry with a different colour: blue, green, red and black.\n")
    colour = input("Wich one do you pick to open? ")
    lower_case_colour = colour.lower()
    if lower_case_colour == "blue":
        print("There is a burst of blue electrical energy. Sorry, you are dead.")
    elif lower_case_colour == "green":
        print("A green poisonous gas fills the chamber. Guess you will need more luck next time. You are dead.")
    elif lower_case_colour == "red":
        hallway = input("A sudden flash of red light and then you see a hallway. Do you follow? Y or N? ")
        if hallway == "Y":
            choice = input("OK, great! Another room! You look around and see yourself standing in a luxurious study room. Two things calls your attention: an odd cabinet and a stained glass window. Wich one do you choose to look first? Cabinet or Window? ")
            lower_case_choice = choice.lower()    
            if lower_case_choice == "cabinet":
               open_cabinet = input("Do you open it? Y or N? ")
               if open_cabinet == "Y":
                    print("It's a mimic. You're dead.")
               if open_cabinet == "N":
                    print("Well...it looks like you are trapped?")
            if lower_case_choice == "window":
                push_button = input("This is a beautifully crafted window. You see planes and planets and various things. But a red button at the center catches your eye. Do you push it? Y or N? ")
                if push_button == "Y":
                    arrow_shaped_room = input("All disappers and suddenly you are in a arrow-shaped room. In one side there a HUGE treasure. Like, huge huge. On the other side, there is a green-blue globe. Which one do you choose? Treasure or Globe? ")
                    lower_case_arrow_shaped = arrow_shaped_room.lower()
                    if lower_case_arrow_shaped == "treasure":
                        print("You are a little greed person, don't you? I said a tour, not a treasure hunt. The treasure is guarded by a dragon. You are dead.")
                    if lower_case_arrow_shaped == "globe":
                        globe = input("It is a very shinning globe. Do you touch it? Y or N? ")
                        if globe == "Y":
                             print("You are out! Hope you have had enjoyed your tiny tour on the Folding Halls of Hallas!(Critical Role Inspired)")
                        if globe == "N":
                             print("Well... you are trapped...WITH A DRAGON! You are good as dead, you know? Sorry.")    
    else:
        print("You see a hallway.")
        hallway2 = input("Do you follow? Y or N?")
        if hallway2 =="Y":
            print("You are in the Dinning Room. And you are staying for dinner, because you are trapped.")
        else:
            print("You are sooo trapped.")        
else:
    print("Well, see you next time.")
