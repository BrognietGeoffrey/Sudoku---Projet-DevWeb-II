from random import sample, randint
from os import system
import copy, platform, time, datetime

class Sudoku:
	def __init__(self):
		self.board, self.player_board = [], []
		self.taille_carre = 3
		self.taille = self.taille_carre**2
		self.compteur_taille_carre = range(self.taille_carre)
		self.difficulty = 0
		self.msg_difficulty = "Veuillez sélectionner une difficultée: 1 pour facile, 2 pour moyen et 3 pour difficile: "
		self.msg_erreur_chiffre = "Veuillez insérer un chiffre entre 1 et {}".format(self.taille)
		self.msg_error_difficulty = "Veuillez insérer un chiffre entre 1 et 3"
		self.temps = 0

	def create_board(self):
		""" Création du board """
		lignes, colonnes = [], []
		tableau = self.shuffle(range(1, self.taille + 1))
		# Création d'une ligne et une colonne avec des valeurs random
		for i in self.shuffle(self.compteur_taille_carre):
			for j in self.shuffle(self.compteur_taille_carre):
				lignes.append(j * self.taille_carre + i)

		for i in self.shuffle(self.compteur_taille_carre):
			for j in self.shuffle(self.compteur_taille_carre):
				colonnes.append(j * self.taille_carre + i)

		# Création du sudoku en vérifiant la possibilité avec pattern(x,y)
		for i in lignes:
			temp = []
			for j in colonnes:
				temp.append(tableau[self.pattern(i, j)])
			self.board.append(temp)
		return self.board

	def pattern(self, ligne, colonne):
		"""
		Algorithme qui renvoie un nombre valide pour le board selon un paterne
		prédéfini pour le sudoku
		"""
		return (self.taille_carre * (ligne % self.taille_carre) + ligne // self.taille_carre + colonne) % self.taille

	def shuffle(self,tableau):
		""" Mélange les lignes et les colonnes """
		return sample(tableau, len(tableau))

	def print_board(self):
		""" Imprime le board en console de manière la plus lisible possible """

		for i in range(1,self.taille+1):
			if i==1:
				print("    ",end="")
			print(i, end="   " if i%3!=0 else "\n" if i==self.taille else "    ")

		for i in range(self.taille):
			if i%3==0 or i==0:
				print(" ="*(self.taille*2+3))
			print("{} ||".format(i+1), end="")
			for j,x in enumerate(self.player_board[i]):
				if j%3==0 and j!=0:
					print("|",end="")
				print(" {} |".format(x if x!=0 else " "), end="")
			print("|")
			if i==self.taille-1:
				print(" ="*(self.taille*2+3))

	def create_player_board(self):
		for i in range(self.taille-1):
			for j in range(self.taille-1):
				if randint(0,10) < self.difficulty:
					self.player_board[i][j] = 0
	def win(self):
		for i in range(self.taille):
			for j in range(self.taille):
				if self.player_board[i][j] == 0:
					return False
		return True

	def verif_number(self,x):
		return int("") if x<1 or x>self.taille else x

	def compare_board(self,x,y,number):
		return number == self.board[x-1][y-1]

	def game(self):
		while self.difficulty < 1 or self.difficulty > 4:
			try:
				self.difficulty = int(input(self.msg_difficulty))
			except:
				print(self.msg_error_difficulty)
		self.player_board = copy.deepcopy(self.create_board())
		self.create_player_board()
		start = time.time()
		while True:
			system("{}".format("cls" if platform.system()=="Windows" else "clear"))
			self.print_board()
			try:
				x = self.verif_number(int(input("Ligne:")))
				y = self.verif_number(int(input("Colonne:")))
				number = self.verif_number(int(input("Chiffre:")))
				if not self.compare_board(x,y,number):
					print("C'est faux!")
				else:
					self.player_board[x-1][y-1] = number
			except:
				print(self.msg_erreur_chiffre)
			if self.win():
				self.temps = str(datetime.timedelta(seconds=time.time()-start)).split(".")[0]
				break
		print("Partie terminée! Temps: {} ".format(self.temps))

a=Sudoku()
a.game()