"""
Your names: Austin He, Caleb Verma
Your student numbers: A00882336, A01257874
"""
import random
import time
import doctest
import itertools


# Print colors
class Colours:
    end = '\033[0m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    magenta = '\033[95m'
    cyan = '\033[96m'


# Constants enclosed in tuples (yes, it looks weird)
REGEN_VALUE = (4,)
MAX_PLAYER_DAMAGE = (20,)
MAX_ENEMY_DAMAGE = (10,)
MAX_SHIV_DAMAGE = (4,)
STARTING_X_COORDINATE = (0,)
STARTING_Y_COORDINATE = (0,)


def ascii_intro():
    """Print ascii art of game title.

    :postcondition: print ascii art of game title

    >>> ascii_intro() # doctest: +NORMALIZE_WHITESPACE
    \033[93m  /$$$$$$                        /$$                                /$$$$$$  /$$
            /$$__  $$                      | $$                               /$$__  $$|__/
            | $$  \__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$   /$$
            |  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/
            \____  $$| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/       \____  $$| $$ \  $$$$/
            /$$  \ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \ $$| $$  >$$  $$
           |  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\  $$
            \______/  \_______/ \_______/   \___/   \______/ |__/             \______/ |__/|__/  \__/
    \033[0m

    """
    print(f"{Colours.yellow}  /$$$$$$                        /$$                                /$$$$$$  /$$          ")
    print(f" /$$__  $$                      | $$                               /$$__  $$|__/          ")
    print(f"| $$  \__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$   /$$")
    print(f"|  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/")
    print(f" \____  $$| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/       \____  $$| $$ \  $$$$/ ")
    print(f" /$$  \ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \ $$| $$  >$$  $$ ")
    print(f"|  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\  $$")
    print(f" \______/  \_______/ \_______/   \___/   \______/ |__/             \______/ |__/|__/  \__/\n{Colours.end}")


def story_introduction_text():
    """Print the introductory story text.

    :postcondition: print the introductory story text

    >>> story_introduction_text() # doctest: +NORMALIZE_WHITESPACE
    In the distant future, humankind has colonized the vast, cold reaches of space. From suburban planets to entire \
    solar systems dedicated to vice, there isn't a sector in the Milky Way Galaxy that's been left untouched by our \
    ever-expanding race. One such sector is devoted to storing all of humanity's physical wealth and fortune. Many a \
    space pirate has tried their hand at laying siege to this sector in hopes of plundering some riches for themselves,\
    and all have been gunned down by the local security militias.
    <BLANKLINE>
    All except you. You put together a ragtag crew, formulated the perfect plan, and somehow managed to fill your ship \
    with as much stolen loot as she could carry. Now all you have to do is escape to the nearest wormhole, treasure in \
    tow, and you'll be christened the first ever space captain to have successfully pilfered from...
    <BLANKLINE>
    """
    print(f"In the distant future, humankind has colonized the vast, cold reaches of space. From suburban planets "
          f"to entire solar systems dedicated to vice, there isn't a sector in the\nMilky Way Galaxy that's been "
          f"left untouched by our ever-expanding race. One such sector is devoted to storing all of humanity's physical"
          f" wealth and fortune. Many a space\npirate has tried their hand at laying siege to this sector in hopes of "
          f"plundering some riches for themselves, and all have been gunned down by the local security militias. \n")
    print(f"All except you. You put together a ragtag crew, formulated the perfect plan, and somehow managed to fill "
          f"your ship with as much stolen loot as she could carry. Now all you\nhave to do is escape to the nearest "
          f"wormhole, treasure in tow, and you'll be christened the first ever space captain to have successfully "
          f"pilfered from...\n")


def boss_fight_start_text(player):
    """Print text introducing the appropriate boss phase.

    :param player: a dictionary
    :precondition: player is a dictionary representing the player character
    :precondition: player contains a key called boss_phase_counter
    :precondition: the value of boss_phase_counter is between [1, 3]
    :postcondition: print text introducing the appropriate boss phase

    >>> player_character = make_player()
    >>> boss_fight_start_text(player_character) # doctest: +NORMALIZE_WHITESPACE
    You've almost escaped from Sector Six, treasure in tow. To your surprise, the enemy militia is nowhere to be found.\
    Where's their final resistance? As you begin your approach to the wormhole's entrance, a shrill scream surrounds \
    your ship. Sound...isn't supposed to travel through space. Whatever made that sound transcends the laws of nature \
    itself. From the pitch black of the wormhole, you notice a pair of scarlet eyes peering back at you from the \
    darkness. A titanic, grotesque \033[95mpink\033[0m body emerges from the wormhole. It's an...
    \033[95mIntergalactic Space Worm\033[0m!
    <BLANKLINE>
    >>> player_character["boss_phase_counter"] = 2
    >>> boss_fight_start_text(player_character) # doctest: +NORMALIZE_WHITESPACE
    It's a \033[95mTwo-Headed Intergalactic Space Worm\033[0m!
    <BLANKLINE>
    >>> player_character["boss_phase_counter"] = 1
    >>> boss_fight_start_text(player_character) # doctest: +NORMALIZE_WHITESPACE
    Get rid of the \033[95mHeadless Intergalactic Space Worm\033[0m to finally escape Sector Six!
    <BLANKLINE>
    """
    if player["boss_phase_counter"] == 3:
        print(f"You've almost escaped from Sector Six, treasure in tow. To your surprise, the enemy militia is nowhere"
              f" to be found. Where's their final resistance?\nAs you begin your approach to the wormhole's entrance, a"
              f" shrill scream surrounds your ship. Sound...isn't supposed to travel through space. Whatever made "
              f"that\nsound transcends the laws of nature itself. From the pitch black of the wormhole, you notice a "
              f"pair of scarlet eyes peering back at you from the darkness.\nA titanic, grotesque "
              f"{Colours.magenta}pink{Colours.end} body emerges from the wormhole. It's an...\n"
              f"{Colours.magenta}Intergalactic Space Worm{Colours.end}!\n")
    elif player["boss_phase_counter"] == 2:
        print(f"It's a {Colours.magenta}Two-Headed Intergalactic Space Worm{Colours.end}!\n")
    elif player["boss_phase_counter"] == 1:
        print(f"Get rid of the {Colours.magenta}Headless Intergalactic Space Worm{Colours.end} to finally escape Sector"
              f" Six!\n")


def boss_phase_death_text(player):
    """Print text introducing the end game boss.

    :return:
    >>> player_character = make_player()
    >>> boss_phase_death_text(player_character) # doctest: +NORMALIZE_WHITESPACE

    >>> player_character["boss_phase_counter"] = 2
    >>> boss_phase_death_text(player_character) # doctest: +NORMALIZE_WHITESPACE

    >>> player_character["boss_phase_counter"] = 1
    >>> boss_phase_death_text(player_character) # doctest: +NORMALIZE_WHITESPACE
    """
    if player["boss_phase_counter"] == 3:
        print(f"You manage to obliterate the {Colours.magenta}Intergalactic Space Worm{Colours.end}'s head!\nHowever, "
              f"its smouldering corpse begins to convulse, and from the gaping hole in its neck sprouts two more "
              f"heads!\n")
    elif player["boss_phase_counter"] == 2:
        print(f"You manage to obliterate the {Colours.magenta}Two-Headed Intergalactic Space Worm{Colours.end}'s heads!"
              f"\nHowever, its corpse now blocks the entrance to the wormhole.\n")
    elif player["boss_phase_counter"] == 1:
        print(f"You finally obliterate the {Colours.magenta}Headless Intergalactic Space Worm{Colours.end}!\n")


def story_ending_text(player):
    """Print the ending story text.

    :param player: a dictionary
    :precondition: player is a dictionary representing the player character
    :precondition: player contains a key called name
    :postcondition: print the ending story text

    >>> player_character = make_player()
    >>> player_character['name'] = "Jaraxxus"
    >>> story_ending_text(player_character) # doctest: +NORMALIZE_WHITESPACE
    You and your crew disappear into the wormhole, along with untold treasure. For millennia, the galaxy will tell \
    tales of the legendary Captain \033[94mJaraxxus\033[0m, the first space captain to pilfer from...
    <BLANKLINE>
    \033[93m         /$$$$$$                        /$$                                /$$$$$$  /$$
            /$$__  $$                      | $$                               /$$__  $$|__/
            | $$  \__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$   /$$
            |  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/
            \____  $$| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/       \____  $$| $$ \  $$$$/
            /$$  \ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \ $$| $$  >$$  $$
           |  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\  $$
            \______/  \_______/ \_______/   \___/   \______/ |__/             \______/ |__/|__/  \__/\033[0m
    <BLANKLINE>
    Thanks for playing!

    """
    print(f"You and your crew disappear into the wormhole, along with untold treasure. For millennia, the galaxy "
          f"will tell tales of the legendary\nCaptain {Colours.blue}{player['name']}{Colours.end}, the first space "
          f"captain to pilfer from...\n")
    print(f"{Colours.yellow}  /$$$$$$                        /$$                                /$$$$$$  /$$          ")
    print(f" /$$__  $$                      | $$                               /$$__  $$|__/          ")
    print(f"| $$  \__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$   /$$")
    print(f"|  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/")
    print(f" \____  $$| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/       \____  $$| $$ \  $$$$/ ")
    print(f" /$$  \ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \ $$| $$  >$$  $$ ")
    print(f"|  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\  $$")
    print(f" \______/  \_______/ \_______/   \___/   \______/ |__/             \______/ |__/|__/  \__/{Colours.end}\n")
    print(f"Thanks for playing!")


def player_death_text():
    """Print text describing player death.

    postcondition: print text describing player death
    """
    print(f"Your ship's integrity has been breached! Sector Six has claimed another crew of would-be thieves.\n")


def enemy_death_text(player):
    """Print text describing enemy death.

    postcondition: print text describing enemy death
    """
    enemy = make_appropriate_enemy_type(player)
    print(f"The enemy {Colours.red}{enemy['name']}{Colours.end} has been defeated!\n")
    time.sleep(1)


def check_if_player_in_boss_room(x_coordinate, y_coordinate):
    """Return True if player x- and y- coordinates are both 24, else return False.

    :return: True if player x- and y- coordinates are both 24, else return False

    >>> check_if_player_in_boss_room(0, 5)
    False
    >>> check_if_player_in_boss_room(24, 24)
    True
    """
    if x_coordinate == 24 and y_coordinate == 24:
        return True
    else:
        return False


def make_player():  # A
    """Return a dictionary representing the player's maximum health, their starting x-coordinate, their starting
       y-coordinate, and their name.

    :postcondition: Return a dictionary representing the player's maximum health, their starting x-coordinate, their
                    starting y-coordinate, and their name
    :return: a dictionary representing the player's current health, starting x-coordinate and y-coordinate, and name

    >>> make_player()
    {'health': 20, 'x-coordinate': 0, 'y-coordinate': 0, 'name': ''}
    """
    return {"health": 20,
            "maximum_health": 20,
            "x-coordinate": STARTING_X_COORDINATE[0],
            "y-coordinate": STARTING_Y_COORDINATE[0],
            "name": None,
            "exp": 0,
            "ship": None,
            "player_class": None,
            "player_class_special_action": None,
            "special_action_counter": 0,
            "level": 1,
            "damage": MAX_PLAYER_DAMAGE[0],
            "boss_phase_counter": 3
            }


def input_player_name():  # A
    """Return player name.

    :postcondition: convert player's input into title case
    :return: player name

    no doctests, accepts user input
    """
    name_input = str(input(f"Enter your {Colours.blue}name{Colours.end}, captain: ")).title()
    if name_input.lower() == "chris" or name_input.lower() == "christopher" or name_input.lower() == "chris thompson":
        print(f"You can be more adventurous than that! \n")
        return input_player_name()
    elif name_input.strip() == "":
        print(f"Every space captain needs a name! \n")
        return input_player_name()
    else:
        return name_input


def display_player_class_menu():  # A
    """

    :return:
    """
    class_choices = list(enumerate(["Squire", "Sapper", "Ghost", "Cherub"], start=1))
    print(f"Select a {Colours.blue}spaceship{Colours.end}: \n", class_choices)
    return input()


def select_player_class(player):  # A
    """Print class description and return class after being passed to confirm_player_class().

    :precondition: user enters input when prompted
    :postcondition: print numbered list of class options [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'),
                    (4, 'Cherub')]
    :postcondition: print class description
    :postcondition: pass user input to confirm_player_class()
    :return: class after being passed to confirm_player_class()
    """
    choice = display_player_class_menu()
    if choice == "1":
        if confirm_player_class("Squire", player):
            warrior_ship(player)
    elif choice == "2":
        if confirm_player_class("Sapper", player):
            magician_ship(player)
    elif choice == "3":
        if confirm_player_class("Ghost", player):
            thief_ship(player)
    elif choice == "4":
        if confirm_player_class("Cherub", player):
            priest_ship(player)
    else:
        print(f"That is not a valid choice! \n")
        select_player_class(player)
    return player


def print_class_description(class_name):  # A
    """

    :param class_name:
    :return:
    """
    if class_name == "Squire":
        print(f"A Lazarus Engine™ allows for this ship to repair itself after its hull integrity has been completely "
              "breached for the first time.")
    elif class_name == "Sapper":
        print(f"Destroy enemy ships to steal their energy and charge up your Quasar Cannon™ for a devastating attack.")
    elif class_name == "Ghost":
        print(f"A nimble ship covered in aerodynamic SlipStream™ technology allows the pilot to make the first move in "
              "combat, and attack multiple times in one turn.")
    elif class_name == "Cherub":
        print(f"QuickFix™ Protocols allows this ship to repair itself during combat.")


def confirm_player_class(class_name, player):  # A
    """Return class_name or call select_player_class, depending on user input.

    :param class_name: any string
    :param player: a dictionary
    :precondition: class_name is any string representing the selected player class
    :precondition: user enters input when prompted
    :postcondition: print f"Do you pilot a {class_name}?"
    :postcondition: print a numbered list of options [(1, 'Yes'), (2, 'No')]
    :postcondition: return class_name if input is "1"
    :postcondition: call select_player_class() if input is "2"
    :postcondition: print "That is not a valid choice" if input is neither "1" or "2" and recall confirm_player_class()
    :return: class_name if input is "1", select_player_class() if input is "2"
    """
    print_class_description(class_name)
    print(f"Do you pilot a {Colours.blue}{class_name}{Colours.end}?")
    print(list(enumerate(["Yes", "No"], start=1)))

    choice = input()
    if choice == "1":
        return True
    elif choice == "2":
        select_player_class(player)
    else:
        print(f"That is not a valid choice! \n")
        return confirm_player_class(class_name, player)


def warrior_ship(player):  # A
    """Modify dictionary to change values to attributes of the warrior ship.

    :param player: must be a dictionary
    :precondition: must have key "health"
    :precondition: must have key "maximum_health"
    :precondition: must have key "ship"
    :precondition: must have key "player_class"
    :precondition: must have key "player_class_special_action"
    :precondition: must have key "special_action_counter"
    :precondition: must have key "damage"
    :postcondition: modify dictionary to include new attributes of the warrior ship
    :return: updated player dictionary

    >>> warrior_ship({"health": 20, "maximum_health":20, "ship": None, "player_class": None, \
    "player_class_special_action": None, "special_action_counter": 0, "damage": 20}) # doctest: +NORMALIZE_WHITESPACE
    {'health': 18, 'maximum_health': 18, 'ship': 'Warrior', 'player_class': 'Squire',
    'player_class_special_action': 'Resurrect', 'special_action_counter': 1, 'damage': 25}
    """
    player["health"] -= 2
    player["maximum_health"] -= 2
    player["ship"] = "Warrior"
    player["player_class"] = "Squire"
    player["player_class_special_action"] = "Resurrect"
    player["special_action_counter"] = 1
    player["damage"] = round(MAX_PLAYER_DAMAGE[0] * 1.25)
    return player


def magician_ship(player):  # A
    """Modify dictionary to change values to attributes of the magician ship.

    :param player: must be a dictionary
    :precondition: must have key "ship"
    :precondition: must have key "player_class"
    :precondition: must have key "player_class_special_action"
    :precondition: must have key "special_action_counter"
    :precondition: must have key "damage"
    :postcondition: modify dictionary to include new attributes of the magician ship
    :return: updated player dictionary

    >>> magician_ship({"ship": None, "player_class": None, "player_class_special_action": None, \
    "special_action_counter": 0, "damage": 20}) # doctest: +NORMALIZE_WHITESPACE
    {'ship': 'Magician', 'player_class': 'Sapper', 'player_class_special_action': 'Magic Blast',
    'special_action_counter': 0, 'damage': 16}
    """
    player["ship"] = "Magician"
    player["player_class"] = "Sapper"
    player["player_class_special_action"] = "Magic Blast"
    player["special_action_counter"] = 0
    player["damage"] = round(MAX_PLAYER_DAMAGE[0] * .8)
    return player


def thief_ship(player):  # A
    """Modify dictionary to change values to attributes of the thief ship.

    :param player: must be a dictionary
    :precondition: must have key "ship"
    :precondition: must have key "player_class"
    :precondition: must have key "player_class_special_action"
    :precondition: must have key "damage"
    :postcondition: modify dictionary to include new attributes of the thief ship
    :return: updated player dictionary

    >>> thief_ship({"ship": None, "player_class": None, "player_class_special_action": None, "damage": 20})
    {'ship': 'Thief', 'player_class': 'Ghost', 'player_class_special_action': 'Multi Strike', 'damage': 20}
    """
    player["ship"] = "Thief"
    player["player_class"] = "Ghost"
    player["player_class_special_action"] = "Multi Strike"
    player["damage"] = MAX_PLAYER_DAMAGE[0]
    return player


def priest_ship(player):  # A
    """Modify dictionary to change values to attributes of the priest ship.

    :param player: must be a dictionary
    :precondition: must have key "health"
    :precondition: must have key "maximum_health"
    :precondition: must have key "ship"
    :precondition: must have key "player_class"
    :precondition: must have key "player_class_special_action"
    :precondition: must have key "damage"
    :postcondition: modify dictionary to include new attributes of the priest ship
    :return: updated player dictionary

    >>> priest_ship({"health": 20, "maximum_health":20, "ship": None, "player_class": None, \
    "player_class_special_action": None, "damage": 20}) # doctest: +NORMALIZE_WHITESPACE
    {'health': 16, 'maximum_health': 16, 'ship': 'Priest', 'player_class': 'Cherub',
    'player_class_special_action': 'Healing Spell', 'damage': 20}
    """
    player["health"] -= 4
    player["maximum_health"] -= 4
    player["ship"] = "Priest"
    player["player_class"] = "Cherub"
    player["player_class_special_action"] = "Healing Spell"
    player["damage"] = MAX_PLAYER_DAMAGE[0]
    return player


def special_action_selector(player):  # A
    """

    :param player:
    :return:
    """
    if player["ship"] == "Warrior":
        resurrect(player)
    elif player["ship"] == "Magician":
        blast_damage = magic_blast(player)
        print(f"You charged up your beam to blast the enemy with {Colours.blue}{blast_damage}{Colours.end} "
              f"damage!\n")
        return blast_damage
    elif player["ship"] == "Thief":
        return multi_attack(player)
    elif player["ship"] == "Priest":
        heal_spell(player)


def resurrect(player):  # A
    """

    :param player:
    :return:
    """
    if player["special_action_counter"] == 1:
        if player["health"] <= 0:
            player["special_action_counter"] = 0
            new_hp = 5 + player["level"] * 5
            player["health"] = new_hp
            print(f"Your undying will allowed you to survive the attack and restored your health to "
                  f"{Colours.blue}{new_hp}{Colours.end}!\n")
            return player
        else:
            print(f"Your passive will allow you to survive a critical attack.\n")
    else:
        print(f"Your passive have already been used. You will not revive if your hp hits 0.\n")


def magic_blast(player):  # A
    """

    :param player:
    :return:
    """
    blast_damage = player["special_action_counter"] * 5
    player["special_action_counter"] = 0
    print(f"You relinquished your charges to deal {Colours.blue}{blast_damage}{Colours.end} to the enemy!")
    return blast_damage


def multi_attack(player):  # A
    """

    :param player:
    :return:
    """
    split_attack = int(round(player["damage"] * player["level"] * 1.25 / 5))
    total_attack = 0
    for attacks in range(0, 5):
        attack = random.randint(1, split_attack)
        print(f"You dealt {Colours.blue}{attack}{Colours.end} damage to the enemy!")
        total_attack += attack
    return total_attack


def heal_spell(player):  # A
    """

    :param player:
    :return:
    """
    amount_healed = player["level"] * 6
    if amount_healed + player["health"] > player["maximum_health"]:
        print(f"You repaired your hull for {Colours.blue}{player['maximum_health'] - player['health']}{Colours.end}"
              f" health.")
        player["health"] = player["maximum_health"]
    else:
        player["health"] += amount_healed
        print(f"You repaired your hull for {Colours.blue}{amount_healed}{Colours.end} health.")
    return player


def make_enemy_difficulty_one():  # A
    """

    :return:
    """
    return {
        "name": "Dinghy",
        "health": 10,
        "experience_points": 25,
        "maximum_damage": 5
    }


def make_enemy_difficulty_two():  # A
    """

    :return:
    """
    return {
        "name": "Gunner",
        "health": 20,
        "experience_points": 50,
        "maximum_damage": 10
    }


def make_enemy_difficulty_three():  # A
    """

    :return:
    """
    return {
        "name": "Disruptor",
        "health": 60,
        "experience_points": 100,
        "maximum_damage": 5,
        "special_ability_counter": 4
    }


def make_enemy_difficulty_four():  # A
    """

    :return:
    """
    return {
        "name": "Shredder",
        "health": 40,
        "experience_points": 150,
        "maximum_damage": 25,
    }


def make_appropriate_enemy_type(player):
    """

    :param player:
    :return:
    """
    if player["x-coordinate"] in range(20, 25) or player["y-coordinate"] in range(20, 25) and \
            (player["x-coordinate"] != 24 and player["y-coordinate"] != 24):
        return make_enemy_difficulty_four()
    elif player["x-coordinate"] in range(15, 20) or player["y-coordinate"] in range(15, 20):
        return make_enemy_difficulty_three()
    elif player["x-coordinate"] in range(5, 15) or player["y-coordinate"] in range(5, 15):
        return make_enemy_difficulty_two()
    elif player["x-coordinate"] in range(0, 5) or player["y-coordinate"] in range(0, 5):
        return make_enemy_difficulty_one()


def enemy_disruptor_teleport_attack_countdown(enemy):
    """

    :param enemy:
    :return:
    """
    enemy["special_ability_counter"] -= 1
    if enemy["special_ability_counter"] > 0:
        print(f"The enemy {Colours.red}{enemy['name']}{Colours.end} is charging...something.")
    return enemy


def enemy_disruptor_teleport_attack_activate(enemy, player):
    """

    :param enemy:
    :param player:
    :return:
    """
    if enemy["special_ability_counter"] == 0:
        random_x_coordinate = random.randint(5, 10)
        random_y_coordinate = random.randint(5, 10)
        player["x-coordinate"] = random_x_coordinate
        player["y-coordinate"] = random_y_coordinate
        print(f"The enemy {enemy['name']} opened a rift in spacetime and teleported you "
              f"to {player['x-coordinate']}, {player['y-coordinate']}!")
        return player
    else:
        return player


def make_enemy_boss_phase_one():
    return {
        "name": "Intergalactic Space Worm",
        "health": 40,
        "maximum_damage": 5
    }


def make_enemy_boss_phase_two():
    return {
        "name": "Two-Headed Intergalactic Space Worm",
        "health": 50,
        "maximum_damage": 5
    }


def make_enemy_boss_phase_three():
    return {
        "name": "Headless Intergalactic Space Worm",
        "health": 80,
        "maximum_damage": 2,
        "special_ability_counter": 5
    }


def make_appropriate_boss_phase(player):
    if player["boss_phase_counter"] == 3:
        return make_enemy_boss_phase_one()
    elif player["boss_phase_counter"] == 2:
        return make_enemy_boss_phase_two()
    elif player["boss_phase_counter"] == 1:
        return make_enemy_boss_phase_three()


def boss_battle_player_attack(boss, player):
    """Return enemy's health value after being attacked by player.

    :param boss: a positive integer
    :param player: a dictionary
    :precondition: enemy_health is any positive integer
    :postcondition: subtract a random integer between [1, player["damage"]] from enemy_health
    :postcondition: return enemy_health
    :return: enemy_health

    no doctest, this uses random values
    """
    player_damage = random.randint(1, player["damage"])
    enemy = make_appropriate_boss_phase(player)
    print(f"You did {Colours.blue}{player_damage}{Colours.end} damage to the "
          f"{Colours.magenta}{enemy['name']}{Colours.end}!\n")
    boss["health"] -= player_damage
    return boss["health"]


def combat_boss_attack_phase_one_and_three(player):
    boss = make_appropriate_boss_phase(player)
    enemy_damage = random.randint(1, boss['maximum_damage'])
    player['health'] -= enemy_damage
    print(f"The {Colours.magenta}{boss['name']}{Colours.end} did {Colours.magenta}{enemy_damage}{Colours.end}"
          f" damage to you!\n")
    return player['health']


def combat_boss_attack_phase_two(player):
    boss = make_appropriate_boss_phase(player)
    enemy_damage_first_attack = random.randint(1, boss['maximum_damage'])
    player['health'] -= enemy_damage_first_attack
    print(f"The {Colours.magenta}{boss['name']}{Colours.end}'s left head did "
          f"{Colours.magenta}{enemy_damage_first_attack}{Colours.end} damage to you!")
    enemy_damage_second_attack = random.randint(1, boss['maximum_damage'])
    player['health'] -= enemy_damage_second_attack
    print(f"The {Colours.magenta}{boss['name']}{Colours.end}'s right head did "
          f"{Colours.magenta}{enemy_damage_second_attack}{Colours.end} damage to you!\n")
    return player['health']


def combat_boss_attack(player):
    time.sleep(1)
    if player["boss_phase_counter"] == 3 or player["boss_phase_counter"] == 1:
        return combat_boss_attack_phase_one_and_three(player)
    elif player["boss_phase_counter"] == 2:
        return combat_boss_attack_phase_two(player)


def boss_battle_print_health_values(player, boss):
    """

    :return:
    """
    time.sleep(1)
    print(f"Your {Colours.blue}{player['player_class']}{Colours.end} can take "
          f"{Colours.blue}{player['health']}{Colours.end} more points of damage.")
    print(f"The enemy {Colours.magenta}{boss['name']}{Colours.end} can take "
          f"{Colours.magenta}{boss['health']}{Colours.end} more points of damage.\n")


def boss_ultimate_attack_countdown(boss):
    """

    :param boss:
    :return:
    """
    boss["special_ability_counter"] -= 1
    if boss["special_ability_counter"] > 0:
        print(f"The {Colours.magenta}{boss['name']}{Colours.end}'s body writhes.")
    return boss


def boss_ultimate_attack_activate(enemy, player):
    """

    :param enemy:
    :param player:
    :return:
    """
    if enemy["special_ability_counter"] == 0:
        print(f"The {enemy['name']}'s body unleashes overwhelming astral power!\nYou, your ship, your crew, and "
              f"everything else in Sector Six takes {Colours.magenta}99999{Colours.end} damage!\n")
        player["health"] -= 99999
        return player
    elif enemy["special_ability_counter"] < 0:
        print(f"The {enemy['name']}'s body unleashes EVEN MORE overwhelming astral power!\nYou, your ship, your crew, "
              f"and everything else in Sector Six takes {Colours.magenta}99999{Colours.end} damage! Again!\n")
        player["health"] -= 99999
        return player
    else:
        return player


def game_board_coordinates(player_x_coordinate, player_y_coordinate):
    """Return dictionary representing game board, with unoccupied coordinates containing a blue asterisk, and occupied
       coordinates containing a yellow at symbol.

    :param player_x_coordinate: any positive integer between [0, 24]
    :param player_y_coordinate: any positive integer between [0, 24]
    precondition: player_x_coordinate is any positive integer between [0, 24] representing current player x-coordinate
    precondition: player_x_coordinate is any positive integer between [0, 24] representing current player y-coordinate
    :postcondition: generate dictionary of game board
    :postcondition: assign every key the value of a blue asterisk
    :postcondition: reassign key corresponding to current player coordinates value of a yellow at symbol
    :return: dictionary representing game board, with unoccupied coordinates containing the value of a blue asterisk,
             and key corresonding to current player location containing the value of a yellow at symbol
    >>> game_board_coordinates(0, 0)

    """
    board_coordinates = [(x_coordinates, y_coordinates) for x_coordinates in range(0, 25) for
                         y_coordinates in range(0, 25)]
    game_board = {coordinate: f"{Colours.blue}*{Colours.end}" for coordinate in board_coordinates}
    game_board[(player_y_coordinate, player_x_coordinate)] = f"{Colours.yellow}@{Colours.end}"
    return game_board


def display_game_board(x_coordinate, y_coordinate, game_board):
    """Return the values in game_board visualized in a 25 by 25 size grid.

    :param x_coordinate: any positive integer between [0, 24]
    :param y_coordinate: any positive integer between [0, 24]
    :param game_board: a dictionary
    :precondition: player_x_coordinate is any positive integer between [0, 24] representing current player x-coordinate
    :precondition: player_x_coordinate is any positive integer between [0, 24] representing current player y-coordinate
    :precondition: game_board is a dictionary whose keys are tuples of length 2
    :precondition: the tuples in game_board are permutations of all integers between [0, 24]
    :precondition: the values in game_board are either blue asterisks or yellow at symbols
    :postcondition: return the values in game_board visualized in a 25 by 25 size grid
    :return: the values in game_board visualized in a 25 by 25 size grid

    >>> display_game_board(0, 0, game_board_coordinates(0, 0))

    """
    surface_visualization = list(game_board.values())
    surface_visualization.insert(0, "")
    for index in range(1, len(surface_visualization) + 25):
        if index % 26 == 0:
            surface_visualization.insert(index, "\n")
    surface_visualization.pop()
    print(*surface_visualization, sep=" ")
    print(f"You are at {x_coordinate}, {y_coordinate}.")


def display_main_menu():
    """Return user input after printing a numbered list.

    :postcondition: print a numbered list [(1, 'Move'), (2, 'Status Report'), (3, 'Quit Game')]
    :postcondition: return user input
    :return: user input

    no doctest, accepts user input
    """
    print(list(enumerate(["Move", "Status Report", "Quit Game"], start=1)))
    return input()


def check_player_statistics(player):
    """Print values of player name, health, level, experience points, class, and class special action.

    :param player: a dictionary
    :precondition: player is a dictionary containing values related to player
    :postcondition: print values of player name, health, level, experience points, class, and class special action

    >>> player_dictionary = make_player()
    >>> check_player_statistics(player_dictionary)

    """
    print(f"You are Captain {Colours.blue}{player['name']}{Colours.end}.")
    print(f"Captain {player['name']} pilots a {Colours.blue}{player['player_class']}{Colours.end}, which has the "
          f"special ability {Colours.blue}{player['player_class_special_action']}{Colours.end}.")
    print(f"Your {player['player_class']} can take {Colours.blue}{player['health']}{Colours.end} more points of "
          f"damage.")
    print(f"Your {player['player_class']} is level {Colours.blue}{player['level']}{Colours.end}.")
    print(f"You have {Colours.blue}{player['exp']}{Colours.end} scrap, "
          f"{Colours.blue}{300 - int(player['exp'])}{Colours.end} scrap away from a "
          f"{Colours.blue}ship upgrade{Colours.end}.\n")


def cardinal_direction():
    """Return player directional input.

    :postcondition: display a list of cardinal directions
    :postcondition: convert player's input into an integer
    :return: integer representing player's choice

    no doctests, accepts user input
    """
    directions = ["North", "East", "South", "West"]
    options = []
    for choice in zip(itertools.count(1), directions):
        options.append(choice)
    print(f"Please enter a number corresponding to the direction you wish to move in.")
    print(options)
    choice = input()
    if choice.isdigit():
        return int(choice)
    else:
        return False


def validate_move(direction, x_coordinate, y_coordinate):
    """Return True if direction would keep player within the bounds of the map given x_coordinate and y_coordinate, else
       return False.

    :param direction: any integer
    :param x_coordinate: any integer
    :param y_coordinate: any integer
    :precondition: direction is any integer
    :precondition: x_coordinate is any integer
    :precondition: y_coordinate is any integer
    :postcondition: return True if direction is 1 and current y_coordinate is not 0
    :postcondition: return True if direction is 2 and current x_coordinate is not 24
    :postcondition: return True if direction is 3 and current y_coordinate is not 24
    :postcondition: return True if direction is 4 and current x_coordinate is not 0
    :postcondition: return False if any of the above postconditions were not satisfied
    :return: True if direction was a valid move, else False

    >>> validate_move(1, 3, 0)
    False
    >>> validate_move(1, 2, 3)
    True
    >>> validate_move(2, 3, 0)
    True
    >>> validate_move(2, 24, 0)
    False
    >>> validate_move(3, 2, 0)
    True
    >>> validate_move(3, 2, 24)
    False
    >>> validate_move(4, 1, 24)
    True
    >>> validate_move(4, 0, 24)
    False
    """
    if (direction == 2 and (x_coordinate == 23 and y_coordinate == 24)) or (direction == 3 and (x_coordinate == 24 and
                                                                                                y_coordinate == 23)):
        return confirm_move_to_boss_room()
    elif direction == 1 and y_coordinate != 0:
        return True
    elif direction == 2 and x_coordinate != 24:
        return True
    elif direction == 3 and y_coordinate != 24:
        return True
    elif direction == 4 and x_coordinate != 0:
        return True
    else:
        return False


def confirm_move_to_boss_room():
    """

    :return:
    """
    print(f"You're about to enter the gravitational pull of the wormhole. This is a point of no return. You've almost "
          "escaped Sector Six with your treasure, but you have a feeling you\nmay face some final resistance...\n"
          "Are you sure you wish to proceed?")
    print(list(enumerate(["Yes", "No"], start=1)))

    choice = input()
    if choice == "1":
        return True
    if choice == "2":
        return False


def move_x_axis(direction, x_coordinate):
    """Increment or decrement x_coordinate.

    :param direction: an integer
    :param x_coordinate: an integer
    :precondition: direction is any integer
    :precondition: x_coordinate is any integer
    :precondition: direction is 2 or 4
    :postcondition: if direction is 2, return x_coordinate incremented by 1
    :postcondition: if direction is 3, return x_coordinate decremented by 1
    :return: incremented or decremented x_coordinate

    >>> move_x_axis(2, 3)
    4
    >>> move_x_axis(4, 4)
    3
    """
    if direction == 2:
        return x_coordinate + 1
    elif direction == 4:
        return x_coordinate - 1
    return x_coordinate


def move_y_axis(direction, y_coordinate):
    """Increment or decrement x_coordinate.

    :param direction: an integer
    :param y_coordinate: an integer
    :precondition: direction is any integer
    :precondition: y_coordinate is any integer
    :precondition: direction is 1 or 3
    :postcondition: if direction is 1, return y_coordinate decremented by 1
    :postcondition: if direction is 3, return y_coordinate incremented by 1
    :return: incremented or decremented y_coordinate

    >>> move_y_axis(1, 3)
    2
    >>> move_y_axis(3, 3)
    4
    """
    if direction == 1:
        return y_coordinate - 1
    elif direction == 3:
        return y_coordinate + 1
    else:
        return y_coordinate


def regen_health(player_health, maximum_health):  # A
    """Add REGEN_VALUE to current_health if current_health <= maximum_health, else return maximum_health.

    :param player_health: any integer less than or equal to maximum_health
    :param maximum_health: any integer
    :precondition: player_health is any integer
    :precondition: maximum_health is any integer
    :postcondition: add REGEN_VALUE to player_health if player_health <= maximum_health after adding REGEN_VALUE
    :postcondition: make player_health = maximum_health if adding REGEN_VALUE to player_health would make it >
                    maximum_health
    :return: player_health plus REGEN_VALUE if player_health <= maximum_health, else maximum_health

    >>> regen_health(-1, 20)
    You regained 4 health points!
    3
    >>> regen_health(14, 20)
    You regained 4 health points!
    18
    >>> regen_health(19, 20)
    You regained all of your health!
    20
    >>> regen_health(20, 20)
    20
    """
    if player_health <= (maximum_health - REGEN_VALUE[0]):
        print(f"You repaired your ship by {Colours.blue}{REGEN_VALUE[0]}{Colours.end} points!")
        return player_health + REGEN_VALUE[0]
    elif maximum_health > player_health > (maximum_health - REGEN_VALUE[0]):
        print(f"You repaired your ship {Colours.blue}completely{Colours.end}!")
        return maximum_health
    else:
        return player_health


def backstab(player_health):  # A
    """20 percent chance to subtract between [1, MAX_SHIV_DAMAGE] from current_health, else return current_health.

    :param player_health: any integer
    :precondition: player_health is any integer
    :postcondition: generate a random integer between [1, 5]
    :postcondition: if integer is 1, subtract between [1, MAX_SHIV_DAMAGE] from player_health
    :postcondition: if integer is not 1, return player_health
    :return: player_health minus between [1, MAX_SHIV_DAMAGE] if True, else player_health

    no doctest, this uses random values
    """
    backstab_chance = random.randint(1, 5)
    backstab_damage = random.randint(1, MAX_SHIV_DAMAGE[0])
    if backstab_chance == 1:
        player_health -= backstab_damage
        if player_health > 0:
            print(f"The enemy shot you for {Colours.red}{backstab_damage}{Colours.end} damage as you fled!")
            return player_health
        else:
            player_death_text()
    else:
        print(f"You successfully escape back into darkness of space.")
        return player_health


def combat_initiative_roll(player):  # A
    """Roll to see if player or foe attacks first.

    :precondition: params must be met
    :postcondition: rolls to check if foe attacks first then returns player
    :return: player if foe goes first otherwise nothing
    """
    player_roll = random.randint(1, 100)
    enemy_roll = random.randint(1, 100)
    enemy = make_appropriate_enemy_type(player)
    if player["ship"] == "Thief":
        print(f"The nimbleness of your ship allows you to attack first.\n")
        return True
    if player_roll == enemy_roll:  # checks for draws
        print(f'Draw! You both rolled a {Colours.blue}{player_roll}{Colours.end}. Rerolling....\n')
        combat_initiative_roll(player)
    if player_roll > enemy_roll:  # checks if player attacks first1
        print(f'You rolled a {Colours.blue}{player_roll}{Colours.end} and the enemy '
              f'{Colours.red}{enemy["name"]}{Colours.end} rolled a {Colours.red}{enemy_roll}{Colours.end}. '
              f'You will attack first.\n')
        return True
    elif player_roll < enemy_roll:  # checks if foe attacks first
        print(f'You rolled a {Colours.blue}{player_roll}{Colours.end} and the enemy '
              f'{Colours.red}{enemy["name"]}{Colours.end} rolled {Colours.red}{enemy_roll}{Colours.end}. '
              f'The enemy {Colours.red}{enemy["name"]}{Colours.end} will attack first.\n')
        return False


def combat_player_attack(enemy_health, player):  # A
    """Return enemy's health value after being attacked by player.

    :param enemy_health: a positive integer
    :param player: a dictionary
    :precondition: enemy_health is any positive integer
    :postcondition: subtract a random integer between [1, player["damage"]] from enemy_health
    :postcondition: return enemy_health
    :return: enemy_health

    no doctest, this uses random values
    """
    player_damage = random.randint(1, player["damage"])
    enemy = make_appropriate_enemy_type(player)
    print(f"You did {Colours.blue}{player_damage}{Colours.end} damage to the enemy "
          f"{Colours.red}{enemy['name']}{Colours.end}!\n")
    enemy_health -= player_damage
    time.sleep(1)
    return enemy_health


def combat_enemy_attack(player):  # A
    """Return player's health value after being attacked by enemy.

    :param player: a positive integer
    :precondition: player_health is any positive integer
    :postcondition: subtract a random integer between [1, MAX_ENEMY_DAMAGE] from player_health
    :postcondition: return player_health
    :return: player_health

    no doctest, this uses random values
    """
    time.sleep(1)
    enemy = make_appropriate_enemy_type(player)
    enemy_damage = random.randint(1, enemy['maximum_damage'])
    player['health'] -= enemy_damage
    print(f"The enemy {Colours.red}{enemy['name']}{Colours.end} did {Colours.red}{enemy_damage}{Colours.end} damage to "
          f"you!\n")
    time.sleep(1)
    return player['health']


def combat_enemy_flee():  # A
    """20 percent chance that enemy will flee from combat.

    :return:
    """
    enemy_flee_chance = random.randint(1, 5)
    if enemy_flee_chance == 1:
        return True
    else:
        return False


def combat_choice():  # A
    """Present menu of combat options.

    """
    options = list(enumerate(["Normal Attack", "Special Ability", "Flee"], start=1))
    print(f"You are engaged in a space battle. What will you do next?\n", options)
    return input()


def combat_print_health_values(player, enemy):  # A
    """

    :return:
    """
    time.sleep(1)
    print(f"Your {Colours.blue}{player['player_class']}{Colours.end} can take "
          f"{Colours.blue}{player['health']}{Colours.end} more points of damage.")
    print(f"The enemy {Colours.red}{enemy['name']}{Colours.end} can take "
          f"{Colours.red}{enemy['health']}{Colours.end} more points of damage.\n")


def gain_experience_points(player):  # A
    """Add experience points for player if not max level.

    :param player: must be a dictionary
    :precondition: dictionary must contain keys "exp", "level", "player_class" and "race"
    :postcondition: rolls for experience gain then check
    :return: player if player is not at the max level

    no doctest, this uses random values
    """
    enemy = make_appropriate_enemy_type(player)
    if player["level"] == 3:
        print(f"You are already at the max level of {Colours.blue}3{Colours.end}!\n You did not gain any scrap from the"
              f" battle.")
    else:
        experience_gained = enemy["experience_points"]
        player["exp"] += experience_gained
        print(f"You won the battle! You gained {Colours.blue}{experience_gained}{Colours.end} scrap.")
        level_system(player)
        if player["ship"] == "Magician":
            player["special_action_counter"] += 1
            print(f"You gained a charge on your special attack. You now have a total of "
                  f"{Colours.blue}{player['special_action_counter']}{Colours.end} charge(s).")
        return player


def level_system(player):  # A
    """Level up the player if they reach a certain amount of experience points.

    :param player: must be a dictionary
    :precondition: dictionary must contain keys "exp", "level", "player_class", "damage", "health" and "ship"
    :precondition: dictionary must contain key "special_action_counter" if key "ship" is "Magician"
    :postcondition: calculate if experience requirement met then increases level, damage and health then sets exp to 0
    :postcondition: if experience requirement met and "ship" is "Magician", increment special_action_counter by 1
    :return: player

    >>> level_system({"level": 1, "exp": 250, "damage": 20, "health": 20, "ship": "Warrior", "player_class": "Squire"})
    {'level': 1, 'exp': 250, 'damage': 20, 'health': 20, 'ship': 'Warrior', 'player_class': 'Squire'}
    >>> level_system({"level": 2, "exp": 299, "damage": 22, "health": 25, "ship": "Thief", "player_class": "Banshee"})
    {'level': 2, 'exp': 299, 'damage': 22, 'health': 25, 'ship': 'Thief', 'player_class': 'Banshee'}
    >>> level_system({"level": 1, "exp": 320, "damage": 20, "health": 20, "ship": "Magician", "player_class": "Sapper"\
    , "special_action_counter": 1}) #doctest: +NORMALIZE_WHITESPACE
    You gained a level! You are now level 2 and your ship has been upgrade to a Drainer.
    You also gained another charge on your special attack! You now have a total of 2.
    {'level': 2, 'exp': 0, 'damage': 22, 'health': 25, 'ship': 'Magician', 'player_class': 'Drainer',
    'special_action_counter': 2}
    >>> level_system({"level": 2, "exp": 300, "damage": 22, "health": 25, "ship": "Priest",\
    "player_class": "Archangel"})
    You gained a level! You are now level 3 and your ship has been upgrade to a Seraphim.
    {'level': 3, 'exp': 0, 'damage': 24, 'health': 30, 'ship': 'Priest', 'player_class': 'Seraphim'}
    """
    if player["exp"] >= 300:
        player["level"] += 1
        player["exp"] = 0
        player["damage"] += 2
        player["health"] += 5
        player["maximum_health"] += 5
        class_upgrade(player)
        print(f"You gained a level! You are now level {Colours.blue}{player['level']}{Colours.end} and your ship has "
              f"been upgrade to a {Colours.blue}{player['player_class']}{Colours.end}.")
        if player["ship"] == "Magician":
            player["special_action_counter"] += 1
            print(f"You also gained another charge on your special attack! You now have a total of "
                  f"{Colours.blue}{player['special_action_counter']}{Colours.end}.")
    return player


def class_upgrade(player):  # A
    classes = {'Warrior': {1: "Squire", 2: "Knight", 3: "Phoenix"},
               'Magician': {1: "Sapper", 2: "Drainer", 3: "Charybdis"},
               'Thief': {1: "Ghost", 2: "Banshee", 3: "Revenant"},
               'Priest': {1: "Cherub", 2: "Archangel", 3: "Seraphim"}
               }
    player["player_class"] = classes[player["ship"]][player["level"]]  # finds class based on ship and level
    return player


def spawn_enemy():  # A
    """20 percent chance to return True, else False.

    :postcondition: generate a random integer between [1, 5]
    :postcondition: if integer is 1 return True
    :postcondition: if integer is not 1 return false
    :return: True if integer is 1, else False

    no doctest, this uses random values
    """
    spawn_chance = random.randint(1, 5)
    if spawn_chance == 1:
        return True
    else:
        return False


def game():
    """
    Drive the main gameplay loop as long as goal_achieved is False
    """
    story_introduction_text()
    ascii_intro()

    player = make_player()
    game_board = game_board_coordinates(player['x-coordinate'], player['y-coordinate'])
    player['name'] = input_player_name()
    select_player_class(player)
    achieved_goal = False
    display_game_board(player['x-coordinate'], player['y-coordinate'], game_board)

    while not achieved_goal:
        main_menu_selection = display_main_menu()
        if main_menu_selection == "1":
            direction = cardinal_direction()
            valid_move = validate_move(direction, player['x-coordinate'], player['y-coordinate'])
            if valid_move:
                player['x-coordinate'] = move_x_axis(direction, player['x-coordinate'])
                player['y-coordinate'] = move_y_axis(direction, player['y-coordinate'])
                in_boss_room = check_if_player_in_boss_room(player['x-coordinate'], player['y-coordinate'])
                if not in_boss_room:
                    enemy_encounter = spawn_enemy()
                    if enemy_encounter:
                        enemy = make_appropriate_enemy_type(player)
                        print(f"You were spotted by an enemy {Colours.red}{enemy['name']}{Colours.end}!")
                        initiative = combat_initiative_roll(player)

                        if not initiative:
                            player["health"] = combat_enemy_attack(player)

                        while player["health"] > 0 and enemy["health"] > 0:
                            combat_print_health_values(player, enemy)
                            combat_round_player_choice = combat_choice()
                            if combat_round_player_choice == "1":
                                enemy["health"] = combat_player_attack(enemy["health"], player)
                            elif combat_round_player_choice == "2":
                                if player["ship"] == "Magician" or player["ship"] == "Thief":
                                    enemy["health"] -= special_action_selector(player)
                                elif player["ship"] == "Priest":
                                    special_action_selector(player)
                                elif player["ship"] == "Warrior":
                                    special_action_selector(player)
                                    continue
                            elif combat_round_player_choice == "3":
                                player["health"] = backstab(player["health"])
                                break
                            elif combat_round_player_choice != "1" or combat_round_player_choice != "2" or \
                                    combat_round_player_choice != "3":
                                print(f"That is not a valid choice!")
                                continue
                            if enemy["health"] > 0:
                                enemy_flee_chance = combat_enemy_flee()
                                if enemy_flee_chance:
                                    enemy["health"] = 99999
                                    break
                                elif not enemy_flee_chance:
                                    if enemy["name"] == "Disruptor":
                                        enemy = enemy_disruptor_teleport_attack_countdown(enemy)
                                        player = enemy_disruptor_teleport_attack_activate(enemy, player)
                                    player["health"] = combat_enemy_attack(player)
                                    if player["health"] <= 0 and player["ship"] == "Warrior" and \
                                            player["special_action_counter"] == 1:
                                        resurrect(player)
                        if enemy["health"] <= 0:
                            enemy_death_text(player)
                            gain_experience_points(player)
                            time.sleep(1)
                        elif player["health"] <= 0:
                            player_death_text()
                            exit()
                        elif enemy["health"] == 99999:
                            print(f"The enemy {Colours.red}{enemy['name']}{Colours.end} escaped!")
                            time.sleep(1)
                    else:
                        player['health'] = regen_health(player['health'], player['maximum_health'])
                elif in_boss_room:
                    while player["boss_phase_counter"] > 0:
                        boss = make_appropriate_boss_phase(player)
                        boss_fight_start_text(player)
                        while player["health"] > 0 and boss["health"] > 0:
                            boss_battle_print_health_values(player, boss)
                            combat_round_player_choice = combat_choice()
                            if combat_round_player_choice == "1":
                                boss["health"] = boss_battle_player_attack(boss, player)
                            elif combat_round_player_choice == "2":
                                if player["ship"] == "Magician" or player["ship"] == "Thief":
                                    boss["health"] -= special_action_selector(player)
                                elif player["ship"] == "Priest":
                                    special_action_selector(player)
                                elif player["ship"] == "Warrior":
                                    special_action_selector(player)
                                    continue
                            elif combat_round_player_choice == "3":
                                print(f"There is no escaping the space worm.")
                                continue
                            elif combat_round_player_choice != "1" or combat_round_player_choice != "2" or \
                                    combat_round_player_choice != "3":
                                print(f"That is not a valid choice!")
                                continue
                            if boss["health"] > 0:
                                player["health"] = combat_boss_attack(player)
                                if boss["name"] == "Headless Intergalactic Space Worm":
                                    boss = boss_ultimate_attack_countdown(boss)
                                    player = boss_ultimate_attack_activate(boss, player)
                                if player["health"] <= 0 and player["ship"] == "Warrior" and \
                                        player["special_action_counter"] == 1:
                                    resurrect(player)
                        if boss["health"] <= 0:
                            boss_phase_death_text(player)
                            player["boss_phase_counter"] -= 1
                            time.sleep(1)
                            player["health"] += 20
                            print(f"The space worm's cosmic ichor washes over your {player['player_class']}, repairing "
                                  f"it by 20 points!\n")
                        elif player["health"] <= 0:
                            player_death_text()
                            exit()
                    story_ending_text(player)
                    exit()
                game_board = game_board_coordinates(player['x-coordinate'], player['y-coordinate'])
                display_game_board(player['x-coordinate'], player['y-coordinate'], game_board)
            else:
                print(f"Please move to a different coordinate.")
        elif main_menu_selection == "2":
            check_player_statistics(player)
        elif main_menu_selection == "3":
            print(f"You have abandoned ship! Sector Six has stopped another group of would-be thieves...")
            exit()
        else:
            print(f"That is not a valid choice!\n")


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
