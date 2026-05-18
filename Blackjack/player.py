from participant import Participant
from deck import Deck
# Divider constant for easier printing
DIVIDER = "-------------------"

class Player(Participant):
    '''
    Player inherits from Participant
    '''
    def __init__(self, name : str) -> None:
        super().__init__(name)

    '''
    The player chooses whether to hit or stand, as long as the bust
    conditions have not been fulfilled
    '''
    def take_turn(self, deck : Deck) -> None:
        print(DIVIDER)
        print("Your turn")
        print(DIVIDER)
        hit_stand = 'h'
        while hit_stand != 's' and not self.is_busted():
            hit_stand = input("Would you like to hit (take card) or stand (not take)? (h/s): ")
            while hit_stand != 'h' and hit_stand != 's' and not hit_stand:
                hit_stand = input("Please enter a valid choice: ")
            if hit_stand == 'h':
                self.take_card(deck.deal_card())
                print(f"\nYou draw: {self.hand.cards[-1]}")
                print(f"Your total: {self.hand.get_total()}\n")

if __name__ == "__main__":
    player = Player("Name")
    d = Deck()
    d.build_deck()
    d.shuffle()
    player.take_turn(d)