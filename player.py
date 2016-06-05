from random import randint
from inventory import *
from level import *
import time

weapons = {'Small Dagger': ['1d5', 250, 100], 'Hands': ['1d3', 0, 0], 'Great Sword': ['2d6', 500, 100]}
shields = {'Small Shield': 3, 'Great Shield': 10}

class Character(object):
	def __init__(self, name, attack, defence, hp, inv):
		self.name = name
		self.icon = '@'
		self.x = None
		self.y = None
		self.attack = attack
		self.defence = defence
		self.hp = hp
		self.inv = inv

	def get_xy(self):
		for i in self.current_level.map:
			if '@' in i:
				self.x = i.index('@')
				self.y = self.current_level.map.index(i)

	def action(self, input):
		if input == 'a':
			if self.current_level.map[self.y][self.x - 1] == '.':
				self.current_level.map[self.y][self.x - 1] = '@'
				self.current_level.map[self.y][self.x] = '.'
			else:
				print 'bump'
				time.sleep(1)

		elif input == 's':
			if self.current_level.map[self.y + 1][self.x] == '.':
				self.current_level.map[self.y + 1][self.x] = '@'
				self.current_level.map[self.y][self.x] = '.'
			elif self.current_level.map[self.y + 1][self.x] == 'D':
				return 'D'
			else:
				print 'bump'
				time.sleep(1)

		elif input == 'd':
			if self.current_level.map[self.y][self.x + 1] == '.':
				self.current_level.map[self.y][self.x + 1] = '@'
				self.current_level.map[self.y][self.x] = '.'
			else:
				print 'bump'
				time.sleep(1)

		elif input == 'w':
			if self.current_level.map[self.y - 1][self.x] == '.':
				self.current_level.map[self.y - 1][self.x] = '@'
				self.current_level.map[self.y][self.x] = '.'
			else:
				print 'bump'
				time.sleep(1)

		self.get_xy()

	def hit(self, enemy):
		dmg = self.attack.split('d')
		dmg = randint(int(dmg[0]), int(dmg[0]) * int(dmg[1]))
		dmg_taken = dmg - enemy.defence
		if dmg > enemy.defence:
			if enemy.defence != 0:
				print "You attack %s and roll %s dealing %d damage. Monster reflects %s." % (enemy.name, self.attack, dmg, enemy.defence)
			else:
				print "You attack %s and roll %s dealing %d damage." % (enemy.name, self.attack, dmg)

			print "Enemy takes %d points of damage!" % (dmg - enemy.defence)
			enemy.hp -= dmg_taken

		else:
			print "You attack the %s and roll %s for %d damage but this fails to hurt the monster!" % (enemy.name, self.attack, dmg)

	def calc_def(self):
		total_def = 0
		if self.inv:
			gear = [self.inv.head, self.inv.torso, self.inv.legs, self.inv.hands, self.inv.shield]
			for i in gear:
				if i:
					total_def += i
			self.defence = total_def

class Player(Character):
	def __init__(self, name = None, attack = '1d3', defence = 0, hp = 100, inv = Inventory(weapon = weapons['Hands'], shield = shields['Small Shield'])):
		super(Player, self).__init__(name, attack, defence, hp, inv)

