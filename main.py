'''
what is needed:

-deck
-player(s) - human
  -has account
  - bets on a hand
  - gets 2 cards face up
-dealer
  - gets 2 cards - one 'face up', one 'face down'
'''

'''VARIABLES'''

import random
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,   'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
player_value = 0
dealer_value = 0
game_on = True

'''CLASSES'''

class Player:
  
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.acc = 100
    
  def __str__():
    return f"{self.name}, your balance is {self.acc}"

  def add_one(new_card):
    self.hand.append(new_card)

class Deck:

  def __init__(self):
    self.all_cards = []

  def shuffle():
    random.shuffle(self.all_cards)

  def draw_one():
    return self.all_cards.pop()

class Dealer:
  def __init__(self):
    self.hand = []

  def add_one(new_card):
    self.hand.append(new_card)



''' METHODS '''
def player_value(player_value, cards):
  player_value = 0
  for x in cards:
    if x.value == 11:
      if value + 11 < 22:
        player_value += x.value
    else: 
      player_value += 1
  else:
    player_value += x.value
  
  return player_value 

def dealer_turn(dealer_value, cards):
  dealer_value = 0
  for x in cards:
    if x.value == 11:
      if value + 11 < 22:
        dealer_value += x.value
    else: 
      dealer_value += 1
  else:
    dealer_value += x.value
  
  return player_value


'''game setup'''
name = input("Hello, what is your name? ")
player_one = Player(name)
dealer_one = Dealer()
deck_one = Deck()
game_on = True
'''Logic'''


while game_on == True:
  print (f"ok {player_one.name}, lets play BLACKJACK")
  print (f"your account balance is {player_one.acc}") 
  
  bet = int(input(f"{player_one.name} how much do you want to bet this round? enter a number"))
   
  for x in range(2):
    player_one.add_one(deck_one.draw_one())
    dealer_one.add_one(deck_one.draw_one())
    player_value(player_value, player_one.hand)
    dealer_value(dealer_value, dealer_one.hand)
  
  p

  




''''
  game end checks:

  player gets 21: black jack
  player gets over 21: bust 

  dealer get 21: dealer Wins
  dealer gets over 21: bust


dealer hit >16 but < player total : player Wins
dealer > player total <22: dealer wins



logic

create deck
create player (ask name, assign bank balance)
create dealer (comp)

player bets

deal two cards to player and dealer
display player cards
display 1 dealer card (0)

ask player to take cards until:
- they decline
- total = 21 - black jack, break
- total > 21 - bust, break

dealer take card if total < 16.

stops if total >16 <22
stops if total > 21
wins if total > player total and less than 22 break
loses if total < player total

if player wins, bet is returned x2 and added to acc

ask to play another hand:

loop



'''