import random

# Card Constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = (
    'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
    'King')
NUMBER_OF_CARDS = 8


# Pass in a deck and return a random card from the deck
def get_card(deck_list_in):
    thisCard = deck_list_in.pop()  # pops a card off the top of the deck and
    # returns it
    return thisCard


# Pass in the deck and the function will return a shuffled copy of it

def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


# MAIN CODE

def main():
    print('Welcome to Higher or Lower.')
    print(
        'You have to choose whether the next card to be shown will be higher '
        'or lower than the current card.')
    print(
        'Getting it right adds 20 points; get it wrong and you lose 15 '
        'points.')
    print('You have 50 points to start.')
    print()

    starting_deck_list = []

    for suit in SUIT_TUPLE:
        for this_value, rank in enumerate(RANK_TUPLE):
            cardDict = {'rank': rank, 'suit': suit, 'value': this_value + 1}
            starting_deck_list.append(cardDict)

    score = 50

    while True:
        print()
        game_deck_list = shuffle(starting_deck_list)
        current_card_dict = get_card(game_deck_list)
        current_card_rank = current_card_dict['rank']
        current_card_value = current_card_dict['value']
        current_card_suit = current_card_dict['suit']
        print(f'Starting card is: {current_card_rank} of {current_card_suit}')
        print()

        for cardNumber in range(0, NUMBER_OF_CARDS):
            answer = input(f"Will the next card be higher or lower than the "
                           f"{current_card_rank} of {current_card_suit}? "
                           f"(Enter h or l) : ")
            answer = answer.casefold()
            next_card_dict = get_card(game_deck_list)
            next_card_rank = next_card_dict['rank']
            next_card_value = next_card_dict['value']
            next_card_suit = next_card_dict['suit']
            print(f" The next card is {next_card_rank} of {next_card_suit}")

            # what happens as a result of each key press?
            if answer == 'h':
                if next_card_value > current_card_value:
                    print("You got it right! It was higher!")
                    score += 20
                else:
                    print("Sorry, it was actually lower than that!")
                    score -= 15
            elif answer == 'l':
                if next_card_value < current_card_value:
                    print("You got it right! It was lower!")
                    score += 20
                else:
                    print("Sorry, it was actually higher than that!")
                    score -= 15
            print(f'Your score is {score}')
            print()
            current_card_rank = next_card_rank
            current_card_value = next_card_value
            current_card_suit = next_card_suit
        goAgain = input("Would you like to play again? Press ENTER for yes, "
                        "and q to quit.")
        goAgain = goAgain.casefold()
        if goAgain == 'q':
            break
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
