import random 
print("Number Guessing Game") 
num = random.randint(1,9) 
chance = 0  
print("Guess a number (between 1 and 9):")  
while chance < 15:  
    guess = int(input())   
    if guess == num: 
        print(" YOU WON!!!") 
        break
    elif guess < num: 
        print("Your guess was too low: Guess a higher no", guess)              
    else: 
        print("Your guess was too high: Guess a  lower no", guess) 
    chance += 1 
if not chance < 15: 
    print("YOU LOSE!!! The no is", num) 
