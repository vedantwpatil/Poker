from card import Card


class Hand:
    def __init__(self, cards: list[Card]) -> None:
        self.__cards = cards

    def getFirstCard(self):
        return self.__cards[0]

    def getSecondCard(self):
        return self.__cards[1]

    def getThirdCard(self):
        return self.__cards[2]

    def getFourthCard(self):
        return self.__cards[3]

    def getFifthCard(self):
        return self.__cards[4]

    def getHand(self):
        return self.__cards

    def __lt__(self, otherHand):
        return self.getValue() < otherHand.getValue()

    def __gt__(self, otherHand):
        return self.getValue() > otherHand.getValue()

    def __eq__(self, otherHand):
        return self.getValue() == otherHand.getValue()

    def isRoyalFlush(self):
        hand = self.getHand()
        firstCard = self.getFirstCard()
        cardSuit = firstCard.getSuit()
        cardValue = firstCard.getValue()

        if cardValue != 10:
            return False
        for i in range(1, len(hand)):
            if hand[i].getSuit() != cardSuit:
                return False
            if hand[i].getValue() != cardValue + 1:
                return False
            cardValue += 1
        return True

    def isStraightFlush(self):
        hand = self.getHand()
        firstCard = self.getFirstCard()
        cardSuit = firstCard.getSuit()
        cardValue = firstCard.getValue()

        for i in range(1, len(hand)):
            if hand[i].getSuit() != cardSuit:
                return False
            if hand[i].getValue() != cardValue + 1:
                return False
            cardValue += 1
        return True

    def isFourOfAKind(self):
        hand = self.getHand()
        value_count = {}
        for card in hand:
            value = card.getValue()
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        return 4 in value_count.values()

    def isFullHouse(self):
        hand = self.getHand()
        value_count = {}
        for card in hand:
            value = card.getValue()
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        return 3 in value_count.values() and 2 in value_count.values()

    def isFlush(self):
        hand = self.getHand()
        firstCard = self.getFirstCard()
        cardSuit = firstCard.getSuit()
        return all(card.getSuit() == cardSuit for card in hand)

    def isStraight(self):
        hand = self.getHand()
        values = sorted([card.getValue() for card in hand])
        return all(values[i] == values[0] + i for i in range(len(values)))

    def isThreeOfAKind(self):
        hand = self.getHand()
        value_count = {}
        for card in hand:
            value = card.getValue()
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        return 3 in value_count.values()

    def isTwoPair(self):
        hand = self.getHand()
        value_count = {}
        for card in hand:
            value = card.getValue()
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        pairs = sum(1 for count in value_count.values() if count == 2)
        return pairs == 2

    def isOnePair(self):
        hand = self.getHand()
        value_count = {}
        for card in hand:
            value = card.getValue()
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        return any(count == 2 for count in value_count.values())

    def getValue(self):
        if self.isRoyalFlush():
            return 10
        elif self.isStraightFlush():
            return 9
        elif self.isFourOfAKind():
            return 8
        elif self.isFullHouse():
            return 7
        elif self.isFlush():
            return 6
        elif self.isStraight():
            return 5
        elif self.isThreeOfAKind():
            return 4
        elif self.isTwoPair():
            return 3
        elif self.isOnePair():
            return 2
        else:
            return 1
