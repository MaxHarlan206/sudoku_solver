import time
board = [
			[0,0,0,3,0,0,0,0,2],
			[0,0,0,0,0,4,0,7,8],
			[4,0,0,0,2,0,9,3,0],
			[5,0,4,0,0,7,6,0,0],
			[0,8,0,4,0,6,0,1,0],
			[0,0,2,8,0,0,7,0,9],
			[0,4,3,0,6,0,0,0,7],
			[9,7,0,5,0,0,0,0,0],
			[1,0,0,0,0,8,0,0,0],
]

def solve(board):
	""" Uses recursion and backtracking to find the final board position"""
	# THE RECURSIVE CASE:
	if find_empty(board) != None:
		x, y = find_empty(board)
		for n in range(1, 10):
			if is_valid(board, x, y, n):
				print_board(board)
				time.sleep(.005)
				board[x][y] = n
				solve(board)
				board[x][y] = 0
		return
	# The base case is if no more empty cells, then return the board
	else:
		print_board(board)
		input("Would you like to see another solution?")

def find_empty(board):
	""" Iterates over the board left to right, row by row, until an empty cell is found and then returns its coordinates"""
	first_square = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				first_square = [i,j]
				return first_square
	else:
		return None

def is_valid(board, row, col, number):
	""" Checks if a value can be placed at the given position in a board. Returns bool."""
	# If there is another  of the same number in the row return false
	for i in range(len(board[row])):
		if board[row][i] == number:
			return False
	# If there is another  of the same number in the column return false
	for j in range(len(board)):
		if board[j][col] == number:
			return False
	# If there is another  of the same number in the box return false
	for i in range(2):
		for j in range(2):
			if board[i + ((row // 3) * 3)][j + ((col // 3) * 3)] == number:
				return False
	else:
		return True 
	return

def print_board(solution):
	""" Prints a nicely formatted sudoku board"""
	for i in range(9):
		if (i) % 3 == 0:
			print("------------------------")
		rowstr = "|"
		for j in range(9):
			if (j+1) % 3 == 0:
				rowstr += str(board[i][j]) + " | "
			else: 
				rowstr += str(board[i][j]) + " "
		print(rowstr)
	print("------------------------\n")

solve(board)