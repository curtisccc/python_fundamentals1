grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

def list():

    for item in grocery_list:
        print("*" + ' ' + item)
    
    if item == "bananas":
        print("You don't need to pick up bananas today")
    else:
        print("You need to pick up bananas")

grocery_list.append("rice")
list()

print(len(grocery_list))

print(grocery_list[1])

grocery_list.sort()
list()

grocery_list.remove("salmon")
list()


