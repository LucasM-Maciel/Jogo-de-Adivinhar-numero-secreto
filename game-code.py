import random
score = 0
compliment = " "
remaining_attempts = 5
used_attempts = 1

def check_plural_used(attempts):
    if attempts <= 1:
        return "attempt"
    else:
        return "attempts"
    
def check_plural_remaining(attempts):
    if attempts-1 <= 1:
        return "attempt"
    else:
        return "attempts"

def ask_integer_number(difficulty):
    while True:
        try:
            number = int(input(f"Try to guess a number from 1 to {10*difficulty}: "))
            return number
        except ValueError:
            print("That's not a valid number")
            continue
    
def verify_difficulty_integer():
    while True:
        try:
            difficulty = int(input("Welcome! This is the mystery number game. Choose a difficulty from 1 to 3\nEnter 4 to exit and check your score: "))
            return difficulty
        except ValueError:
            print("That's not a valid number")
            continue

while True:
    difficulty = verify_difficulty_integer()
    if difficulty == 4:
        break
    elif difficulty == 1:
        secret_number = random.randint(1, 10*difficulty)
        remaining_attempts = 5
        used_attempts = 1
        while remaining_attempts > 0:
            word_remaining = check_plural_remaining(remaining_attempts)
            word_used = check_plural_used(used_attempts)
            challenge_level1 = ask_integer_number(difficulty)
            if challenge_level1 > 10 or challenge_level1 < 1:
                print("Invalid number, try a number from 1 to 10")
                continue
            elif challenge_level1 > secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level1} is higher than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            elif challenge_level1 < secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level1} is lower than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            else:
                print(f"Congratulations! The number {secret_number} is the secret number, and you guessed it in {used_attempts} {word_used}!")
                score += 10
                break
        if remaining_attempts == 0:
            print("\nYou lost, try again")  
    
    elif difficulty == 2:
        secret_number = random.randint(1, 10*difficulty)
        remaining_attempts = 5
        used_attempts = 1
        while remaining_attempts > 0:
            word_remaining = check_plural_remaining(remaining_attempts)
            word_used = check_plural_used(used_attempts)
            challenge_level2 = ask_integer_number(difficulty)
            if challenge_level2 > 20 or challenge_level2 < 1:
                print("Invalid number, try a number from 1 to 20")
                continue
            elif challenge_level2 > secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level2} is higher than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            elif challenge_level2 < secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level2} is lower than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            else:
                print(f"Congratulations! The number {secret_number} is the secret number, and you guessed it in {used_attempts} {word_used}!")
                score += 20
                break
        if remaining_attempts == 0:
            print("\nYou lost, try again")  
    elif difficulty == 3:
        secret_number = random.randint(1, 10*difficulty)
        remaining_attempts = 5
        used_attempts = 1
        while remaining_attempts > 0:
            word_remaining = check_plural_remaining(remaining_attempts)
            word_used = check_plural_used(used_attempts)
            challenge_level3 = ask_integer_number(difficulty)
            if challenge_level3 > 30 or challenge_level3 < 1:
                print("Invalid number, try a number from 1 to 30")
                continue
            elif challenge_level3 > secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level3} is higher than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            elif challenge_level3 < secret_number:
                remaining_attempts -= 1
                print(f"The number {challenge_level3} is lower than the secret number!\nYou have {remaining_attempts} {word_remaining} left.")
                used_attempts += 1
            else:
                print(f"Congratulations! The number {secret_number} is the secret number, and you guessed it in {used_attempts} {word_used}!")
                score += 30
                break
        if remaining_attempts == 0:
            print("\nYou lost, try again")          
    else: 
        print("Invalid number, enter a number from 1 to 3 for the desired difficulty\nEnter 4 to stop and check your score")
        
if score <= 10:
    compliment = "You are a terrible guesser"
elif score > 10 and score <= 50:
    compliment = "You're on your way to becoming an excellent guesser!"
else:
    compliment = "Supreme Guesser!"
    
print(f"\nCongratulations! You scored {score} points!\n{compliment}")
