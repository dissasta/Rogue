from itertools import count

levels_list = {1: ['level1.txt'], 2: ['level2.txt']}

class Level(object):
    _ids = count(1)

    def __init__(self):
        self.id = self._ids.next()
        self.monsters = []
        self.chests = []
        self.map = []
        levels_list[self.id].append(self)

    def gen_map(self):

	map_file = open(levels_list[self.id][0], 'r')

	for line in map_file:
		row = []
		for ch in line:
			if ch != '\n':
				row.append(ch)
		self.map.append(row)

	map_file.close()