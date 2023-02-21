import random
import art

print(art.logo)
print("I'm Thinking of a number between 1 to 100")
level = input("Which level you want to play? easy / hard: ").lower()

global actual_number
actual_number = random.randint(1,100)
print(actual_number)

def decide(user_input):
  if user_input > actual_number:
    print("Too high")
    return 0
  if user_input < actual_number:
    print("Too low")
    return 0
  if user_input == actual_number:
    return 1

def guess():
  user_guess = input("Guess my number: ")
  if int(user_guess) > 100 or int(user_guess) < 1 or user_guess.isnumeric() == False:
    print("Entry Invalid ---- Please enter a number between 1 to 100")
    guess()
  if user_guess.isnumeric() == True:
    return int(user_guess)

count = 0
if level == "hard":
  print(f"you have {5 - count} chances to guess")
  while count < 5:
    decision = decide(guess())
    if decision == 0:
      count += 1
      print(f"you have {5 - count} chances to guess")
    if decision == 1:
      print("That's right! You won")
      break
  if count == 5 and decision == 0:
    print("You Lose")
if level == "easy":
  print(f"you have {10 - count} chances to guess")
  while count  < 10:
    decision = decide(guess())
    if decision == 0:
      count += 1
      print(f"you have {10 - count} chances to guess")
    if decision == 1:
      print("That's right! You won")
      break
  if count == 10 and decision == 0:
    print("You Lose")