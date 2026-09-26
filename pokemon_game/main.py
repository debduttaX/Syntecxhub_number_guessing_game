import os
os.chdir(os.path.dirname(__file__))  # Ensure in project dir

from player import Player
from world import World
from battle import battle, attempt_capture
from utils import safe_input, print_status, load_player, get_riddle
from pokemon import Pokemon

def main():
    name = input("Enter trainer name: ")
    player = load_player(name)
    player.save()  # Initial save
    
    world = World()
    
    print("Welcome to Ecosystem Pokemon! Explore, battle, capture with riddles!")
    print("Commands: explore, move [n/s/e/w], status, heal, save, quit")
    
    while True:
        cmd = safe_input("> ", ['explore', 'move', 'status', 'heal', 'save', 'quit', 'north', 'south', 'east', 'west'])
        
        if cmd in ['north', 'south', 'east', 'west']:
            world.move(cmd)
            if random.random() < 0.4:  # 40% encounter
                wild = world.random_encounter()
                active = player.get_active_pokemon()
                if not active:
                    print("No Pokemon! Catch one first.")
                    continue
                result = battle(active, wild, world.current_biome)
                if result == 'win' or result == 'ball_drop':
                    attempt_capture(wild, player)
                elif result == 'loss':
                    player.heal_team()
        
        elif cmd == 'explore':
            wild = world.random_encounter()
            active = player.get_active_pokemon()
            if active:
                result = battle(active, wild, world.current_biome)
                if result in ['win', 'ball_drop']:
                    attempt_capture(wild, player)
        
        elif cmd == 'status':
            print_status(player, world)
        
        elif cmd == 'heal':
            print("Healed team at Pokemon Center!")
            player.heal_team()
        
        elif cmd == 'save':
            player.save()
            print("Game saved!")
        
        elif cmd == 'quit':
            player.save()
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
