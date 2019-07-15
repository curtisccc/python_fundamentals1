range = range(1, 101)
def bitmaker():
    for number in range:
        if number % 3 == 0 and number % 5 == 0:
            print("Bitmaker")
        elif number & 3 == 0:
            print("Bit")
        elif number % 5 == 0:
            print("Maker")
        else:
            print (number)

bitmaker()