import random
import sys

name = input("enter your name? ")

while True:

	secret = random.randint(1, 20)
	
	for guesses in range(1, 8):
		guess = int(input("guess the number? 1..20 "))
		
		if guess == secret:
			break
		elif (guess + 5) <= secret:
			print("you guessed too low!")
		elif (guess - 5) > secret:
			print("you guessed too high!")
		elif guess < secret:
			print("you guessed low!")
		elif guess > secret:
			print("you guessed high!")
			
	if guess == secret:
		print(f"bhesh {name}! you guessed it in {guesses} tries.")
    else:
	    print("better luck next time {name}! you couldn't guess the number in 7 chances.")
	
	again = input("do you want to play again? Yes/No. ")
	if again.lower() == "no":
		sys.exit(0)