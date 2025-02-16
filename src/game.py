from card import Card
from deck import Deck
from hand import Hand
from player import Player
import player


# from ai import ai
class Game:
    def __init__(self):
        deck_list = []
        deck_class = Deck(deck_list)

        deck_class.addCards()
        deck_list = deck_class.getDeck()

        deck_list = deck_class.shuffleDeck()

        # TODO: Imeplement error handling
        player_amt = int(input("Enter the amount of players "))
        starting_chips = int(input("Enter the initial chips "))

        self.dealCards(
            amt_of_players=player_amt, deck=deck_list, initial_chips=starting_chips
        )

    def dealCards(self, amt_of_players, deck: list[Card], initial_chips):
        players = []
        for i in range(amt_of_players):
            player_hand = []

            player_hand.append(deck.pop())
            player_hand.append(deck.pop())

            hand = Hand(player_hand)

            players.append(Player(cards=hand, initial_chips=initial_chips))
        print(players)


def main():
    game = Game()


main()
