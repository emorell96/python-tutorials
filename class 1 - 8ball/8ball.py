# first excercise:

# create a program that will loop forever unless the user writes 'exit' and asks the user for a question on every iteration.
# it will print the question back to the user.

# after the question, the program has to give you a number from 1 to 10 randomly.

# instead of giving a number give a random text from the ones in the wikipedia https://en.wikipedia.org/wiki/Magic_8_Ball#Possible_answers

import random as random
question = ""
answer = ""
seq = ["It is certain.", "As I see it, yes.", "Reply hazy, try again.", "Don't count on it."]

while question != 'exit' :
    question = input("Ask me a question.")
    if question != 'exit':
        answer = random.choice(seq)
        print(question)
        print(answer)
