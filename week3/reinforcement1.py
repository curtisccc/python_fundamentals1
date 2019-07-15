schedule = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# 1. save the direction of train 111 into a variable
train111_direction = schedule[7]['direction']
print(train11_direction)

# 2. save the frequency of train 80B into a variable
train80B_freq = schedule[5]['frequency_in_minutes']
print(train80B_freq)

# 3. save the direction of train 610 into a variable
train610_direction = schedule[2]['direction']
print(train610_direction)

# 4. create an empty list. Iterate through each train and add the name of the train into the list if it travels north.
travel_north = []
for train in train_list:
    if train["direction"] == north
        print(train["train"])

# 5. Do the same thing for trains that travel east.
travel_east = []
for trains in train_list:
    if train["direction"] == east
    print(train["train"])

# 6. DRY up the code from 5 & 4
def direction(train_dir):
    for train in train_list:
        if train['direction'] == train_dir:
            print(train['train'])
direction('north')
direction('east')
print(train_list[1])

# 8. now we want ot make a new dictionary where the train frequencies are the keys and the values are a list of train names
trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        train_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)



