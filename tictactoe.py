import sys
def make_board():
	for i in range(0,3):
		for j in range(0, 3):
			print board[2-i][j],
			if j != 2:
				print "|",
		print ""
		

def no_winning():
	move_check = False
	for i in range(0,3):
		if board[i][0] == board[i][1] == 'O' and board[i][2] != 'X':
			board[i][2] = 'O'
			print "\n"
			make_board()
			print "\nFatality!"
			sys.exit()
			break
		elif board[i][0] == board[i][2] == 'O' and board[i][1] != 'X':
			board [i][1] = 'O'
			print "\n"
			make_board()
			print "\nBrutality!"
			sys.exit()
			break
		elif board[i][1] == board[i][2] == 'O' and board[i][0] != 'X':
			board[i][0] = 'O'
			print "\n"
			make_board()
			print "\nAnimality!"
			sys.exit()
			break
		elif board[0][i] == board[1][i] == 'O' and board[2][i] != 'X':
			board[2][i] = 'O'
			print "\n"
			make_board()
			print "\nBabality!"
			sys.exit()
			break
		elif board[0][i] == board[2][i] == 'O' and board[1][i] != 'X':
			board[1][i] = 'O'
			print "\n"
			make_board()
			print "\nC-c-combo Breaker!"
			break
		elif board[1][i] == board[2][i] == 'O' and board [0][i] != 'X':
			board[0][i] = 'O'
			print "\n"
			make_board()
			print "\nUltra Ultra Ultra!"
			sys.exit()
			break
		elif board[i][0] == board[i][1] == 'X' and board[i][2] != 'O':
			board[i][2] = 'O'
			move_check = True
			break
		elif board[i][0] == board[i][2] == 'X' and board[i][1] != 'O':
			board [i][1] = 'O'
			move_check = True
			break
		elif board[i][1] == board[i][2] == 'X' and board[i][0] != 'O':
			board[i][0] = 'O'
			move_check = True
			break
		elif board[0][i] == board[1][i] == 'X' and board[2][i] != 'O':
			board[2][i] = 'O'
			move_check = True
			break
		elif board[0][i] == board[2][i] == 'X' and board[1][i] != 'O':
			board[1][i] = 'O'
			move_check = True
			break
		elif board[1][i] == board[2][i] == 'X' and board [0][i] != 'O':
			board[0][i] = 'O'
			move_check = True
			break
	
	if move_check == False:
		if board[1][1] == " ":
			board[1][1] = 'O'
		elif board[0][0] == " ":
			board[0][0] = 'O'
		elif board[0][2] == " ":
			board[0][2] = 'O'
		elif board[2][0] == " ":
			board[2][0] = 'O'
		elif board[2][2] == " ":
			board[2][2] = 'O'
		elif board[0][1] == " ":
			board[0][1] = 'O'
		elif board[1][0] == " ":
			board[1][0] = 'O'
		elif board[1][2] == " ":
			board[1][2] = 'O'
		elif board[2][1] == " ":
			board[2][1] = 'O'
		
	
	
	if " " not in board[0] and " " not in board[1] and " " not in board[2]:
		print "\nDraw! Can't win!"
		return True
	else:
		return False

board = [	[" "," "," "],
			[" "," "," "],
			[" "," "," "]]
		
done = False

while done != True:
	make_board()
	
	next_move = False
	while next_move != True:
		print "\nSelect your next move:"
		print "7|8|9"
		print "4|5|6"
		print "1|2|3"
		
		position = input("\nSelect: ")
		if position <= 9 and position >= 1:
			y = position/3
			x = position%3
			if x != 0:
				x -= 1
			else:
				x = 2
				y -= 1
	 
			if board[y][x] == " ":
				board[y][x] = "X"
				next_move = True
				done = no_winning()
				if done == True:
					next_move = False
					sys.exit()