
from wordle_a import wordle

class wordle_app:

  def __init__( self, wordle_file ):
       self.wordle_file = wordle_file
       self.wordle = wordle( wordle_file )
       self.wordle.wordle_reader()
       self.wordle.pick_wordle_word()
       print("pick: ", self.wordle.wordle_word )
       self.guess_list = [] 

  def print_loop( self ):

       guess = input("Guess: " )
       st = self.wordle.wordle_cmp(guess)
       self.guess_list.append(st)
  
  def print_status( self ):

       for i in self.guess_list:
           print(" " )
           self.wordle.print_status(i)
           print(" " )
 
  def run( self ):

       for i in range(5):
           self.print_loop()
           self.print_status()
  
def main():
   
   guess_list = []
 

   def status_loop():

      for i in guess_list:
        print(" ")
        w.print_status(i)
        print(" ")

   def print_loop():

          guess = input("Guess: ")

          print(w.is_wordle_word(guess))

          st = w.wordle_cmp( guess )

          guess_list.append(st)
          
          status_loop() 

   w = wordle("wordle.words.sorted.txt")

   w.wordle_reader()

   w.print_wordle_list(10)

   print(w.pick_wordle_word())

   for i in range(5):
       print_loop()

if __name__ == "__main__" :

   #  main()

   app = wordle_app("wordle.words.sorted.txt" )
   app.run()
