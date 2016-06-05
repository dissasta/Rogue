from random import randint
class Monster(object):
	def __init__(self, name, x, y, attack, defence, hp, inv):
		self.name = name
		self.icon = '@'
		self.x = x
		self.y = y
		self.attack = attack
		self.defence = defence
		self.hp = hp
		self.inv = inv

class Enemy(Monster):
	def hit(self, player):
		dmg = self.attack.split('d')
		dmg = randint(int(dmg[0]), int(dmg[0]) * int(dmg[1]))
		if dmg > player.defence:
			dmg_taken = dmg - player.defence
			print "The %s attacks you and rolls %s dealing %d damage. You manage to reflect %s." % (self.name, self.attack, dmg, player.defence)
			print "You take %d points of damage!" % (dmg - player.defence)
			player.hp -= dmg_taken
		else:
			print "The %s attacks you and rolls %s dealing %d damage. You manage to reflect the hit!" % (self.name, self.attack, dmg)

	def calc_def(self):
		total_def = 0
		if self.inv:
			gear = [self.inv.head, self.inv.torso, self.inv.legs, self.inv.hands, self.inv.shield]
			for i in gear:
				if i:
					total_def += i
			self.defence = total_def