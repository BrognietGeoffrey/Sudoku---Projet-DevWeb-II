from random import sample, randint
from os import system
import copy, platform

board, player_board = [], []
taille_carre = 3
taille = taille_carre**2
compteur_taille_carre = range(taille_carre)
difficulty = 2
message_erreur = "Veuillez insérer un chiffre entre 1 et {}".format(taille)

def create_board():
	""" Création du board """
	lignes, colonnes = [], []
	tableau = shuffle(range(1, taille + 1))
	# Création d'une ligne et une colonne avec des valeurs random
	for i in shuffle(compteur_taille_carre):
		for j in shuffle(compteur_taille_carre):
			lignes.append(j * taille_carre + i)

	for i in shuffle(compteur_taille_carre):
		for j in shuffle(compteur_taille_carre):
			colonnes.append(j * taille_carre + i)

	# Création du sudoku en vérifiant la possibilité avec pattern(x,y)
	for i in lignes:
		temp = []
		for j in colonnes:
			temp.append(tableau[pattern(i, j)])
		board.append(temp)
	return board

def pattern(ligne, colonne):
	"""
	Algorithme qui renvoie un nombre valide pour le board selon un paterne
	prédéfini pour le sudoku
	"""
	return (taille_carre * (ligne % taille_carre) + ligne // taille_carre + colonne) % taille

def shuffle(tableau):
	""" Mélange les lignes et les colonnes """
	return sample(tableau, len(tableau))

def print_board():
	""" Imprime le board en console de manière la plus lisible possible """

	for i in range(1,taille+1):
		if i==1:
			print("    ",end="")
		print(i, end="   " if i%3!=0 else "\n" if i==taille else "    ")


	for i in range(taille):
		if i%3==0 or i==0:
			print(" ="*(taille*2+3))
		print("{} ||".format(i), end="")
		for j,x in enumerate(player_board[i]):
			if j%3==0 and j!=0:
				print("|",end="")
			print(" {} |".format(x if x!= 0  else " "), end="")
		print("|")
		if i==taille-1:
			print(" ="*(taille*2+3))

def create_player_board():
	for i in range(taille-1):
		for j in range(taille-1):
			if randint(1,10) < difficulty:
				player_board[i][j] = 0
def win():
	for i in range(taille):
		for j in range(taille):
			if player_board[i][j] == 0:
				return False
	return True

def verif_number(x):
	return int("") if x<1 or x>taille else x

def compare_board(x,y,number):
	return number == board[x-1][y-1]

def game():
	while True:
		system("{}".format("cls" if platform.system()=="Windows" else "clear"))
		print_board()
		try:
			x = verif_number(int(input("Ligne:")))
			y = verif_number(int(input("Colonne:")))
			number = verif_number(int(input("Chiffre:")))
			if not compare_board(x,y,number):
				print("C'est faux!")
			else:
				player_board[x-1][y-1] = number
		except:
			print(message_erreur)
		if win():
			break
	print("Partie terminée!")



player_board = copy.deepcopy(create_board())
create_player_board()
game()