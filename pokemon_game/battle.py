import random
from pokemon import Pokemon

TYPE_CHART = {
    'fire': {'strong_vs': ['grass'], 'weak_vs': ['water']},
    'water': {'strong_vs': ['fire'], 'weak_vs': ['electric']},
    'grass': {'strong_vs': ['water'], 'weak_vs': ['fire']},
    'electric': {'strong_vs': ['water'], 'weak_vs': ['ground']},
    'rock': {'strong_vs': ['fire'], 'weak_vs': ['water']},
    'psychic': {'strong_vs': ['fighting'], 'weak_vs': ['psychic']}
    # Expand as needed
}

TERRAIN_MODS = {
    'forest': {'grass': 1.2, 'fire': 0.9},
    'water': {'water': 1.2, 'fire': 0.8, 'electric': 0.9},
    'mountain': {'rock': 1.3, 'flying': 0.8},
    'grassland': {},
    'cave': {'ground': 1.2, 'rock': 1.1}
}

def get_modifier(attacker_types, defender_types, terrain):
    mod = 1.0
    for atk_type in attacker_types:
        if atk_type in TYPE_CHART:
            if any(t in TYPE_CHART[atk_type].get('strong_vs', []) for t in defender_types):
                mod *= 2.0
            elif any(t in TYPE_CHART[atk_type].get('weak_vs', []) for t in defender_types):
                mod *= 0.5
    # Terrain
    for t in attacker_types:
        mod *= TERRAIN_MODS.get(terrain, {}).get(t, 1.0)
    return mod

def battle(player_pkmn, wild_pkmn, terrain='grassland'):
    print(f"Wild {wild_pkmn.name} appeared!")
    while not player_pkmn.is_fainted and not wild_pkmn.is_fainted:
        print(f"\n{player_pkmn.name} HP: {player_pkmn.hp}/{player_pkmn.max_hp}")
        print(f"{wild_pkmn.name} HP: {wild_pkmn.hp}/{wild_pkmn.max_hp}")
        
        # Player turn
        print("1. Attack  2. Item  3. Run")
        choice = input("> ")
        if choice == '1':
            print("Attacks:", [a['name'] for a in player_pkmn.attacks])
            atk = input("Attack: ")
            dmg_msg = player_pkmn.attack(atk, wild_pkmn, terrain)
            print(dmg_msg)
        elif choice == '2':
            return 'item'
        elif choice == '3':
            return 'run'
        
        if wild_pkmn.is_fainted: break
        
        # Wild turn
        wild_atk = random.choice(wild_pkmn.attacks)['name']
        dmg_msg = wild_pkmn.attack(wild_atk, player_pkmn, terrain)
        print(dmg_msg)
    
    if player_pkmn.is_fainted:
        print("You fainted! Heal at Pokemon Center.")
        return 'loss'
    else:
        print("Wild Pokemon fainted!")
        if random.random() < 0.3:  # 30% drop
            print("Pokemon dropped a Pokeball!")
            return 'ball_drop'
        return 'win'

def attempt_capture(wild_pkmn, player):
    print(f"\nTry to capture {wild_pkmn.name}? HP low = higher chance!")
    print("Solve riddle for capture: What gets wetter as it dries? (hint: 4 letters)")
    answer = input("> ").strip().lower()
    if answer == 'towel':
        if random.random() < (1 - wild_pkmn.hp / wild_pkmn.max_hp) * 0.7:
            if player.add_pokemon(wild_pkmn):
                print(f"Gotcha! {wild_pkmn.name} joined the team!")
                player.wins += 1
                return True
            else:
                print("Team full!")
        else:
            print("Capture failed!")
    else:
        print("Wrong answer! Pokemon fled.")
    return False
