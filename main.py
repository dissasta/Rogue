from player import *
from monster import *
from level import *
import platform
import os
import time

def cls():
	if platform.system() == 'Linux':
		os.system('clear')
	elif platform.system() == 'Windows':
		os.system('cls')

def getch():
	if platform.system() == 'Linux':
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		tty.setraw(sys.stdin.fileno())

		ch = sys.stdin.read(1)

		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

	elif platform.system() == 'Windows':
		return msvcrt.getch()

def print_game():
	cls()
	for i in p.current_level.map:
		print "".join(i)

def level_down(level):
	level += 1
	if len(levels_list[level]) != 2:
		Level()
		p.current_level = levels_list[level][1]
		p.current_level.gen_map()
	else:
		p.current_level = levels_list[level][1]

if __name__ == '__main__':
	if platform.system() == "Windows":
		import msvcrt
	elif platform.system() == "Linux":
		import sys, tty, termios

	level = 1
	p = Player()
	Level()
	p.current_level = levels_list[level][1]
	p.current_level.gen_map()
	p.get_xy()

	while p:
		print_game()
		input = getch()
		if input:
			action = p.action(input)
			if action == "D":
				level_down(level)


		#p = False


#	p.attack = p.inv.weapon[0]
#	p.calc_def()

	#p.name = raw_input("What is your character's name? ")
#	enemies = [Enemy('Rat', 10, 20, '1d6', 0, 4, inv = Inventory())]
#	enemies[0].calc_def()
#	enemies[0].hit(p)
#	p.hit(enemies[0])
#	print enemies[0].hp
#	print p.inv
