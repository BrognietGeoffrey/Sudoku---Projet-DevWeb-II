from random import sample

board = []
base = 3
side = base * base

def createBoard():
	rBase = range(base)
	rows, cols = [], []
	for r in shuffle(rBase):
		for g in shuffle(rBase):
			rows.append(g * base + r)

	for c in shuffle(rBase):
		for g in shuffle(rBase):
			cols.append(g * base + c)

	nums = shuffle(range(1, base * base + 1))

	# produce board using randomized baseline pattern
	for r in rows:
		temp = []
		for c in cols:
			temp.append(nums[pattern(r, c)])
		board.append(temp)

def pattern(r, c):
	# pattern for a baseline valid solution
	return (base * (r % base) + r // base + c) % side

def shuffle(s):
	# randomize rows, columns and numbers (of valid base pattern)
	return sample(s, len(s))

def printBoard():
	print(" =" * (side*2+2))
	for i in range(side):
		print("||", end="")
		for j,x in enumerate(board[i]):
			if j%3==0 and j!=0:
				print("|",end="")
			print(" {} |".format(x), end="")
		print("|")

		if (i+1)%3==0:
			print(" =" * (side*2+2))

createBoard()
printBoard()
