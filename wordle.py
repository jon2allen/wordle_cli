
from wordle_a import wordle

class wordle_app:

  def __init__( self, wordle_file ):
       self.wordle_file = wordle_file
       self.wordle = wordle( wordle_file )
       self.wordle.wordle_reader()
       self.wordle.pick_wordle_word()
       print("pick: ", self.wordle.wordle_word )
       self.guess_list = [] 

  def print_loop( self , count):
       prompt = str(count+1) + "  Guess: "
       guess = input(prompt )
       st = self.wordle.wordle_cmp(guess)
       self.guess_list.append(st)
  
  def print_status( self ):

       for i in self.guess_list:
           print(" " )
           self.wordle.print_status(i)
           print(" " )
 
  def run( self ):

       for i in range(5):
           self.print_loop(i)
           self.print_status()



if __name__ == "__main__" :

   #  main()

   #app = wordle_app("wordle.words.sorted.txt" )
   app = wordle_app("common_words.txt" )
   app.run()
