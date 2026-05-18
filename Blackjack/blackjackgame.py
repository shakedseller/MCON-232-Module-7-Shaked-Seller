from deck import Deck
from player import Player
from dealer import Dealer
# Divider constant for easier printing
DIVIDER = "-------------------"

class BlackjackGame:
    '''
    Blackjack game has a player, dealer, and deck
    '''
    def __init__(self, player_name : str):
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer()

    '''
    Deals two cards to both the player and dealer
    '''
    def initial_deal(self) -> None:
        self.player.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())
        self.player.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())

    '''
    Shows the dealer's card and the player's card at
    the beginning of the game
    '''
    def show_game_state(self) -> None:
        print(f"Dealer shows: {self.dealer.show_first_card()}")
        print("Dealer has: [Hidden Card]")
        print()
        print(f"Your hand: {self.player.show_hand()}")
        print(f"Your total: {self.player.get_total()}")

    '''
    Returns the appropriate winning message depending on the winner
    '''
    def determine_winner(self) -> str:
        if self.player.is_busted():
            return "Result: Dealer won!"
        elif self.dealer.is_busted():
            return "Result: You won!"
        elif self.player.get_total() == self.dealer.get_total():
            return "Result: It's a tie!"
        elif self.player.get_total() > self.dealer.get_total():
            return "Result: You won!"
        elif self.dealer.get_total() < self.player.get_total():
            return "Result: Dealer won!"
        return " "

    '''
    Plays the actual Blackjack game
    '''
    def play(self) -> None:
        print(DIVIDER)
        print("Game Start")
        print(DIVIDER)

        self.deck.build_deck()
        self.deck.shuffle()
        self.initial_deal()
        self.show_game_state()

        self.player.take_turn(self.deck)

        if not self.player.is_busted():
            self.dealer.take_turn(self.deck)

        print(DIVIDER)
        print("Final hands")
        print(DIVIDER)
        print(f"Dealer hand: {self.dealer.show_hand()}")
        print(f"Dealer total: {self.dealer.get_total()}")
        print()
        print(f"Your hand: {self.player.show_hand()}")
        print(f"Your total: {self.player.get_total()}")
        print(DIVIDER)

        print(self.determine_winner())
        print(DIVIDER)

