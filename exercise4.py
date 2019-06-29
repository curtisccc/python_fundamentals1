print("Enter a number")
number = input()
if int(number) > 100:
    print("That's a big number!")
else:
    print("Why not dream a little bigger?")

print("enter your age?")
age = input()
age_apart = 24 - int(age)
if int(age) > 105:
    print("I'm not sure I believe you")
else:
    print("We are {} years apart.".format(age_apart))

master_name = "curtis"
print("Enter your name!")
user_name = input().lower()
if master_name == user_name:
    print("We have the same name!")
else:
    print("What a great name!")

secret_number = 7
print("Enter a number:")
user_number = input()
num =int(user_number)
if secret_number == num:
    print("You win!")
elif secret_number == num - 1 or secret_number == num + 1:
    print("So close!")
else:
    print("Try again!")