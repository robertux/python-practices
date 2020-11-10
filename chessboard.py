

PAWN   = ('♙', '♟', 1)
KNIGHT = ('♘', '♞', 3)
BISHOP = ('♙', '♝', 3)
ROOK   = ('♖', '♜', 5)
QUEEN  = ('♕', '♛', 10)
KING   = ('♔', '♚', 9999)
EMPTY  = ('_', '_', 0)

PLAYERS = {'WHITE': 0, 'BLACK': 1}
current_player = PLAYERS['WHITE']

def is_piece(board, position, piece):
	if (isinstance(piece, tuple) and len(piece) == 3):
		return board[position[0]][position[1]] in [piece[0], piece[1]]

	return False

def is_pawn(board, position):
	return is_piece(board, position, PAWN)

def is_knight(board, position):
	return is_piece(board, position, KNIGHT)

def is_bishop(board, position):
	return is_piece(board, position, BISHOP)

def is_rook(board, position):
	return is_piece(board, position, ROOK)

def is_queen(board, position):
	return is_piece(board, position, QUEEN)

def is_king(board, position):
	return is_piece(board, position, KING)

def is_empty(board, position):
	return is_piece(board, position, EMPTY)

def create_board():
	board = [[ROOK[1], KNIGHT[1], BISHOP[1], QUEEN[1], KING[1], BISHOP[1], KNIGHT[1], ROOK[1]],
		[PAWN[1], PAWN[1], PAWN[1], PAWN[1], PAWN[1], PAWN[1], PAWN[1], PAWN[1]],
		[EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0]],
		[EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0]],
		[EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0]],
		[EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0], EMPTY[0]],
		[PAWN[0], PAWN[0], PAWN[0], PAWN[0], PAWN[0], PAWN[0], PAWN[0], PAWN[0]],
		[ROOK[0], KNIGHT[0], BISHOP[0], QUEEN[0], KING[0], BISHOP[0], KNIGHT[0], ROOK[0]]]

	return board

def print_board(board):
	for i in range(8):
		print("[", end="")
		print(board[i][0],board[i][1],board[i][2],board[i][3],board[i][4],board[i][5],board[i][6],board[i][7], end="", sep=" ")
		print(" ]")

def is_in_range(board, position):
	return position[0] in range(len(board)) and position[1] in range(len(board))

def can_move_to(board, current_position, next_position):
	in_range = is_in_range(next_position)
	if is_piece(board[current_position[0]][current_position[1]], PAWN):
		if (current_player == PLAYERS['WHITE']):
			return in_range and not is_empty(current_position) and is_empty(next_position) and current_position[0] == next_position[0] and next_position[1] == current_position[1] + 1
		else:
			return in_range and not is_empty(current_position) and is_empty(next_position) and current_position[0] == next_position[0] and next_position[1] == current_position[1] - 1

	return False

def move(board, current_position, next_position):
	board[next_position[0]][next_position[1]] = board[current_position[0]][current_position[1]]
	board[current_position[0]][current_position[1]] = EMPTY[0]

board = create_board()
move(board, [1,0], [2,0])
print_board(board)
