import json
import random
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

class Pokemon:
    def __init__(self, name, types, hp, attacks, trait=''):
        self.name = name
        self.types = types
        self.max_hp = hp
        self.hp = hp
        self.attacks = attacks
        self.trait = trait
        self.level = 5
        self.is_fainted = False

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_fainted = True

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def attack(self, attack_name, target, terrain='neutral'):
        attack = next(a for a in self.attacks if a['name'] == attack_name)
        damage = attack['damage']
        
        # Type effectiveness simplified
        type_mod = 1.0
        for t in target.types:
            if attack['type'] == 'fire' and t == 'water':
                type_mod *= 0.5
            elif attack['type'] == 'water' and t == 'fire':
                type_mod *= 2.0
            # Add more matchups...
        
        # Terrain modifier (unique mechanic)
        terrain_mod = 1.0
        if terrain == 'forest' and 'grass' in self.types:
            terrain_mod *= 1.2
        elif terrain == 'water' and 'fire' in self.types:
            terrain_mod *= 0.8
        # Add more...
        
        final_damage = int(damage * type_mod * terrain_mod * random.uniform(0.85, 1.0))
        target.take_damage(final_damage)
        return f"{self.name} used {attack_name}! Dealt {final_damage} damage."

    @classmethod
    def random_pokemon(cls):
        with open(DATA_PATH, 'r') as f:
            data = json.load(f)
        pkmn_data = random.choice(data)
        return cls(**pkmn_data)

    def to_dict(self):
        return {
            'name': self.name, 'types': self.types, 'hp': self.hp,
            'max_hp': self.max_hp, 'attacks': self.attacks,
            'trait': self.trait, 'level': self.level
        }

    @classmethod
    def from_dict(cls, data):
        pkmn = cls(data['name'], data['types'], data['max_hp'], data['attacks'], data['trait'])
        pkmn.hp = data['hp']
        pkmn.level = data['level']
        return pkmn
