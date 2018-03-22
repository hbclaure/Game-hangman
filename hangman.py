import random

word_list = []
word_list.append("hey")
word_list.append("and")


choose = random.choice(word_list)


tries_correct = []
tries_incorrect = []


message = print('Hello and welcome to hangman')

guess = print('guess the following word: ')

print('___ ___ ___')
count =0

if choose == 'hey':
	while count < 3:
		trial = input()
		if  trial in ['h','e','y']:
			print("nice")
			tries_correct.append(trial)
			count = count + 1
		else:
			print("try again")
			tries_incorrect.append(trial)



if choose == 'and':
	while count < 3:
		trial = input()
		if  trial in ['a','n','d']:
			print("nice")
			tries_correct.append(trial)
			count = count + 1
		else:
			print("try again")
			tries_incorrect.append(trial)

print("Congrats you won!")
print("Here are your attempts:   ")
print(tries_incorrect)


	








