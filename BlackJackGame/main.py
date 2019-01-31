"""
created on 1/28/19
created by: root


player
    name
    money
    position at table
    dealer flag?
    cards in hand

card
    value
    suit

deck
    builds a set of 52 cards
    (Do I want to set up a set of 5 decks, or just randomly generate cards?)

Methods (what do they attach to? which class?):
    deal
    non - player decision/action
    dealer decision/action
    calculate money loss/gain


how to join a player with his hand?


Use case - Player setup:
Instantiate the dealer
Greet player
Ask for name
Instantiate player
Ask how many people they want to play against
Instantiate the other players

Use case - initial deal
deal one card down to all npcs
deal one card down and tell player thier card
deal one card down to dealer
deal one card up to all players (how to handle Aces?)


Use case - player has an Ace
    NPC -
        if they have a jack - WINNER
        add cards with Ace value as 11, if sum over 21 ace = 1. if less, and sum is 19-21, stay, if not ace = 1 and hit (?)

    Player -
        calculate sum, if over 21, make ace = 1, if not, ask player what to do.

    Dealer -
        calculate sum, if over 21, ace = 1, if 17-21, stay, if under 17, hit.

Use case - playing the game
    npc players  -
        if sum is less than 14, hit
        if sum is 15-16, hit 2 in 3 times
        if sum 1s 17-18, hit 1 in 3 times
        if sum is 19+, stand
        if sum is 21+, tell player is out
    Player
        tell player sum
        ask if they want to hit, or stand
        if hit, give player new card, tell player sum
        if over 21, bust, if under
        repeat
    Dealer
        if sum > 17 hit
        if sum <= 17, stand
        once dealer stands, compare to each player and indicate winners and losers and increment $$$

Phase II - split/double down/etc?

"""
import random

class Player:
    def __init__(self, name, money, table_pos, cards):
        self.name = name
        self.money = money
        self.table_pos = table_pos
        self.cards = cards

    def adjust_money(self, bet_result):
        if self.name == "Dealer":
            pass
        else:
            self.money = self.money + bet_result


class NPC (Player):
    def __init__(self):
        pass

    def NPCBet(self):
        if self.money > 100:
            bet = random.randint(1,9) * 10
        else:
            bet = 10
        return bet


class User(Player):
    pass

class Dealer(Player):
    pass

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def cardValue(self):
        if self.value == "A":
            return 11
        elif self.value== "K" or "Q" or "J":
            return 10
        else:
            return str(self.value)


class Deck(Card):
    def __init__(self):
        pass


"""
    def Shuffle(self):
        random.shuffle(self)

"""


if __name__ =="__main__":
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    #suits = ["♠", "♥", "♦", "♣"]
    card_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")



    pass


