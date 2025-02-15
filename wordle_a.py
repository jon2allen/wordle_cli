import random
from enum import Enum

class wordle_match(Enum):
     NO_MATCH =  1
     MATCH_POS = 2
     MATCH_ANY = 3

class wordle:
   def __init__( self, wordle_file ):
      self.wordle_file = wordle_file
      self.wordle_word = ""
      self.winner = False
   def wordle_reader( self ):
      with open(self.wordle_file) as f:
         self.wordle_db = f.readlines()

   def print_wordle_list( self, count ):
      amt = 0
      for word in self.wordle_db:
         if count > amt:
            print("word: ", word )
         count = count - 1

   def pick_wordle_word( self ):
       self.wordle_word = random.choice(self.wordle_db)
       #self.wordle_word = "broom"
       #self.wordle_word = "daddy"
       return self.wordle_word 

   def is_wordle_word( self, word ):
       #print( word )
       for wrd in self.wordle_db:
          if wrd.find(word) > -1:
             # print ("wrd: ", wrd )
             return True
       return False;

   def letter_status( self, letter, pos, index ):
       if index == -1:
          return ( letter, wordle_match.NO_MATCH)
       if pos == index:
          return ( letter, wordle_match.MATCH_POS)
       if index != pos:
          return ( letter, wordle_match.MATCH_ANY )
   
   def get_status_indicator( self, wordle_m ):
       if wordle_m == wordle_match.MATCH_ANY:
          return 'x'
       if wordle_m == wordle_match.MATCH_POS:
          return '$'
       if wordle_m == wordle_match.NO_MATCH:
          return '#'
       return '?'
          
   def print_status( self, status_list ):
       word = ""
       st2 = ""
       for ltr in status_list:
          word += ltr[0]
          st2 += self.get_status_indicator(ltr[1])
       print("word entered         : ",  word )
       print("Letter status key    : ",  st2 ,  "key $ = correct position, x = used somewhere else, # = not in wordle")
       self.winner = self.test_for_winner( st2 )

   def test_for_winner( self, status ):
       if status == "$$$$$":
          return True
       else:
          return False
       
       
   def wordle_cmp( self, guess ):
       if len( guess ) != 5:
          print("Invalid guess" )
       guess_ltr = list( guess )
       wordle_ltr = list( self.wordle_word )
       status = []
       pos = 0 
       while guess_ltr:
             letter = guess_ltr.pop(0)
             #print("letter: ", letter )
             idx2  = self.wordle_word.find(letter) 
             idx = self.wordle_word.find(letter,pos)
             #backtrack to see if letter comes earlier.
             if idx2 > -1 and idx == -1: 
                #print("idx2: ", idx2 ) 
                #print("idx: ", idx )
                idx = idx2 
             # debug prints
             # print ( "Index : ", idx, "Pos: ",pos )
             # print ( self.letter_status( letter, pos, idx ))
             status.append(self.letter_status( letter, pos, idx ))   
             pos=pos+1 
       #print(status)
       return status
       
