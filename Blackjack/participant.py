from card import Card
from hand import Hand
from deck import Deck
# Constant for bust conditions
BUST = 21

class Participant:
    '''
    Participant has a name and hand
    '''
    def __init__(self, name : str) -> None:
        self.name = name
        self.hand = Hand()

    '''
    Take one card from the deck
    '''
    def take_card(self, card : Card) -> None:
        self.hand.cards.append(card)

    '''
    Shows the hand of the participant
    '''
    def show_hand(self) -> str:
        return self.hand.show_hand()

    '''
    Returns the total of the participant's hand
    '''
    def get_total(self) -> int:
        return self.hand.get_total()

    '''
    Returns true if the participant's total is greater than 
    the bust constant
    '''
    def is_busted(self) -> bool:
        if self.get_total() > BUST:
            return True
        return False

    '''
    Placeholder method for taking a turn
    '''
    def take_turn(self, deck : Deck) -> None:
        self.take_card(deck.deal_card())
