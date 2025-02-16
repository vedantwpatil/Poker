from hand import Hand
from deck import Deck
from card import Card


# The general methodology all the players will use while playing, this is more for human players but provides the blueprint for the ai strategies
class Player:
    def __init__(self, cards: Hand, initial_chips: int) -> None:
        self.__hand = cards
        self.__chips = initial_chips

    def __str__(self) -> str:
        return f"Player Hand: {self.get_hand()}, Player Chips: {self.get_chips()}"

    def play_turn(self):
        pass

    def check_pot(self):
        pass

    def bet_pot(self):
        pass

    def call_pot(self):
        pass

    def raise_pot(self):
        pass

    def fold_pot(self):
        pass

    def set_hand(self, newHand):
        self.__hand = newHand

    def get_hand(self):
        return self.__hand

    def add_chips(self, newChips):
        self.__chips += newChips

    def get_chips(self):
        return self.__chips
