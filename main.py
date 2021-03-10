print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ")
    if wants_to_play == "yes":
        print("Let's Play!!")
else:
    print("You aren't enough to play")