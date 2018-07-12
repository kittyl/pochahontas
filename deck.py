# Python module defining a deck of cards and the hand rankings 
import random 

class Deck(): 
   def __init__(self): 
      self.cards = ["2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Ks", "Qs", "As", 
                    "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Kd", "Qd", "Ad", 
                    "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Kh", "Qh", "Ah", 
                    "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Kc", "Qc", "Ac"]

   def deal_one_card(self): 
      dealt_card = random.choice(self.cards) 
      self.cards.remove(dealt_card) 
      return(dealt_card) 

   def deal_two_cards(self): 
      dealt_card1 = random.choice(self.cards) 
      self.cards.remove(dealt_card1) 
      dealt_card2 = random.choice(self.cards) 
      self.cards.remove(dealt_card2) 
      return((dealt_card1, dealt_card2)) 
      
