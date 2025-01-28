class Card:
    def __init__(self, suit, value) -> None:
        self.__suit = suit
        self.__value = value

    def __lt__(self, otherCard):
        return self.getValue() < otherCard.getValue()

    def __gt__(self, otherCard):
        return self.getValue() > otherCard.getValue()

    def __eq__(self, otherCard):
        return self.getValue() == otherCard.getValue()

    def getSuit(self):
        return self.__suit

    def getValue(self):
        return self.__value

    def setSuit(self, newSuit):
        self.__suit = newSuit

    def setValue(self, newValue):
        self.__value = newValue
