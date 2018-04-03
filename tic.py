import random
import sys

sore_o = 0 
sore_x = 0
computer_score = 0
user_score = 0
def drawBoard(board):

	# This function prints out the board that it was passed.
	# "board" is a list of 10 strings representing the board (ignore index 0)

	print('   |   |')

	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

	print('   |   |')

	print('-----------')

	print('   |   |')

	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

	print('   |   |')

	print('-----------')

	print('   |   |')

	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

	print('   |   |')

def startgame():

	print('Do you want to be X or O?')
	#should change to while loop
	a  = 'False'
	while a  == 'False':
		letter =  raw_input().upper()
		if letter == 'X' or letter == 'O':
			print('You have choosen : '+str(letter))
			a  = 'True'
		else:
			print('Please enter a valid letter X or O')
			a = 'False'
	drawBoard([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

	return initialplay(letter)

def initialplay(letter):

	print('Do you want to make your first move Y or N')
	a  = 'False'
	while a  == 'False':
		first_move =  raw_input().upper()
		if first_move == 'Y' :
			#print(first_move)
			a  = 'True'
		elif first_move == 'N':
			#print(first_move)
			a  = 'True'
		else:
			print('Please enter a valid first move Y or N')
			a = 'False'

	return user_play(letter,first_move)

def user_play(letter, first_move):

	print(letter, first_move)
	if letter == 'X':
		manual_letter = 'O'
	elif letter == 'O':
		manual_letter = 'X'

	new_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	if first_move == 'Y':

		print('You have Opted to play the First Move.')
	elif first_move == 'N':

		print('Computer will play the First Move.')
		manual_input = random.randint(1,9)
		new_list[int(manual_input)] = letter
		drawBoard(new_list)

	a  = 'False'

	while a  == 'False':

		b = 'False'
		while b == 'False':
			
			board_value = raw_input('please enter a value between 1 to 9\n')

			try:
				if new_list [int(board_value)] == ' ':

					new_list[int(board_value)] = letter
					b = 'True'
				else:

					print('This Value is already taken by '+str(new_list[int(board_value)]))
					b = 'False'
			except IndexError:
				b = 'False'
				print('The value you have entered is invalid, please enter a value between 1 to 9')	
		
		checkdata(new_list, letter)
		b = 'False'

		while b == 'False':

			manual_input = random.randint(1,9)
			if new_list [int(manual_input)] == ' ':

				new_list[int(manual_input)] = manual_letter
				b = 'True'

		checkdata(new_list, letter)
		drawBoard(new_list)

def checkdata(new_list, letter):

	check_value = ''
	if new_list [1] == new_list [2] == new_list [3] :

		if  new_list [1] == new_list [2] == new_list [3] != ' ' :

			print('Player '+str(new_list[1])+' win the game')
			drawBoard(new_list)
			winner = new_list[1]
			check_value = 'True'  
		
	elif new_list [4] == new_list [5] == new_list [6] :

		if  new_list [4] == new_list [5] == new_list [6] != ' ' :
		
			print('Player '+str(new_list[5])+' win the game')
			drawBoard(new_list)
			winner = new_list[5]
			check_value = 'True'  

	elif new_list [7] == new_list [8] == new_list [9] :

		if new_list [7] == new_list [8] == new_list [9] != ' ' :

			print('Player '+str(new_list[7])+' win the game')
			drawBoard(new_list)
			winner = new_list[7]
			check_value = 'True'  

	elif new_list [1] == new_list [4] == new_list [7] :

		if new_list [1] == new_list [4] == new_list [7]  != ' ':

			print('Player '+str(new_list[4])+' win the game')
			drawBoard(new_list)
			winner = new_list[4]
			check_value = 'True'  

	elif new_list [2] == new_list [5] == new_list [8] :

		if new_list [2] == new_list [5] == new_list [8] != ' ':
		
			print('Player '+str(new_list[5])+' win the game')
			drawBoard(new_list)
			winner = new_list[5]
			check_value = 'True'  

	elif new_list [3] == new_list [6] == new_list [9] :

		if new_list [3] == new_list [6] == new_list [9] != ' ':

			print('Player '+str(new_list[6])+' win the game')
			drawBoard(new_list)
			winner = new_list[6]
			check_value = 'True'  

	elif new_list [1] == new_list [5] == new_list [9] :

		if new_list [1] == new_list [5] == new_list [9] != ' ':

			print('Player '+str(new_list[5])+' win the game')
			drawBoard(new_list)
			winner = new_list[5]
			check_value = 'True'  

	elif new_list [7] == new_list [5] == new_list [3] :

		if new_list [7] == new_list [5] == new_list [3] != ' ':

			print('Player '+str(new_list[5])+' win the game')
			drawBoard(new_list)
			winner = new_list[5]
			check_value = 'True'  

	myItem = ' '
	if myItem not in new_list:
		print('-------------------------------------------------')
		winner = 'D'
		check_value = 'True'

	global sore_o 
	global sore_x
	global computer_score
	global user_score
	if check_value == 'True'  :		

		if winner == 'X':

			sore_x += 1

		elif winner == 'O':

			sore_o += 1

		elif winner == 'D':

			sore_o += 0
			sore_x += 0
		
		if letter == winner:

			print('Player wins this Round')
			user_score += 1

		elif letter != winner:

			print('Computer wins this Round')
			computer_score += 1

		else:

			print('Its a Tie, try again.')

		print('\n')
		print('------------------SCORE CARD------------------')
		print('\n')
		print('Total Score for X : '+str(sore_x))
		print('\n')
		print( 'Total Score for O : '+str(sore_o))
		print('\n')
		print('Player score : '+str(user_score))
		print('\n')
		print('Computer score : '+str(computer_score))
		print('\n')

		if user_score == computer_score:
			print('The Game is in tie')
		elif user_score > computer_score:
			print('The User is Leading')
		elif user_score < computer_score:
			print('The Computer is Leading, watch out....')

		print('\n')
		print('------------------ ~ END ~ ------------------')
		print('Would you like to play the game once again Y or N.')
		user_choice = raw_input().upper()

		if user_choice == 'Y':
			print('Wait while we load the game')
			startgame()
		elif user_choice == 'N':
			print('Thank s for Playing')
			sys.exit()


if __name__ == '__main__':

	startgame()
