import sys

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
winning_patterns = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), \
	((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)), \
	((0,0), (1,1), (2,2)), ((2,0), (1,1), (0,2)))
values = ("0", "X")
first_turn = True
finishedGame = False

def print_board():
	print('[', board[0][0], '|', board[0][1], '|', board[0][2], ']')
	print('[', board[1][0], '|', board[1][1], '|', board[1][2], ']')
	print('[', board[2][0], '|', board[2][1], '|', board[2][2], ']')

def set_board():
	global first_turn
	positions = input(values[int(first_turn)] + "'s turn. [x,y]:")

	if (len(positions) == 0):
		sys.exit()

	pos_x, pos_y = positions[0], positions[2]
	return mark(int(pos_x), int(pos_y), values[int(first_turn)])
		

def mark(pos_x, pos_y, value):
	if (board[pos_y][pos_x] != ' '):
		print("Already taken")
		return False

	try:
		board[pos_y][pos_x] = value
		return True
	except IndexError:
		print("Index out of range")

	return False

def evaluate_board():
	global finishedGame
	for pattern in winning_patterns:
		if (board[pattern[0][0]][pattern[0][1]] != ' ' and board[pattern[0][0]][pattern[0][1]] == board[pattern[1][0]][pattern[1][1]] and board[pattern[0][0]][pattern[0][1]] == board[pattern[2][0]][pattern[2][1]]):
			print_board()
			print("==== ", values[int(first_turn)], " is the Winner!")
			finishedGame = True


while (not finishedGame):
	print_board()
	changeTurn = set_board()
	evaluate_board()

	if (changeTurn):
		first_turn = not first_turn
	
