import random


def main():
    # boolean - True or false values

    guessed_number = False

    while not guessed_number:
        number_to_guess = random.randint(1, 21)
        user_guess = int(input("Enter a number between 1 and 20: "))
        if user_guess == number_to_guess:
            print(f"You're correct! The number was {number_to_guess} ")
            guessed_number = True


if __name__ == '__main__':
    main()
