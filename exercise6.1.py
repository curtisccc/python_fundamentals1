distance = 0
answer = ""
while answer != "go home":
    print("Would you like to walk, run, or go home?")
    answer = input().lower()
    if answer == "walk":
        distance += 1
        print("Distance from home is {}km.".format(distance))
    elif answer == "run":
        distance += 5
        print("Distance from home is {}km.".format(distance))
    elif answer == "go home":
        print("You are now home")
    else:
        print("not found")
