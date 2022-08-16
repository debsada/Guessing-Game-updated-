import random
from art import logo

print(logo)

random_num = random.randint(1,100)
print(random_num)
print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
level = input("Easy or Difficult level: ")
if level == "easy":
  tries = 10
else:
  tries = 3

def play_game(tries_1, random_num_1):
  while tries_1 > 0: #While the user still has game lives, continue the game
    guess = int(input("guess a number between 1 and 100: "))
    if guess == random_num_1:
      return(print("Well done, you got it! Winner!")) #this breaks out of the loop and function, as user has won
    elif guess > random_num_1: #checks to see if user's guess is too high
      tries_1 -= 1 #removes a life each time the user gets it wrong
      print("Too high.")
      print(f"You have {tries_1} tries left")
    else: #only other possible option is if the user guesses a number that is too low
      tries_1 -= 1 #removes a life each time the user gets it wrong
      print("Too low.")
      print(f"You have {tries_1} tries left")

  return(print("You have run out of lives. Sorry, you lose!")) #when tries becomes 0, loop finishes which means user has lost

play_game(tries,random_num)
