import random
import os
import json
from player import SAVE_PATH

RIDDLES = [
    ("What gets wetter as it dries?", "towel"),
    ("What has keys but can't open locks?", "piano"),
    ("What has a head, a tail, is brown, and has no legs?", "penny"),
    ("What can travel around the world while staying in a corner?", "stamp"),
    ("What has one eye but can't see?", "needle")
]

def get_riddle():
    question, answer = random.choice(RIDDLES)
    return question, answer

def safe_input(prompt, valid_options=None):
    while True:
        resp = input(prompt).strip().lower()
        if valid_options is None or resp in valid_options:
            return resp
        print("Invalid choice.")

def print_status(player, world):
    print(f"\n=== {player} ===")
    print(f"Biome: {world.current_biome}")
    print("Team:", [p.name for p in player.team])

def load_player(name):
    player = Player.load()
    if player:
        print("Loaded previous save.")
        return player
    print("New game!")
    return Player(name)
