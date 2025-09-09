import random
print("You must qezz a number between 0 and 100 \n you have 7 changes to qess.\nlets begin")
number = random.randrange(0,100)
chances = 7
guess_taken = 0
chances_left = 7
#is qess_taken = changes then your out
#if quess is > number then say too big, of quess < number then say too small
while guess_taken < chances:
    guess_taken += 1
    chances_left -= 1
    my_quess = int(input("whats your quess: "))
    if my_quess == number:
            print(f"You won,its {number} in {guess_taken} Attempt")
            #need to break the code if you quess right
            break
    elif  my_quess < number:
            print(f"your guess it too small,your Attempt is {guess_taken},you have {chances_left} Attempt left")
    elif my_quess > number:
        print(f"your guess is too big,your Attempt is {guess_taken},you have {chances_left} Attempt left")
if chances == guess_taken and my_quess != number:
    print(f"you lose, the number was {number}")