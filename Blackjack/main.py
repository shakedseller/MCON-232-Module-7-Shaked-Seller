from blackjackgame import BlackjackGame
'''
Starts the Blackjack game
'''
print("--- WELCOME TO BLACKJACK ---")
name = input("Please enter your name: ")
while not name:
    name = input("Please enter a valid name: ")

blackjack = BlackjackGame(name)
blackjack.play()