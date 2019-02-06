"""
created on 1/28/19
created by: root
"""
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player:
    def __init__(self, name, money, table_pos, hand):
        self.name = name
        self.money = money
        self.table_pos = table_pos
        self.hand = hand

    def adjust_money(self, bet_result):
        if self.name == "Dealer":
            pass
        else:
            self.money = self.money + bet_result


class NPC(Player):
    def __init__(self, name, money, table_pos, hand):
        Player.__init__(self, name, money, table_pos, hand)
        if self.name == "Dealer":
            print(bcolors.BOLD + bcolors.OKGREEN + "{0} initialized.".format(self.name))
        else:
            print(bcolors.BOLD + bcolors.OKGREEN+"{0} initialized. ${1}".format(self.name, self.money))


    def NPCBet(self):
        if self.money > 100:
            bet = random.randint(1, 9) * 10
        else:
            bet = 10
        return bet


class User(Player):
    def __init__(self, name, money, table_pos, hand):
        Player.__init__(self, name, money, table_pos, hand)
        print("{0} initialized. ${1}".format(self.name, self.money))

    def player_bet(self):
        #Catch exceptions
        player_bet = input(bcolors.OKBLUE+"How much would you like to bet?"+bcolors.ENDC)
        return player_bet


class Dealer(NPC):
    def __init__(self, name, money, table_pos, hand):
        NPC.__init__(self, name, money, table_pos, hand)


"""
class Deck:
    def __init__(self):
        for suit in suits:
            for value in card_list:
                card = card[suit, value]
                self.append(card))

    def card_value(self, card):
        if card.value == "A":
            return 11
        elif card.value== "K" or "Q" or "J":
            return 10
        else:
            return int(card.value)


    def Shuffle(self, deck):
        random.shuffle(deck)

"""


if __name__ == "__main__":
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    #suits = ["♠", "♥", "♦", "♣"]
    card_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    """
        #let's set up the deck
        #deck = Deck()
        print(deck[0], deck[13], deck[14], deck[26])
    """


    #let's set up the players
    print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to Blackjack!!!!!!" + bcolors.ENDC)
    dealer = Dealer("Dealer", 100000, 0, [])
    npc1 = NPC("Player 1", 10000, 1, [])
    npc2 = NPC("Player 2", 10000, 2, [])

    name_check = 1
    while name_check:
        try:
            user_name = input("What is your name?")
            name_check = 0
        except EOFError:
            print("I can't use that. Try again.")
        except KeyboardInterrupt:
            print("I can't use that. Try again.")

    player = User(user_name, 10000, 3, [])
    player_list = [dealer, npc1, npc2, player]

    game_exit = 0;
    while not game_exit:
        print("Money")
        for players in player_list:
            print(bcolors.WARNING + players.name + "     " + "$" + str(players.money) + bcolors.ENDC)
        print("LET'S PLAY!!!")
        #player.player_bet()

        play_on = 1
        while play_on:
            try:
                keep_play = input("Would you like to play another hand? (Y or N)")
                if keep_play == ("N" or "n"):
                    print("Thanks for playing!!!")
                    game_exit = 1
                    play_on = 0
                else:
                    game_exit = 0
                    play_on = 0
            except EOFError:
                print("I can't use that. Try again.")
            except KeyboardInterrupt:
                print("I can't use that. Try again.")






