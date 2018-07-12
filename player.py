# Module for each player in the game 
# Note that the action of each player is stored within each player Class 

class Player:
   def __init__(self, stack):
      self.stack = stack 
      self.actions = [] 

   def dealcard(self, card1, card2):
      self.card1 = card1 
      self.card2 = card2 

   def do_action_player(self, action_type, betsize, action_when): 
      if(self.actions == []): 
         self.actions = [(action_type, betsize, action_when)] 
      else: 
         self.actions = self.actions.append((action_type, betsize, action_when) ) 

   def last_action_type(self): 
      return(self.actions[-1].action_type) 
 
