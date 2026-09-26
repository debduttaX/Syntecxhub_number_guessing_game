import json
import os
from pokemon import Pokemon

SAVE_PATH = os.path.join(os.path.dirname(__file__), 'save.json')

class Player:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.inventory = {'pokeballs': 5}
        self.location = 'grassland'
        self.wins = 0

    def add_pokemon(self, pokemon):
        if len(self.team) < 6:
            self.team.append(pokemon)
            return True
        return False

    def get_active_pokemon(self):
        for p in self.team:
            if not p.is_fainted:
                return p
        return None

    def heal_team(self):
        for p in self.team:
            p.heal(p.max_hp // 2)

    def save(self):
        save_data = {
            'name': self.name,
            'team': [p.to_dict() for p in self.team],
            'inventory': self.inventory,
            'location': self.location,
            'wins': self.wins
        }
        with open(SAVE_PATH, 'w') as f:
            json.dump(save_data, f, indent=2)

    @classmethod
    def load(cls):
        if os.path.exists(SAVE_PATH):
            with open(SAVE_PATH, 'r') as f:
                data = json.load(f)
            player = cls(data['name'])
            player.team = [Pokemon.from_dict(p) for p in data['team']]
            player.inventory = data['inventory']
            player.location = data['location']
            player.wins = data['wins']
            return player
        return None

    def __str__(self):
        active = self.get_active_pokemon()
        status = f"Active: {active.name} HP:{active.hp}/{active.max_hp}" if active else "No active Pokemon"
        return f"{self.name} - Team size: {len(self.team)} | {status} | Balls: {self.inventory['pokeballs']}"
