from tkinter import *	
	
class Move():
	"""Stores the position of a move"""
	
	def __init__(self, r = None, c = None, letter = None):
		self.r = r
		self.c = c
		self.letter = letter
	
	
class Game():
	"""Isolation Game Logic"""
	
	def __init__(self):
		# 2D list for game grid
		self.grid = []
		self.x_move = Move()
		self.o_move = Move()
		self.last_x_move = Move()
		self.last_o_move = Move()
		# Initialize the logical grid
		for r in range(0,6):
			self.grid.append([])
			for c in range(0,8):
				# grid[r].append(str(r) + ", " + str(c))
				self.grid[r].append("")
					
	def make_move(self, move):
		"""Check for a valid move"""
		if self.grid[move.r][move.c] != "":
			print("Not a valid move")
		else:
			self.grid[move.r][move.c] = move.letter

			
class GameUI():
	"""Draws and manages the game grid"""
	
	def __init__(self, game):
		self.root = Tk()
		self.root.title("Isolation Game")
		self.game = game
		self.draw_grid()
		self.o_move = Move(-1, -1)
		mainloop()
	
	def draw_grid(self):
		"""Create a UI using Entry widgets"""
		for r in range(0,6):
			for c in range(0,8):
				e = Entry(self.root, width=4)
				e.insert(0,game.grid[r][c])
				def handler(event, row = r, col = c):
					self.entry_callback(event, row, col)
				e.bind("<FocusOut>", handler)
				e.grid(row=r, column=c)
		
	def entry_callback(self, event, row, col):
		letter = event.widget.get().upper()
		print("cb " + letter + ", " + str(row) + ", " + str(col))
		if letter == 'X':
			x_move = Move(row, col, letter)
			game.make_move(x_move)
		elif letter == "O":
			o_move = Move(row, col, letter)
			game.make_move(o_move)
		else:
			print("Please enter an X or an O")
			event.widget.delete(0,END)

#### Program starts here ####

game = Game()
ui = GameUI(game)


	
	

