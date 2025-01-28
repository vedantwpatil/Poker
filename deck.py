import random
from card import Card


class Deck:
    def __init__(self, deck: list[Card]) -> None:
        self.__deck = deck

    def getDeck(self):
        return self.__deck

    def setDeck(self, deck: list[Card]):
        self.__deck = deck

    def setupDeck(self):
        deck = self.getDeck()
        deck = self.shuffleDeck(deck)

        self.setDeck(deck)

    def shuffleDeck(self, deck: list[Card]):
        for i in range(len(deck), 1):
            j = int(random.random() * i)

            temp = deck[i]
            deck[i] = deck[j]
            deck[j] = temp

        return deck

    def splitDeck(self):
        pass

    def addCards(self):
        deck = self.getDeck()

        for i in range(3):
            for j in range(9):
                suit = ""
                num = j + 1

                match i:
                    case 0:
                        suit = "Spades"
                    case 1:
                        suit = "Hearts"
                    case 2:
                        suit = "Diamonds"
                    case 3:
                        suit = "Clubs"

                newCard = Card(suit=suit, value=num)
                deck.append(newCard)
