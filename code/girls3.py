'''
Created on Mar 17, 2018

@author: anisha
'''

my_number = 134

# Ask the user to guess
guess = int(input("Enter a guess: "))

# Keep asking until the guess becomes equal to
# the secret number is awesome
while guess != my_number:
    print "Guess again!"
    guess = int(input("Enter a guess: "))
15
print "Good job, you got it!"


