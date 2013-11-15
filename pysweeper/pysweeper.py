"""
A basic Minesweeper clone written in Python.
This works as a demo for Tkinter, a Python GUI framework.
"""

from Tkinter import *
import random

# ============ Config ============

fieldsize = 8
mines     = 8

# ============ Helper functions ============

def print_field(field):
  """ Print the game field """
  for row in field:
    print row

def surrounding_mines(minefield, x, y):
  """ Count the mines surrounding a field """
  # Nomenclature for position X
  # NW  N  NE
  # W   X  E
  # SW  S  SE
  NW = minefield[x-1][y-1] if x > 0 and y > 0 else 0
  N = minefield[x-1][y] if x > 0 else 0
  NE = minefield[x-1][y+1] if x > 0 and y < len(minefield)-1 else 0

  W = minefield[x][y-1] if y > 0 else 0
  E = minefield[x][y+1] if y < len(minefield)-1 else 0

  SW = minefield[x+1][y-1] if x < len(minefield)-1 and y > 0 else 0
  S = minefield[x+1][y] if x < len(minefield)-1 else 0
  SE = minefield[x+1][y+1] if x < len(minefield)-1 and y < len(minefield)-1 else 0
  return NW + N + NE + W + E + SW + S + SE


# ============ Setup ============

# The playing field has NxN fields
minefield = [[0]*fieldsize for x in xrange(fieldsize)]

# Place mines
for i in range(mines):
  x = random.randint(0,fieldsize-1)
  y = random.randint(0,fieldsize-1)
  minefield[x][y] = 1

# Count surrounding mines for each field:
field = [[0]*fieldsize for x in xrange(fieldsize)]
for x in range(fieldsize):
  for y in range(fieldsize):
    field[x][y] = surrounding_mines(minefield, x, y)

# print_field(minefield) # Show minefield
print_field(field)     # Show hints for mines

# ============ Game GUI ============

root = Tk()
root.grid()
field_img = PhotoImage(file="img/field.gif")
empty_img = PhotoImage(file="img/empty.gif")

# Put all gui elements into an array
grid_labels = [[None]*fieldsize for x in xrange(fieldsize)]
grid_text   = [[""]*fieldsize for x in xrange(fieldsize)]

"""
def reveal_field(field, x, y):
  if field[x][y] == 0:
"""

def click_field(event):
  grid_info = event.widget.grid_info()
  #print "row:", grid_info["row"], "column:", grid_info["column"]
  x = int(grid_info["column"])
  y = int(grid_info["row"])
  grid_labels[x][y]["image"] = empty_img

for i in range(fieldsize):
  for j in range(fieldsize):
    t = StringVar()
    t.set(" ")
    l = Label(root, textvariable=t, height="10", width="10", image=field_img,
        compound=CENTER)
    l.bind("<Button-1>", click_field)
    l.grid(column=i, row=j)
    grid_labels[i][j] = l
    grid_text[i][j] = t
root.resizable(False,False)
root.update()
root.geometry(root.geometry())
root.mainloop()
