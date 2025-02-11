
from wordle_a import wordle



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

   main()
