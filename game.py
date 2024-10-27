from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.deck = [suit + rank for suit in SUITE for rank in RANKS]
        shuffle(self.deck)
        self.hand1, self.hand2 = self.deck[:26], self.deck[26:]

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.insert(0, card)

    def remove(self, card):
        self.cards.remove(card)

    def is_empty(self):
        return len(self.cards) == 0

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def display(self):
        print(f"{self.name}'s Cards: {self.hand.cards}")

# Initialize Game
print("Welcome to Peace! Let's begin...")
human_name = input("Enter your name: ")
bot_name = "Computer"

# Deck and player setup
deck = Deck()
p1 = Player(bot_name, Hand(deck.hand1))
p2 = Player(human_name, Hand(deck.hand2))

# Game loop
while True:
    if p2.hand.is_empty():
        print("Computer Wins! You ran out of cards.")
        break
    elif p1.hand.is_empty():
        print("Congratulations! You won all the cards.")
        break

    # Display players' cards
    p2.display()
    p1.display()

    # Draw cards for battle
    p2_card = p2.hand.cards[-1]
    p1_card = p1.hand.cards[-1]

    # Compare ranks
    rank_p1 = RANKS.index(p1_card[1:])
    rank_p2 = RANKS.index(p2_card[1:])
    print(f"Pit: Your card - {p2_card}, Computer's card - {p1_card}")

    if rank_p2 > rank_p1:
        print("Nice! Your draw is greater!")
        p1.hand.remove(p1_card)
        p2.hand.add(p1_card)
        p2.hand.add(p2_card)
    elif rank_p2 < rank_p1:
        print("Sorry, you lost this round!")
        p2.hand.remove(p2_card)
        p1.hand.add(p2_card)
        p1.hand.add(p1_card)
    else:
        print("It's a draw! This is Peace.")
        break

print("Game Over")
