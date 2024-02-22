# 1. a)
class CuteCreature:
	def __init__(self, species, max_hp, atk, defense, xp_value, is_special=False):
		self.species = species
		self.max_hp = max_hp
		self.atk = atk
		self.defense = defense
		self.xp_value = xp_value
		self.is_special = is_special
		self.level = 1
		self.current_hp = max_hp
		self.xp = 0
		self.xp_needed = 200

# b)
	def __str__(self):
		if self.is_special:
			return f"\nLevel {self.level} {self.species}\n{'-' * 16}\n !!!Special!!!\n\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"
		else:
			return f"\nLevel {self.level} {self.species}\n{'-' * 16}\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"


# c)	# should only be callable from gain_xp method
	def level_up(self):	
		self.level += 1
		self.xp_value += 25
		self.xp_needed += 75 * (self.level - 1) + 200
		print(f'{self.species} leveled to {self.level}!')
		if self.level < 10:
			self.max_hp += 7
			self.atk += 3
			self.defense += 3
		else:
			self.max_hp += 2
			self.atk += 1
			self.defense += 1			
		self.current_hp = self.max_hp


# d)	any positive amount - base case needed?
	def gain_xp(self, amount):
		self.xp += amount
		print(f'{self.species} gained {amount} experience!')
		while self.xp >= self.xp_needed:
			self.level_up()


# e)	# no negative hit points base case 
	def take_damage(self, amount):
		print(f'{self.species} took {amount} damage!')
		print()
		self.current_hp -= amount
		if amount >= self.current_hp:
			self.current_hp = 0
			print(f'{self.species} fainted!')


# f)
	def attack(self, target):
		print(f'{self.species} attacks {target.species}!')
		damage = 0 
		import random
		attempt = random.randint(0, 99)
		# print(attempt)

		if attempt >= 90:		# 10% chance of crit
			print('Critical Hit!', end=' ')
			damage = (self.atk - target.defense) * 2
			if damage < 2:
				damage = 2

		elif attempt >= 20:		# 70% chance of hit
			print('Hit!', end=' ')
			damage = self.atk - target.defense
			if damage < 1:
				damage = 1
		else:					# 20% chance of miss
			print('Miss!')
			print()
			return
		target.take_damage(damage)
		if target.current_hp < 1:
			self.gain_xp(target.xp_value)
			print(f'{self.species} defeated {target.species}!')


# g)
chunt = CuteCreature("Shifter", 60, 6, 4, 200, False)
usidore = CuteCreature("Wizard", 50, 7, 4, 125, True)
# print(chunt)
# print(usidore)


if __name__ == '__main__':
	print(chunt)
	print(usidore)
	while chunt.current_hp > 0 and usidore.current_hp > 0:
		chunt.attack(usidore)
		if chunt.current_hp > 0 and usidore.current_hp > 0:
			usidore.attack(chunt)
	print(chunt)
	print(usidore)
print(chunt + usidore)
# print(chunt)
# chunt.gain_xp(200)
# print(chunt)
# print(usidore)
# usidore.gain_xp(5000)
# print(usidore)
# usidore.take_damage(20)
# print(usidore)
# usidore.gain_xp(400)
# print(usidore)
# cast = [usidore, chunt]
# for a in cast:
# 	print(a)
