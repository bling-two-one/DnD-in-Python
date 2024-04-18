import enum

class player :
    item_bag = []
    p_level = 0
    p_class = enum.Enum(Rogue = 0, Wizard = 1, Cleric = 2, Fighter = 3)
    def __init__(self, p_class, Race, stats, skills, name) :
        """
           Set player's first state
           ---
           ---
           Race must set as one of race below\n
           - [Dwarf, Elf, Human, Halfling]\n
           ---
           stats argu's numbers must be 5 \n
           - [STR, DEX, CON, INT, WIS, CHA]
           ---
           Get or make skills on [Skill List]\n
           ---
           Name must be shorter than 6 letters\n
           ---
           Class must set as one of race below\n
           - [Rogue, Wizard, Cleric, Fighter]\n
           ---
           Name must be shorter than 6 letters \n
           ---
        """
        self.p_class = p_class
        self.Race = Race
        self.stats = stats
        self.skills = skills
        self.name = name
