from deck import Deck 
from hand import Hand 
from player import Player

player1 = Player(100) 
player2 = Player(100) 
player3 = Player(100) 

hand1 = Hand([player1, player2, player3], 0, 5, 10) 
hand1.place_blinds() 
hand1.deal_players() 


