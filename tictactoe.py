class Player:
	def __init__(self, name):
		self.name = name
		self.wins = 0
	def getName(self):
		return self.name
	def getWins(self):
		return self.wins
	def addWin(self):
		self.wins += 1


def printLine():
	print()
	print('---' * 5)
	print()


def makeMove(board, sign, player):
	'''sign is X or O'''

	while True:
		print()
		print(player.getName(), "to play as", sign)
		printBoard(board)
		position = input("Enter row column to play: ")
		print()

		try:
			move = position.split()
			row = int(move[0]) - 1
			column = int(move[1]) -  1
		except:
			print("Bad entry: Rows are 1, 2, 3 columns are 1, 2, 3")
			print("example: 1 2")
			continue
		if not row in range(3) or not column in range(3):
			print("Bad entry: Rows are 1, 2, 3 columns are 1, 2, 3")
			print("example: 1 2")
			continue
		if board[row][column] == ' ':
			board[row][column] = sign
			break
		else:
			print('Bad Move, space is already taken')
			print()
	print(player.getName(),'played', sign, 'on', position,)
	return board


def printBoard(board):

	counter = 1

	print()
	print('    1   2   3')
	for row in board:
		print(str(counter)+' ', end='')
		for column in row:
			print('|',column, end = ' ')
		print('|')
		counter += 1
	print()



def checkWin(board, sign):

	# Horizontal
	for row in board:
		if row[::] == [sign, sign, sign]:
			return True

	# Vertical 
	for i in range(3):
		if board[0][i] == board[1][i] == board[2][i] == sign:
			return True

	# Diagonal
	if board[0][0] == board[1][1] == board[2][2] == sign:
		return True
	if board[0][2] == board[1][1] == board[2][0] == sign:
		return True

	return False

def validateName(name):
	if 3 <= len(name) <= 16:
		return True
	else:
		return False


# Initiate the game

if __name__ == '__main__':

	print()
	print('TIC TAC TOE')
	printLine()
	print('Rows are 1, 2, 3 top down')
	print('Columns are 1, 2, 3 left to right')
	print('Enter the coordinate separated by a space like so: 1 3')
	print()
	input("Press enter to continue")
	print()

	while True:
		player1Name = input("Enter name for Player 1: ")
		if not validateName(player1Name):
			print('Must be between 3 and 16 characters')
		else: break
	print()
	while True:
		player2Name = input("Enter name for Player 2: ")
		if not validateName(player2Name):
			print('Must be between 3 and 16 characters')
		else: break


	signs = ['O','X']
	player1 = Player(player1Name)
	player2 = Player(player2Name)

	while True:

		turn = 1
		board = [

		[' ',' ',' '],
		[' ',' ',' '],
		[' ',' ',' '],

		]


		printLine()
		print()

		print(player1.getName(), 'is Player 1 as X')
		print(player2.getName(), 'is Player 2 as O')


		# Play a match
		while True:

			if turn % 2 == 0:
				sign = signs[0]
				player = player2

			else: 
				sign = signs[1]
				player = player1

			board = makeMove(board, sign, player)
			printBoard(board)

			if checkWin(board, sign):
				player.addWin()
				print(player.getName(), 'Wins!')
				break

			if turn == 9:
				print('This match is a draw')
				break

			printLine()
			turn += 1

		printLine()
		print('Score:')
		print('  ', player1.getName(), player1.getWins())
		print('  ', player2.getName(), player2.getWins())
		print()
		quit = input('Enter q to quit, or return to play again: ')
		if quit.upper() == 'Q':
			print('Exiting')
			break










