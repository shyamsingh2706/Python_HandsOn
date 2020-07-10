'''
1) Create a Deck of 52 card and shuffle the same
2) make sure Player bet dont cross available chips
3) assign two card to each player i.e. Human Player and computer dealer
4) show only one card of the dealer and both card of Human player
5) Ask Human Player to place the bet
6) ask player if he want to Hit to take another card or Stay. (If ACE card, take inout from user if he want to override the Ace value to 1 or 11)
7) if Human Player doesnt BUST ( go over 21) , ask him of he want another Hit or stay
8) if Player stands, Player the dealer's Hand. Dealer will always Hit until dealer value exceeds Human value
   or Dealer will BUST
9) If Human player Bust , Dealer Wins. If Delaer Bust , Human player win and if Dealer beat Human player , Dealer Wins
10) Determine the winner and adjust the chips accordingly. if Human Player wins , he will get 2 times of chips that he placed on bet as reward.
'''

import numpy as np

class Card():

    ''' This class will
    1) create a card Object with a definite Color and value. Also it will assign a card value for each type of card
    2) Handle the scenario through an attribute that will determine whether a user want to override the ace value or not.
    2) Dunder method to print a card object
    '''

    colors = ['heart', 'diamonds', 'spades', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_points = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

    def __init__(self,value,color,ace_override_value):
        self.value = value
        self.color=color
        self.point_on_card = Card.card_points[value]
        self.ace_override_value = ace_override_value

    def __str__(self):
        return f"{self.value} of {self.color} having ranking as {self.ranking}"

class Deck():

    ''' This class will be used to
    1) create a deck of cards Objects during intialization
    2) a Method to shuffle the deck
    3) a Dunder method to print the deck
    4) a method to pull a card from deck.
    '''

    deck_list = []

    # create a deck of card while initialization of the class
    def __init__(self):
        loop_count = 1
        for i in Card.colors:
            for j in Card.values:
                card_details = Card(j,i,'N')
                self.deck_list.insert(loop_count,card_details)
                loop_count += 1

    # Print the initialized deck of cards when someone is trying to print a deck class
    def __str__(self):
        assign_cards = []
        for j in self.deck_list:
            card = j.value + ' of ' + j.color
            assign_cards.append(card)
        return f"{assign_cards}"

    def shuffle_deck(self):
        np.random.shuffle(self.deck_list)

    def pull_card(self):
        return self.deck_list.pop()

class Player():

    ''' Player class to create a empty deck for a player while initialization and assign chips for each player
    a method to place a bet
    a method to show a specific card ( last available card on the player's deck
    a method to show all card for a specific player
    a method to calculate the total for a player deck after each pull
    a method to take user input when ACE card is pulled to confirm if a player want to override a ACE value to 1 instead of 11
    '''

    def __init__(self,available_chips):
        self.Player_card_deck = []
        self.available_chips = available_chips

    def place_bet(self,chips):
        return np.random.randint(0,chips)

    def show_card(self):
        return f"{self.Player_card_deck[-1].value} of {self.Player_card_deck[-1].color}"

    def calculate_card_total(self):
        card_total=0
        for j in self.Player_card_deck:
            # print (j.value)
            # print(j.color)
            # print(j.ace_override_value)
            if ( j.value == 'A' and j.ace_override_value == 'Y') :
                card_total = card_total + 1
            else:
                card_total = card_total + j.point_on_card
        return card_total

    def show_all(self):
        assign_cards = []
        for j in self.Player_card_deck:
            card = j.value + ' of ' + j.color
            assign_cards.append(card)
        return f"{assign_cards}"

    def __str__(self):
        assign_cards = []
        for j in self.Player_card_deck:
            card = j.value + ' of ' + j.color
            assign_cards.append(card)
        return f"{assign_cards}"

    def select_ace_value(self):
        choice = 'Wrong'
        while True:
            try:
                choice = input('Please enter the Ace value you want to override Ace value to 1 !! Yes / No : ')
                if not (choice.upper() in ('YES','NO')):
                    print ('Please enter input correctly !! : ')
                    raise
            except:
                continue
            else:
                break

        return choice

############################## Game Logic ##################################

'''create a new Deck of 52 Card Objects'''
Card_Deck = Deck()

'''Shuffle the deck'''
Card_Deck.shuffle_deck()

#Create Player
Computer_Dealer = Player(0)
Human_Player = Player(30)

'''  Ask Player to place the bet'''
Chips_on_bet = Human_Player.place_bet(Human_Player.available_chips)
print("{} chips has been available with Human player".format(Human_Player.available_chips))
print("{} chips has been available with Dealer".format(Computer_Dealer.available_chips))
print("{} chips has been placed on Bet by Human player".format(Chips_on_bet))

#  assign 2 cards to each player
Computer_Dealer.Player_card_deck.append(Card_Deck.pull_card())
Computer_Dealer.Player_card_deck.append(Card_Deck.pull_card())
Human_Player.Player_card_deck.append(Card_Deck.pull_card())
Human_Player.Player_card_deck.append(Card_Deck.pull_card())

## Show card for respective player
print("Dealer One Card is {}".format(Computer_Dealer.show_card()))
print("Human Player both cards are {}".format(Human_Player.show_all()))

# Human player will select the cards first to go closer to 21
Game_over = False


while not(Game_over):

    Human_current_card_total = Human_Player.calculate_card_total()
    print("Human Player current card Total is {}".format(Human_current_card_total))
    Human_input = input("You want to Play a HIT or Stay  : ")

    if Human_input.upper() == 'HIT' :

        Human_Player.Player_card_deck.append(Card_Deck.pull_card())
        print("latest pulled card is {}".format(Human_Player.show_card()))

        # Ask Player the ACE value that he wanted to override Ace value if last pulled card is Ace
        if ( Human_Player.Player_card_deck[-1].value == 'A') :

                Ace_override = Human_Player.select_ace_value()
                if (Ace_override.upper() == 'YES' ):
                    Human_Player.Player_card_deck[-1].ace_override_value = 'Y'
                else:
                    Human_Player.Player_card_deck[-1].ace_override_value = 'N'

        # Calculate Total card value as per Ace Value selected
        Human_current_card_total = Human_Player.calculate_card_total()
        print("Now Human Player current card Total is {}".format(Human_current_card_total))

        if Human_current_card_total > 21:
            print("Sorry you lost the game as total card value crossed 21. Computer dealer wins!!")
            Human_Player.available_chips = Human_Player.available_chips - Chips_on_bet
            Computer_Dealer.available_chips = Chips_on_bet
            Game_over = True
            break
        else:
            continue
    else:
        print('You have selected to standDown now. Now its Turn of Computer dealer')


        Dealer_card_total = Computer_Dealer.calculate_card_total()
        print("Dealer current card Total is {}".format(Dealer_card_total))

        while Dealer_card_total < Human_current_card_total :
            print('Dealer card total is still lesser than Human Player card total !!')
            print('Going for a HIT !!!')
            Computer_Dealer.Player_card_deck.append(Card_Deck.pull_card())
            print("latest pulled card is {}".format(Computer_Dealer.show_card()))
            Dealer_card_total = Computer_Dealer.calculate_card_total()
            if Dealer_card_total > 21:
                print("Sorry you lost the game as total card value crossed 21. Human Player wins!!")
                Human_Player.available_chips = (Human_Player.available_chips - Chips_on_bet ) + (Chips_on_bet*2)
                Game_over = True
                break
            else:
                continue
        else:
            print("Dealer Card Total is more than Human Player card total !! Dealer wins !!!")
            Human_Player.available_chips = Human_Player.available_chips - Chips_on_bet
            Computer_Dealer.available_chips = Chips_on_bet
            Game_over = True
            break


print("{} chips has been available with Human player".format(Human_Player.available_chips))
print("{} chips has been available with Dealer".format(Computer_Dealer.available_chips))
print('Thank you for Playing !!!')