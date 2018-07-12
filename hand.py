# Python class to represent one hand 
from deck import Deck 
from player import Player 

class Hand(): 
   # We are assuming the players are in position to act here 
   def __init__(self, players, buttonplayer, smallblind, bigblind): 
      self.buttonplayer = buttonplayer 
      # Just assuming button player is the first player here 
      # So the players list is ordered according to order to act 
      self.players = players 
      self.active_players_pos = range(0,len(players)) 
      self.players_to_act_pos = range(0,len(players)) 
      self.deck = Deck() 
      self.smallblind = smallblind 
      self.bigblind = bigblind 
      self.pot = 0 
      self.flop = None 
      self.turn = None 
      self.river = None 
      self.action_when = None 
      self.player_to_act_pos = -1 
      self.nplayers = len(players) 
      self.curbet = 0 

   def place_blinds(self): 
      self.pot = self.smallblind + self.bigblind 
      self.players[0].stack = self.players[0].stack - self.bigblind 
      self.players[1].stack = self.players[1].stack - self.smallblind 
      self.curbet = self.bigblind 
 
   # Returns the player that is next to act       
   def next_to_act(self): 
      if self.action_when == None: 
         print("Need to deal first") 
      else: 
         return(self.players[self.player_to_act_pos])  

   def do_action(self,someaction, betsize): 
      type_of_action = self.action_when 
      player_to_act = self.next_to_act() 
      player_to_act.do_action_player(someaction, betsize, type_of_action) 

      # If this player folds, then remove this player from list of active players 
      if someaction == "fold": 
         self.active_players_pos.remove(self.player_to_act_pos) 

      # If this player calls, then put some money in the pot 
      # If there is no current bet, then assume this is a check 
      if someaction == "call": 
         player_to_act.stack -= self.curbet 
         self.pot += self.curbet 
          
      # If this player bets, then work out what the current bet size is  
      if someaction == "bet": 
          # Check that the bet is as big as the current bet 
          if betsize <= self.curbet: 
             print("Betsize needs to be as big as the current bet which is ", self.curbet) 
             return() 
         
          self.curbet = betsize 
          player_to_act.stack -= betsize 
          self.pot += betsize   
   
      # Let's move the next player to act along 
      self.player_to_act_pos = self.find_next_active_pos() 

      # If there is only one active player left, then this player wins the pot 
      if len(self.active_players_pos) == 1: 
         self.players[self.player_to_act_pos].stack += self.pot  
         print("Hand is done. Pot size is ", self.pot, " current phase is: ", self.action_when)  
         return(1) 
      else: 
         print("Pot size is ", self.pot, " next player to act ", self.player_to_act_pos)  

   # Given the current player to act, find the position in the players list of 
   # the next player 
   def find_next_active_pos(self): 
      next_player_to_act_pos = ( self.player_to_act_pos + 1 ) % self.nplayers 
      while(next_player_to_act_pos not in self.active_players_pos):  
         next_player_to_act_pos = ( next_player_to_act_pos + 1 ) % self.nplayers 
      return(next_player_to_act_pos) 
 
   def deal_players(self): 
      # Start of the hand where each player is dealt two cards  
      for player in self.players: 
         player.holecards = self.deck.deal_two_cards() 
      self.action_when = "Preflop" 
      # Under the gun position is the next to act in preflop 
      self.player_to_act_pos = 2 

   def deal_flop(self): 
      # Check that all players have either acted or folded preflop 
      flop1 = self.deck.deal_one_card()        
      flop2 = self.deck.deal_one_card()        
      flop3 = self.deck.deal_one_card()        
      self.flop = (flop1, flop2, flop3) 
      self.action_when = "Postflop" 
      self.player_to_act_pos = self.active_players_pos[0]  
      self.curbet = 0  

   def deal_turn(self): 
      # Check that all players have either acted or folded preflop 
      turncard = self.deck.deal_one_card()        
      self.turn = turncard 
      self.action_when = "Turn" 
      self.player_to_act_pos = self.active_players_pos[0]  
      self.curbet = 0  

   def deal_turn(self): 
      turncard = self.deck.deal_one_card()        
      self.turn = turncard 
      self.action_when = "Turn" 
      self.player_to_act_pos = self.active_players_pos[0]  
      self.curbet = 0  

   def deal_river(self): 
      rivercard = self.deck.deal_one_card()        
      self.river = rivercard
      self.action_when = "River" 
      self.player_to_act_pos = self.active_players_pos[0]  
      self.curbet = 0  
