from random import sample

board = []
taille_carre = 3
taille = taille_carre**2
compteur_taille_carre = range(taille_carre)

def create_board():
	lignes, colonnes = [], []
	for i in shuffle(compteur_taille_carre):
		for j in shuffle(compteur_taille_carre):
			colonnes.append(j * taille_carre + i)

	for i in shuffle(compteur_taille_carre):
		for j in shuffle(compteur_taille_carre):
			lignes.append(j * taille_carre + i)

	nums = shuffle(range(1, taille + 1))

	# produce board using randomized carreline pattern
	for i in lignes:
		temp = []
		for j in colonnes:
			temp.append(nums[pattern(i, j)])
		board.append(temp)

def pattern(ligne, colonne):
	# pattern for a carreline valid solution
	return (taille_carre * (ligne % taille_carre) + ligne // taille_carre + colonne) % taille

def shuffle(tableau):
	# Mélange les lignes et les colonnes
	return sample(tableau, len(tableau))

def print_board():
	for i in range(taille):
		if i%3==0 or i==0:
			print(" =" *(taille*2+2))
		print("||", end="")
		for j,x in enumerate(board[i]):
			if j%3==0 and j!=0:
				print("|",end="")
			print(" {} |".format(x), end="")
		print("|")
		if i==taille-1:
			print(" ="*(taille*2+2))

create_board()
print_board()
