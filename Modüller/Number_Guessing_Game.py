import random
import time

print("""****************************************

Number Guessing Game

Predict between 1 and 40......

****************************************""")

random_number = random.randint(1, 40)
right_to_guess = 5

while True:
    guess = int(input("Your guess = "))
    if 1 <= guess <= 40:
        if guess < random_number:
            print("Prediction Query...")
            time.sleep(1)
            right_to_guess -= 1
            if right_to_guess != 0:
                print("Predict Higher!")

        elif guess > random_number:
            print("Prediction Query...")
            time.sleep(1)
            right_to_guess -= 1
            if right_to_guess != 0:
                print("Predict Less!")

        else:
            print("Congratulations, Number = ", random_number)
            break

        if right_to_guess == 0:
            print("Your Right To Forecast Done....")
            break
    else:
        print("Predict between 1 and 40!!!")
