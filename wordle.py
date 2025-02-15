
from wordle_a import wordle

class wordle_app:

  def __init__( self, wordle_file ):
       self.wordle_file = wordle_file
       self.wordle = wordle( wordle_file )
       self.wordle.wordle_reader()
       self.wordle.pick_wordle_word()
       #print("pick: ", self.wordle.wordle_word )
       self.guess_list = [] 

  def process_command(self, cmd ):
      if cmd == "/exit":
        quit() 
      if cmd == "/hint":
        print( " hint: ", self.wordle.wordle_word )


  def print_loop( self , count):
       lpe = True
       while lpe == True:
          prompt = str(count+1) + "  Guess: "
          guess = input(prompt )
          if len(guess) != 5:
             lpe = True
             print("Need 5 letters....")
             continue 
          if guess[0] == '/':
             self.process_command( guess )
             lpe = True
          else:   
             st = self.wordle.wordle_cmp(guess)
             self.guess_list.append(st)
             lpe = False

  
  def print_status( self ):

       for i in self.guess_list:
           print(" " )
           self.wordle.print_status(i)
           print(" " )
           if self.wordle.winner == True:
              print("***************************")
              print("you have guess the wordle  ")
              print("***************************")
              quit()

        
 
  def run( self ):

       for i in range(5):
           self.print_loop(i)
           self.print_status()

       if self.wordle.winner == False:

           print(" Wordle was:  ", self.wordle.wordle_word )

if __name__ == "__main__" :

   #  main()

   #app = wordle_app("wordle.words.sorted.txt" )
   app = wordle_app("common_words.txt" )
   app.run()
