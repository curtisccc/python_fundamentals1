distance = 0
while distance >= 0:
    print("Would you like to walk or run?")
    answer = input().lower()
    if answer == "walk":
        distance += 1
        print("Distance from home is {}km".format(distance))
    elif answer == "run":
        distance += 5
        print("Distance from home is {}km".format(distance))