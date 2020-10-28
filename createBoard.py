import sys
from random import sample
sys.setrecursionlimit(2**31-1)

board = [[1,2,3,4,5,6,7,8,9] for i in range(9)]

def createBoard():
	"""for i in range(9):
		r.shuffle(board[i])
	if not (verifColonne() and verifDiagonale()):
		createBoard()"""
	base = 3
	side = base * base

	# pattern for a baseline valid solution
	def pattern(r, c):
		return (base * (r % base) + r // base + c) % side

	# randomize rows, columns and numbers (of valid base pattern)
	def shuffle(s):
		return sample(s, len(s))

	rBase = range(base)
	# rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
	rows = []
	for r in shuffle(rBase):
		for g in shuffle(rBase):
			rows.append(g * base + r)

	# cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
	cols = []
	for c in shuffle(rBase):
		for g in shuffle(rBase):
			cols.append(g * base + c)

	nums = shuffle(range(1, base * base + 1))

	# produce board using randomized baseline pattern
	# board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
	board = []
	for r in rows:
		temp = []
		for c in cols:
			temp.append(nums[pattern(r, c)])
		board.append(temp)

	for line in board:
		print(line)

def verifColonne():
	"""for colonne in range(9):
		numbers = []
		for ligne in range(9):
			numbers.append(board[ligne][colonne])
		if not uniqueNumbers(numbers):
			return False"""
	numbers = []
	for i in range(81):
		if i%9==0:
			numbers = []
		if len(numbers)<9:
			numbers.append(board[i%9][i//9])
		if len(numbers)==9 and not uniqueNumbers(numbers):
			return False
	return True
	
def verifDiagonale():
	numbers = []
	numbers2 = []
	for i in range(9):
		numbers.append(board[i][i])
		numbers2.append(board[-i][-i])
	return uniqueNumbers(numbers) and uniqueNumbers(numbers2)
		

def uniqueNumbers(numbers):
	return sorted(numbers) == [1,2,3,4,5,6,7,8,9]

def printBoard():
	for i in range(9):
		print(board[i])

createBoard()
#printBoard()
