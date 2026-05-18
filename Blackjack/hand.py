from card import Card

class Hand:
    '''
    Hand has a list of cards
    '''
    def __init__(self) -> None:
        self.cards = []

    '''
    Adds a card to the hand
    '''
    def add_card(self, card : Card) -> None:
        self.cards.append(card)

    '''
    Returns the total of the hand
    Applies the ace rule: if an ace with value 11 would cause the player
    to bust, use a value of 1 instead
    '''
    def get_total(self) -> int:
        total = 0
        for c in self.cards:
            if c.rank == "Ace":
                if total + c.value[1] > 21:
                    total += c.value[0]
                else:
                    total += c.value[1]
            else:
                total += c.value

        return total

    '''
    Shows the hand of the participant
    '''
    def show_hand(self) -> str:
        card_hand = []
        for c in self.cards:
            card_hand.append(f"{c}")

        return ", ".join(card_hand)

if __name__ == "__main__":
    h = Hand()
    h.cards.append(Card("H", "K", 10))
    h.cards.append(Card("D", "A", 11))

    print(h.show_hand())