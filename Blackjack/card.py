class Card:
    '''
    Each card as a suit, rank, and value
    '''
    def __init__(self, suit : str, rank : str, value) -> None:
        self.suit = suit
        self.rank = rank
        self.value = value

    '''
    If you print the card, it'll be in a familiar, readable format 
    '''
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    pass