import random

value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,   'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
player_val = 0
dealer_val = 0
game_on = True


'''CLASSES'''


class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = value[rank]

  def __lt__(self, other):
         return self.value < other.value

  
  def __str__(self):
    return self.rank +" of " + self.suit + " valued at " + f"{self.value}"


class Deck:

  def __init__(self):
    self.all_cards = []

    for suit in suits:
      for rank in ranks:
        created_card = Card(suit,rank)
        self.all_cards.append(created_card)

  def shuffle(self):
    random.shuffle(self.all_cards)

  def draw_one(self):
    return self.all_cards.pop()


class Player:
  
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.acc = 100
    
  def __str__():
    return f"{self.name}, your balance is {self.acc}"

  def add_one(self,new_card):
    self.hand.append(new_card)

  def adjust_bal(self, bet, result,):
    if result == "plus":
      return self.acc + (bet*2)
    elif result == "blackjack":
      return self.acc + (bet*2.5)
    elif result == "draw":
      return self.acc + bet
    else:
      return self.acc - bet

class Dealer:
  def __init__(self):
    self.hand = []

  def add_one(self,new_card):
    self.hand.append(new_card)


''' METHODS '''


def new_screen():
  print ("\n" * 15)
  
def player_value(player_val, cards):
  player_val = 0
  sorted_cards = sorted(cards)
  for x in sorted_cards:
    if x.value == 11:
      if player_val + 11 < 22:
        player_val += x.value
      else: 
        player_val += 1
    else:
      player_val += x.value
  
  return player_val 

def dealer_value(dealer_val, cards):
  dealer_val = 0
  sorted_cards = sorted(cards)
  for x in sorted_cards:
    if x.value == 11:
      if dealer_val + 11 < 22:
        dealer_val += x.value
      else: 
        dealer_val += 1
    else:
      dealer_val += x.value
  
  return dealer_val

def another_round(game_on):
  ask = input("do you want to play another round? y or n")
  if ask == "y":
    print ("OK let's go again..")
    game_on = True
    print (game_on)
  else:
    print (f"thanks for playing, you leave the table with {player_one.acc} in your account")
    game_on = False

  return game_on


'''GAME SETUP'''


name = input("Hello, what is your name? ")
player_one = Player(name)
dealer_one = Dealer()

game_on = True
result = ""


'''LOGIC'''


print (f"ok {player_one.name}, lets play BLACKJACK")

while game_on == True:
  deck_one = Deck()
  deck_one.shuffle()
  valid = False
  player_one.hand = []
  dealer_one.hand = []
  
  print (f"your account balance is {player_one.acc}") 

  while valid == False:
    bet = int(input(f"{player_one.name} how much do you want to bet this round? enter a number:\n"))
    if bet > player_one.acc:
      print ("that's not a valuid bet")
      valid = False
    else:
      valid = True
      
  result = "minus"
  player_one.acc = player_one.adjust_bal(bet, result)

  new_screen()
  print (f"you bet {bet} and your remaining balance is {player_one.acc}")
  print("let's play, the dealer starts to deal...")



  for x in range(2):
    player_one.add_one(deck_one.draw_one())
    dealer_one.add_one(deck_one.draw_one())

  player_val = player_value(player_val, player_one.hand)
  dealer_val = dealer_value(dealer_val, dealer_one.hand)
  
  
  print ("In your hand you have:")
  for x in player_one.hand:    
    print (x)
  
  print(f"you have {player_val}")

  if player_val == 21:
    print ("BLACKJACK! You win BIG!")
    result = "blackjack"
    player_one.acc = player_one.adjust_bal(bet, result)
    print (f"your account balance is now {player_one.acc}")
    game_on = another_round(game_on)
    break
  else:
    action = input("do you want to stick or twist? enter t or s")
    
    while action == "t":
      player_one.add_one(deck_one.draw_one())
      print (f"you got {player_one.hand[-1]}")
      player_val = player_value(player_val, player_one.hand)
      
      if player_val >=22:
        print (f"You have {player_val}")
        print ("you are bust, you lose this hand")
        print (f"your account balance is now {player_one.acc}")
        if player_one.acc > 0:
          game_on = another_round(game_on)
        else:
          print ("your are broke! Get lost loser!")
          game_on = False
          break
        break
      elif player_val == 21:
        print ("21! you stick")
        break
      else:
        print (f"you have {player_val}")
        action = input("do you want to stick or twist? enter t or s")
        
    if player_val < 22:
      new_screen()
      print ("now it's the dealer's turn...")
      print (f"the dealer has in their hand:")
      for x in dealer_one.hand:    
        print (x)
    
      print (f"the dealer has {dealer_val}")
  
      if dealer_val >= 16:
        pass
      else:
        while dealer_val < 16:
          dealer_one.add_one(deck_one.draw_one())
          dealer_val = dealer_value(dealer_val, dealer_one.hand)  
          print (f"the dealer deals themself a {dealer_one.hand[-1]} and now has {dealer_val}")
        
      if dealer_val > 22:
        result = "plus"
        player_one.acc = player_one.adjust_bal(bet, result)
        print ("the dealer has bust! you win this hand")
        print (f"You win {bet} and your new account balance is {player_one.acc}")
        
    
      elif dealer_val >= 16 and dealer_val == player_val:
        result = "draw"
        player_one.acc = player_one.adjust_bal(bet, result)
        print ("its a draw! you get you money back")
        print (f"Your account balance is {player_one.acc}")
       
    
      elif dealer_val >= 16 and dealer_val < player_val:
        result = "plus"
        player_one.acc = player_one.adjust_bal(bet, result)
        print (f"The dealer sticks on {dealer_val}. You have {player_val}, you win!")
        print (f"Your account balance is {player_one.acc}")
                                              
    
      elif dealer_val >= 16 and dealer_val > player_val:
        print (f"The dealer sticks on {dealer_val}. You have {player_val}, you lose :(")
        print (f"Your account balance is {player_one.acc}")
        
    
  if player_one.acc > 0:
    game_on = another_round(game_on)
  else:
    print ("your are broke! Get lost loser!")
    game_on = False
