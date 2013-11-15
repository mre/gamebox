#/usr/bin/env python

'''
 Implementation of the game "Dalli Click" in Python using the Py-Game library.
 The objective of the game is to guess an image that is covered by tiles that will
 gradually be removed until the whole image is visible.

 Copyright (c) 2010 Matthias Endler

 Dalli Click is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Import modules
import os, pygame, random
import argparse # Command-line arguments
from pygame.locals import *

# Configuration
screen_size = (1000, 600)	# Size of window
tiles_x, tiles_y = 8, 6		# Number of tiles horizontally and vertically
tile_color = (0,0,0) 		# Black tiles
fps = 40 					# Frames per second
mouse_visibility = True		# Show mouse on screen
resource_dir = ''			# Folder where pictures are in

# Functions to create our resources.
def load_image(name, colorkey=None):
	fullname = os.path.join(resource_dir, name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()

# Classes for our game objects
class Background(pygame.sprite.Sprite):
	"""The picture to guess"""
	def __init__(self, image_name):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image, self.rect = load_image(image_name)
		self.image = pygame.transform.scale(self.image, screen_size)


class Foreground():
	"""The background image is covered by tiles in the foreground."""
	def __init__(self):
		# The foreground manages all tiles that cover the image
		self.tiles = self.initTiles()

	def initTiles(self):
		"Creates a list of tiles."
		tiles = []
		for pos_x in range(tiles_x):
			 for pos_y in range(tiles_y):
				tiles.append(Tile(pos_x, pos_y))
		return tiles
		
	def update(self):
		"Show all remaining tiles on screen."
		for tile in self.tiles:
			tile.update()

	def removeTile(self):
		"Remove a random tile"
		if self.tiles:
			tile = random.choice(self.tiles)
			self.tiles.remove(tile)
			return tile.rectangle


class Tile():
	"""A tile is a part of the foreground that covers the background image."""

	def __init__(self, pos_x, pos_y):
		self.screen = pygame.display.get_surface()
		self.color = tile_color
		self.tile_width  = screen_size[0] / tiles_x
		self.tile_height = screen_size[1] / tiles_y
		self.rectangle = self.rectangleSize(pos_x, pos_y)

	def rectangleSize(self, pos_x, pos_y):
		"Calculate the rectangle where the tile will be drawn"
		start_x = pos_x*self.tile_width
		start_y = pos_y*self.tile_height
		return (start_x, start_y, self.tile_width, self.tile_height)
		
	def update(self):
		"Draw tile on the screen"
		pygame.draw.rect(self.screen, self.color, self.rectangle)

def main():
	"""This function is called when the program starts.
		it initializes everything it needs, then runs in
		a loop until the game ends."""
	
	# Read options from commandline
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--image')
	args = parser.parse_args()
	
	if not args.image:
		args.image = 'background.jpg'
            
	#Initialize Everything
	pygame.init()
	pygame.display.set_caption('Dalli Click')
	pygame.mouse.set_visible(mouse_visibility)

	#Paint the background surface black
	screen = pygame.display.set_mode(screen_size)
	surface = pygame.Surface(screen.get_size())
	surface = surface.convert()
	surface.fill(tile_color)
 
#Prepare Game Objects
	clock = pygame.time.Clock()
	background_image = Background(args.image)
	foreground = Foreground()
	background = pygame.sprite.RenderPlain(background_image)

#Main Loop
	while 1:
		clock.tick(fps)

		#Handle Input Events
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type is MOUSEBUTTONUP:
				removed_area = foreground.removeTile()
				print(removed_area)

		#Draw Everything
		screen.blit(surface, (0, 0))
		background.draw(screen)
		foreground.update()
		pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()

