import random as r

board = [[1,2,3,4,5,6,7,8,9] for i in range(9)]

def createBoard():
	for i in range(9):
		r.shuffle(board[i])
	if not (verifColonne() and verifDiagonale()):
		createBoard()

def verifColonne():
	for colonne in range(9):
		numbers = []
		for ligne in range(9):
			numbers.append(board[ligne][colonne])
		if not uniqueNumbers(numbers):
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
printBoard()
