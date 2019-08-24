# Helen Li
# April 22, 2015
# Assignment #8: Part #3

import random

cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

player_cards = []
player_values = []

comp_cards = []
comp_values = []

card1p = random.randint(0, len(cards))
a = cards[card1p]
player_cards.append(a)
b = values[card1p]
player_values.append(b)
del values[card1p]
cards.remove(a)

card2p = random.randint(0, len(cards))
c = cards[card2p]
player_cards.append(c)
d = values[card2p]
player_values.append(d)
del values[card2p]
cards.remove(c)


print ("Player hand:", player_cards, "is worth", sum(player_values))

while sum(player_values) < 21:
  again = input("(h)it or (s)tand? ")
  if again == "s":
    print ()
    card1c = random.randint(0, len(cards))
    g = cards[card1c]
    comp_cards.append(g)
    h = values[card1c]
    comp_values.append(h)
    del values[card1c]
    cards.remove(g)
    
    card2c = random.randint(0, len(cards))
    j = cards[card2c]
    comp_cards.append(j)
    k = values[card2c]
    comp_values.append(k)
    del values[card2c]
    cards.remove(j)
    
    print ("Computer hand:", comp_cards, "is worth", sum(comp_values))
    if sum (comp_values) > sum(player_values):
      print ("Computer wins!")
      break
    else:
      while sum(comp_values) < 21:
        ccard = random.randint(0, len(cards))
        m = cards[ccard]
        comp_cards.append(m)
        q = values[ccard]
        comp_values.append(q)
        print ("Computer drew", m)
        del values[ccard]
        cards.remove(m)
        
        print ("Computer hand:", comp_cards, "is worth", sum(comp_values))
        if sum(comp_values) == 21:
          print ("Computer wins!")
          break
        elif sum(comp_values) > 21:
          print ("Bust!")
          print ("Player wins!")
          break
        elif sum(comp_values) > sum(player_values):
          print ("Computer wins!")
          break
    break
      
  else:
    pcard = random.randint(0, len(cards))
    e = cards[pcard]
    player_cards.append(e)
    f = values[pcard]
    player_values.append(f)
    print ("You drew", e)
    del values[pcard]
    cards.remove(e)
    
    print ("Player hand:", player_cards, "is worth", sum(player_values))
    if sum(player_values) == 21:
      print ("Player wins!")
      break
    elif sum(player_values) > 21:
      print ("Bust!")
      print ("Computer wins!")
      break
    
