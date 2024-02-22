# create class CuteCreature
def __str__(self):
    if self.is_special:
        return f"\nLevel {self.level} {self.species}\n{'-' * 16}\n !!!Special!!!\n\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"
    else:
        return f"\nLevel {self.level} {self.species}\n{'-' * 16}\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"


class CuteCreature
    attr_reader :species :level :current_hp :max_hp :atk :defense :xp :xp_value :xp_needed :is_special
    def initialize(species, max_hp=40, atk=5, defense=3, xp_value=70, is_special=false)
        @species = species
        @level = 1
        @current_hp = max_hp
        @max_hp = max_hp
        @atk = atk
        @defense = defense
        @xp = 0
        @xp_value = xp_value
        @xp_needed = 200
        @is_special = is_special
    end
	def display
		if .is_special:
			return f"\nLevel {self.level} {self.species}\n{'-' * 16}\n !!!Special!!!\n\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"
		else:
			return f"\nLevel {self.level} {self.species}\n{'-' * 16}\nHP:{self.current_hp:>10}/{self.max_hp:<8}\nATK:{self.atk:12}\nDEF:{self.defense:12}\nXP:{self.xp:>9}/{self.xp_needed:<6}\nXP Val:{self.xp_value:9}\n\n"

end