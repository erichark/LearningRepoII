"""
created on 1/28/19
created by: root
Testing changes
"""
import random
from reportbug.ui.text_ui import handle_bts_query

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
    
    
    def print_hand(self, hand):
        for card in hand:
            print(hand[card].value)
            
    
    def hand_value(self, hand):
        card_sum = 0
        for card in hand:   
            if card.value == "A":
                card_sum = card_sum + 11
            elif card.value== "K" or "Q" or "J":
                card_sum = card_sum + 10
            else:
                card_sum = card_sum + int(card.value)
        return card_sum
     

            

class NPC(Player):
    def __init__(self, name, money, table_pos, hand):
        Player.__init__(self, name, money, table_pos, hand)
        print(bcolors.BOLD + bcolors.OKGREEN+"{0} initialized. ${1}".format(self.name, self.money))


    def NPCBet(self):
        if self.money > 100:
            bet = random.randint(1, 9) * 10
        else:
            bet = 10
        return bet


class Dealer(Player):
    def __init__(self, name, money, table_pos, hand):
        Player.__init__(self, name, money, table_pos, hand)
        print(bcolors.BOLD + bcolors.OKBLUE + "{0} initialized.".format(self.name))        
        

class User(Player):
    def __init__(self, name, money, table_pos, hand):
        Player.__init__(self, name, money, table_pos, hand)
        print("{0} initialized. ${1}".format(self.name, self.money))

    def player_bet(self):
        #Catch exceptions
        player_bet = input(bcolors.OKBLUE+"How much would you like to bet?"+bcolors.ENDC)
        return player_bet


class Card:
    def __init__(self, value):
        self.value = value

        
class Deck:
    def __init__(self):
        self.deck = []
        for value in card_list:
            self.deck.append(Card(value))
        random.shuffle(self.deck)       

    
    def print_deck(self):
        for card in self.deck:
            print(card.value)

    def get_card(self):
        if not deck:
            pass  #need to shuffle and create a new deck
        else:
            self.print_deck()
            new_card = self.deck.pop()
            return new_card


if __name__ == "__main__":
    #suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    suits = ["♠", "♥", "♦", "♣"]
    card_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


    #let's set up the deck
    deck = Deck()

    #let's set up the players
    print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to Blackjack!!!!!!" + bcolors.ENDC)
    npc1 = NPC("Player 1", 10000, 0, [])
    npc2 = NPC("Player 2", 10000, 1, [])
    dealer = Dealer("Dealer", 100000, 3, [])

    name_check = 1
    while name_check:
        try:
            user_name = input("What is your name?")
            name_check = 0
        except EOFError:
            print("I can't use that. Try again.")
        except KeyboardInterrupt:
            print("I can't use that. Try again.")

    player = User(user_name, 10000, 2, [])
    player_list = [npc1, npc2, player, dealer]
    
    #deal out initial cards, we deal two cards to start. 
    for players in player_list:
        new_card = deck.get_card()
        players.hand.append(new_card)
        new_card = deck.get_card()
        players.hand.append(new_card)
       

    game_exit = 0;
    while not game_exit:
        print("/n")
        print(bcolors.BOLD + "Money" + bcolors.ENDC)
        for players in player_list:
            print(bcolors.WARNING + players.name + "     " + "$" + str(players.money) + bcolors.ENDC)
        print("LET'S PLAY!!!")
        
        for players in player_list:
            if players.__class__.__name__ == "NPC":
                npc_bet = players.NPCBet()
                print("{0} shows a {1}".format(players.name, players.hand[0].value))
                print("{0} bets ${1}".format(players.name, str(players.money)))
                #player plays cards
                card_sum = players.hand_value(players.hand)
                while card_sum >= 21:
                    if card_sum > 14:
                        new_card = deck.get_card()
                        players.hand.append(new_card)
                    elif 14 <= card_sum <= 17:
                        guess = random.randint(1,10)
                        if guess > 7:
                            new_card = deck.get_card()
                            players.hand.append(new_card)
                        else:
                            continue
                if card_sum > 21:
                    print(players.name, "has gone bust!")
                else:
                    print(players.name, "holds at", card_sum)
                
            elif players.__class__.__name__ == "User":
                print(bcolors.OKBLUE + bcolors.BOLD +"It's your turn."+ bcolors.ENDC)
                user_play = 1
                while user_play:
                    print(bcolors.OKBLUE + "Your cards are: {0} and {1}".format(players.hand[0].value, players.hand[1].value))
                    user_choice = input("What would you like to do? (1 = hit, 0 = stay)")
                    if user_choice:
                        new_card = deck.get_card()
                        print("Your new card is a", str(new_card.value))
                        players.hand.append(new_card)
                        card_sum = players.hand_value(players.hand)
                        if card_sum > 21:
                            print(bcolors.FAIL + bcolors.BOLD +"You're BUST!" + bcolors.ENDC)
                            user_play = 0
                        else:
                            continue 
                    else:
                       user_play = 0
                        
            else:
                dealer_play = 1
                while dealer_play:
                    if sum(players.hand) < 17:
                        new_card = deck.get_card()
                        players.hand.append(new_card)
                    elif 17 <= sum(player.hand) <= 21:
                        dealer_play = 0
                    else: 
                        dealer_play = 0
                        print(bcolors.BOLD + bcolors.OKGREEN + "DEALER IS BUST!! EVERYONE WINS!!!" + bcolors.ENDC)
                        
        #Let's compare and pay out
        print(bcolors.BOLD + bcolors.WARNING + "Dealer has: ", sum(int(dealer.hand) +bcolors.ENDC))
        for players in player_list:
            if players.__class__.__name__ is not "Dealer":
                if sum(players.hand) > sum(dealer.hand):
                    print("{0} has {1}. {0}'s hand wins!")
                    #call adjust_money...but have I lost the bet amount from above?
                

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






