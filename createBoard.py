import random as r

board = [[1,2,3,4,5,6,7,8,9] for i in range(9)]

def createBoard():
	board2 = board[:]
	for i in range(9):
		r.shuffle(board[i])

def verifColonne():
	isok = False
	for colonne in range(9):
		numbers = []
		for ligne in board:
			if ligne[colonne] in numbers:
				numbers.append(ligne[colonne])
		if not uniqueNumbers(numbers):
			return False
		else:
			isok = True
	return isok
"""
def verifLigne():
	for ligne in board:
		if not uniqueNumbers(ligne):
			return False
	return True
"""	
	
def verifDiagonale():
	numbers = []
	numbers2 = []
	for i in range(9):
		numbers.append(board[i][i])
		numbers.append(board[-i][-i])
	return uniqueNumbers(numbers) and uniqueNumbers(numbers2)
		

def uniqueNumbers(numbers):
	return numbers.sort() == [1,2,3,4,5,6,7,8,9]

def printBoard():
	for i in range(9):
		print(board[i])

createBoard()
printBoard()