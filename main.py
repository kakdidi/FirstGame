print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Play!!")
        left_or_right = input("First Choice left or right... (left/right? ")
        if left_or_right == "left":
            ans = input("Nice you follow the right path. Do you swim accross or go around. (accross/around)? ")
            if ans == "accross":
                print("testing")
            
            elif ans == "around":
                print("testing2")
            else: 
                print("You Lost...")
        else:
            print("You Fell down and lost...") 
    else:
        print("Bye...")
else:
    print("You aren't enough to play")