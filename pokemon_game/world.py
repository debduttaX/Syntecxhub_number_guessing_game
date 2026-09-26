import random
from pokemon import Pokemon

BIOMES = {
    'grassland': ['FireFox', 'LeafBird'],
    'forest': ['LeafBird', 'PsyOwl'],
    'water': ['AquaShark', 'ThunderCat'],
    'mountain': ['RockGolem', 'ThunderCat'],
    'cave': ['RockGolem', 'PsyOwl']
}

POKEMON_BY_NAME = {  # Simplified lookup
    'FireFox': lambda: Pokemon('FireFox', ['fire'], 80, [{'name': 'Flame Burst', 'damage': 25, 'type': 'fire'}], 'blaze'),
    'AquaShark': lambda: Pokemon('AquaShark', ['water'], 90, [{'name': 'Water Jet', 'damage': 20, 'type': 'water'}], 'torrent'),
    'LeafBird': lambda: Pokemon('LeafBird', ['grass', 'flying'], 70, [{'name': 'Vine Whip', 'damage': 20, 'type': 'grass'}], 'overgrow'),
    'ThunderCat': lambda: Pokemon('ThunderCat', ['electric'], 75, [{'name': 'Thunderbolt', 'damage': 30, 'type': 'electric'}], 'static'),
    'RockGolem': lambda: Pokemon('RockGolem', ['rock', 'ground'], 100, [{'name': 'Rock Throw', 'damage': 25, 'type': 'rock'}], 'sturdy'),
    'PsyOwl': lambda: Pokemon('PsyOwl', ['psychic'], 65, [{'name': 'Psybeam', 'damage': 22, 'type': 'psychic'}], 'synchronize')
}

class World:
    def __init__(self):
        self.current_biome = 'grassland'
        self.x, self.y = 0, 0

    def move(self, direction):
        moves = {'north': (0, 1), 'south': (0, -1), 'east': (1, 0), 'west': (-1, 0)}
        dx, dy = moves.get(direction, (0, 0))
        self.x += dx
        self.y += dy
        # Procedural biome based on position
        if self.x > 5: self.current_biome = 'mountain'
        elif self.y > 5: self.current_biome = 'forest'
        elif self.y < -5: self.current_biome = 'water'
        elif abs(self.x) > 3: self.current_biome = 'cave'
        else: self.current_biome = 'grassland'
        print(f"Moved {direction}. Now in {self.current_biome} at ({self.x}, {self.y})")

    def random_encounter(self):
        biome_pokemon = BIOMES.get(self.current_biome, BIOMES['grassland'])
        pkmn_name = random.choice(biome_pokemon)
        wild_pkmn = POKEMON_BY_NAME[pkmn_name]()
        return wild_pkmn
