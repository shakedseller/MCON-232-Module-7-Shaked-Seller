from participant import Participant
from deck import Deck
# Divider constant for easier printing
DIVIDER = "-------------------"

class Dealer(Participant):
    '''
    Inherits from Participant
    '''
    def __init__(self):
        super().__init__("")

    '''
    The dealer keeps taking cards until the total is 17
    '''
    def take_turn(self, deck : Deck) -> None:
        print(DIVIDER)
        print("Dealer's turn")
        print(DIVIDER)
        print(f"Dealer reveals hidden card: {self.hand.cards[-1]}")
        print(f"Dealer total: {self.get_total()}")
        while self.get_total() <= 16:
            self.take_card(deck.deal_card())
            print(f"\nDealer draws: {self.hand.cards[-1]}")
            print(f"Dealer total: {self.get_total()}")

    '''
    Shows the first card for the first turn
    '''
    def show_first_card(self) -> str:
        return self.hand.cards[0]