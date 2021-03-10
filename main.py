print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old")
health = 10
print("You are starting from", health, "health.")
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play (Yes/No)? ").lower()
    if wants_to_play == "yes":
        print("Let's Play!!")
        left_or_right = input("First Choice left or right... (left/right? ")
        if left_or_right == "left":
            ans = input("Nice you follow the right path. Do you swim accross or go around. (accross/around)? ")
            if ans == "accross":
                print("You manage to accross the lake but were bit by a fish and lost 5 health.")
                health -= 5
            
            elif ans == "around":
                print("You went around")
            else: 
                print("You Lost...")
        else:
            print("You Fell down and lost...") 
    else:
        print("Bye...")
else:
    print("You aren't enough to play")