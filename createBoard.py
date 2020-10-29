from random import sample

board = []
carre = 3
taille = carre**2
compteur_taille_carre = range(carre)


def create_board():
	rows, cols = [], []
	for r in shuffle(compteur_taille_carre):
		for g in shuffle(compteur_taille_carre):
			rows.append(g * carre + r)

	for c in shuffle(compteur_taille_carre):
		for g in shuffle(compteur_taille_carre):
			cols.append(g * carre + c)

	nums = shuffle(range(1, taille + 1))

	# produce board using randomized carreline pattern
	for r in rows:
		temp = []
		for c in cols:
			temp.append(nums[pattern(r, c)])
		board.append(temp)


def pattern(r, c):
	# pattern for a carreline valid solution
	return (carre * (r % carre) + r // carre + c) % taille


def shuffle(s):
	# randomize rows, columns and numbers (of valid carre pattern)
	return sample(s, len(s))


def print_board():
	for i in range(taille):
		if i % 3 == 0 or i==0:
			print(" =" * (taille * 2 + 2))
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
