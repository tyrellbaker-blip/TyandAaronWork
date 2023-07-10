import random



def odd_or_even():
    number = int(input("Type in a number here: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")



odd_or_even()















def main():

    Aarons_favorite_games = ["bonk.io", "Cities Skylines", "Foxhole",
                             "Rimworld", "Xcom 2"]

    for game in range(len(Aarons_favorite_games)):
        print(Aarons_favorite_games[game])


if __name__ == '__main__':
    main()
