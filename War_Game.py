''' Game of cards where two player will compare their card and the player has bigger card will take both the cards.
	if Both card has same ranking its a WAR..both player will pull 2 additional card each to keep aside the cards and will replay the game.
	Who ever wins will keep all the cards. If it will be a tie again , Game will be TIE.
    finally the layer who will have all 52 cards will win the game
'''

import numpy as np

class Card():

    ''' This class will
    1) create a card Object with a definite Color and value. Also ranking will be assigned to each card
    2) Dunder method to print a card object
    '''

    colors = ['heart', 'diamonds', 'spades', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}

    def __init__(self,value,color):
        self.value = value
        self.color=color
        self.ranking = Card.rank[value]

    def __str__(self):
        return f"{self.value} of {self.color} having ranking as {self.ranking}"

class Deck():

    ''' This class will be used to
    1) create a deck of cards Objects during intialization
    2) a Method to shuffle the deck
    3) a Dunder method to print the deck
    '''

    deck_list = []

    # create a deck of card while initialization of the class
    def __init__(self):
        loop_count = 1
        for i in Card.colors:
            for j in Card.values:
                card_details = Card(j,i)
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

class Player():

    '''
    1) Player class to assign card deck while initializing
    2) Method to pull and assign cards
    3) Method to validate victory of a player for each pull or war condition
    4) dunder method to print a player that wil intern will print his cards that a player
       has currently at any stage of the game
     '''

    def __init__(self,assigned_card_list):
        self.assign_card_list = assigned_card_list

    def pull_card(self,n):
        return self.assign_card_list.pop(n)

    def assign_cards(self,card_list):
        self.assign_card_list.extend(card_list)

    def validate_victory(self):

        if (len(self.assign_card_list) == 0 ):
            return 1
        else:
            return 0


    def __str__(cls):

        assign_cards = []
        for j in cls.assign_card_list:
            card = j.value + ' of ' +  j.color
            assign_cards.append(card)
        return f"{assign_cards}"

############################## Game Logic ##################################

'''create a new Deck of 52 Card Objects'''
Card_Deck = Deck()

'''Shuffle the deck'''
Card_Deck.shuffle_deck()

print ("Card deck is created and shuffled that has : {}".format(Card_Deck))

even_odd = 1
Player_1_card = []
Player_2_card = []

'''Distribute equal cards in two players'''

for j in Card_Deck.deck_list:
    if(even_odd%2 == 0):
        Player_1_card.append(j)
    else:
        Player_2_card.append(j)

    even_odd += 1

'''Assign equal card Deck to each player'''

Player_1 = Player(Player_1_card)
Player_2 = Player(Player_2_card)

print ( "Card desk for Player 1 is : {}".format(Player_1))
print ( "Card desk for player 2 is : {}".format(Player_2))

'''Variable  to identify how many rounds are played before a player won the game'''
loop = 1

while True :

    ''' Pull 1 card from the deck'''

    card_player_1 = Player_1.pull_card(np.random.randint(0, len(Player_1_card)))
    card_player_2 = Player_2.pull_card(np.random.randint(0, len(Player_2_card)))

    print ("Card Pulled by player 1 is : {} ".format(card_player_1))
    print ("Card Pulled by player 2 is : {} ".format(card_player_2))

    if (card_player_1.ranking > card_player_2.ranking) :

        assign_card_list_temp = [card_player_1,card_player_2]
        Player_1.assign_cards(assign_card_list_temp)

    elif (card_player_2.ranking > card_player_1.ranking) :

        assign_card_list_temp = [card_player_1, card_player_2]
        Player_2.assign_cards(assign_card_list_temp)

    elif (card_player_2.ranking == card_player_1.ranking):

        #Pull 2 additional card from the each deck'''
        print ("its a WAR !! Ranking of Both cards of Player 1 & 2 is same . Pulling two additional card for each player")

        try:
            if ( len(Player_1_card) < 3 and len(Player_2_card) < 3 ) :
                print ("Both Player 1 & layer 2 dont have sufficient card, Its a Tie!!!")
                raise
            elif ( len(Player_1_card) < 3 and  len(Player_2_card) > 3 ):
                print ("Player 1 dont have sufficient card, Player 2 is winner in this WAR!!!")
                raise
            elif (len(Player_2_card) < 3 and len(Player_1_card) > 3):
                print  ("Player 2 dont have sufficient card, Player 1 is winner in this WAR!!!")
                raise
            else:
                card_player_1_2 = Player_1.pull_card(np.random.randint(0, len(Player_1_card)))
                card_player_1_3 = Player_1.pull_card(np.random.randint(0, len(Player_1_card)))
                print("First additional Card Pulled by player 1 is : {} ".format(card_player_1_2))
                print("Second additional card Pulled by player 1 is : {} ".format(card_player_1_3))
                card_player_2_2 = Player_2.pull_card(np.random.randint(0, len(Player_2_card)))
                card_player_2_3 = Player_2.pull_card(np.random.randint(0, len(Player_2_card)))
                print("First additional Card Pulled by player 1 is : {} ".format(card_player_2_2))
                print("Second additional card Pulled by player 1 is : {} ".format(card_player_2_3))
                card_player_1_4 = Player_1.pull_card(np.random.randint(0, len(Player_1_card)))
                card_player_2_4 = Player_2.pull_card(np.random.randint(0, len(Player_2_card)))
                print("Final Card Pulled by player 1 for re-comparision is : {} ".format(card_player_1_4))
                print("Final Card Pulled by player 1 for re-comparision is : {} ".format(card_player_2_4))
                assign_card_list_temp = [card_player_1, card_player_2, card_player_1_2, card_player_1_3, card_player_1_4,
                                    card_player_2_2,card_player_2_3, card_player_2_4 ]

                try:
                    if (card_player_1_4.ranking > card_player_2_4.ranking):
                        print("Player 1 is winner in this WAR!!!")
                        Player_1.assign_cards(assign_card_list_temp)

                    elif (card_player_2_4.ranking > card_player_1_4.ranking):
                        print("Player 2 is winner in this WAR!!!")
                        Player_2.assign_cards(assign_card_list_temp)

                    elif (card_player_2_4.ranking == card_player_1_4.ranking):

                        print ("Its a TIE again !!! Quiting ......")
                        raise
                except:
                    print("Thank you")
                    break
        except:
            print("Thank you")
            break

    print("Card desk for Player 1 is after round {} is : {}".format(loop,Player_1))
    print("Card desk for Player 2 is after round {} is : {}".format(loop,Player_2))

    loop += 1
    ''' validate victory after each round '''
    Player_1_win = Player_1.validate_victory()
    Player_2_win = Player_2.validate_victory()

    if (Player_1_win == 1):
        print ("Player 2 has won !!! ")
        break
    elif(Player_2_win == 1):
        print ("Player 1 has won !!! ")
        break
    else:
        continue
else:
        print('Thank you for playing!!!')