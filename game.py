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
MAX_PLAYER_HEALTH = (20,)
MAX_ENEMY_HEALTH = (10,)
REGEN_VALUE = (4,)
MAX_PLAYER_DAMAGE = (20,)
MAX_ENEMY_DAMAGE = (10,)
MAX_SHIV_DAMAGE = (4,)
STARTING_X_COORDINATE = (0,)
STARTING_Y_COORDINATE = (0,)


def ascii_intro():
    """Print ascii art of game title.

    :postcondition: print ascii art of game title

    >>> ascii_intro()

    """
    print(f"{Colours.yellow}  /$$$$$$                        /$$                                /$$$$$$  /$$          ")
    print(" /$$__  $$                      | $$                               /$$__  $$|__/          ")
    print("| $$  \__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$   /$$")
    print("|  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/")
    print(" \____  $$| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/       \____  $$| $$ \  $$$$/ ")
    print(f" /$$  \ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \ $$| $$  >$$  $$ ")
    print(f"|  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\  $$")
    print(f" \______/  \_______/ \_______/   \___/   \______/ |__/             \______/ |__/|__/  \__/\n{Colours.end}")


def story_introduction():
    """Print the introductory story text.

    :postcondition: print the introductory story text

    >>> story_introduction()
    In the distant future, humankind has colonized the vast, cold reaches of space. From suburban planets to entire solar systems dedicated to vice, there isn't a sector in the
    Milky Way Galaxy that's been left untouched by our ever-expanding race. One such sector is devoted to storing all of humanity's physical wealth and fortune. Many a space
    pirate has tried their hand at laying siege to this sector in hopes of plundering some riches for themselves, and all have been gunned down by the local security militias.
    <BLANKLINE>
    All except you. You put together a ragtag crew, formulated the perfect plan, and somehow managed to fill your ship with as much stolen loot as she could carry. Now all you
    have to do is escape to the nearest wormhole, treasure in tow, and you'll be christened the first ever space captain to have successfully pilfered from...
    <BLANKLINE>
    """
    print("In the distant future, humankind has colonized the vast, cold reaches of space. From suburban planets "
          "to entire solar systems dedicated to vice, there isn't a sector in the\nMilky Way Galaxy that's been "
          "left untouched by our ever-expanding race. One such sector is devoted to storing all of humanity's physical "
          "wealth and fortune. Many a space\npirate has tried their hand at laying siege to this sector in hopes of "
          "plundering some riches for themselves, and all have been gunned down by the local security militias. \n")
    print("All except you. You put together a ragtag crew, formulated the perfect plan, and somehow managed to fill "
          "your ship with as much stolen loot as she could carry. Now all you\nhave to do is escape to the nearest "
          "wormhole, treasure in tow, and you'll be christened the first ever space captain to have successfully "
          "pilfered from...\n")


def story_ending():
    """Print the ending story text.

    :postcondition: print the ending story text
    """
    pass


def player_death():
    """Print text describing player death.

    postcondition: print text describing player death
    """
    print("You died.")
    exit()


def enemy_death():
    """Print text describing enemy death.

    postcondition: print text describing enemy death
    """
    print("The enemy died.")
    time.sleep(2)


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


def check_if_goal_attained(boss_health):
    """Return True if boss_health <= 0, else return False.

    """
    pass


def make_player():
    """Return a dictionary representing the player's maximum health, their starting x-coordinate, their starting
       y-coordinate, and their name.

    :postcondition: Return a dictionary representing the player's maximum health, their starting x-coordinate, their
                    starting y-coordinate, and their name
    :return: a dictionary representing the player's current health, starting x-coordinate and y-coordinate, and name

    >>> make_player()
    {'health': 20, 'x-coordinate': 0, 'y-coordinate': 0, 'name': ''}
    """
    return {"health": MAX_PLAYER_HEALTH[0],
            "x-coordinate": STARTING_X_COORDINATE[0],
            "y-coordinate": STARTING_Y_COORDINATE[0],
            "name": None,
            "exp": 0,
            "ship": None,
            "player_class": None,
            "player_class_special_action": None,
            "special_action_counter": 0,
            "level": 1,
            "damage": 20,
            "damage_multiplier": 1,
            "flee_chance_multiplier": 1
            }


def input_player_name():
    """Return player name.

    :postcondition: convert player's input into title case
    :return: player name

    no doctests, accepts user input
    """
    name_input = str(input("Enter your name, captain: ")).title()
    if name_input.lower() == "chris" or name_input.lower() == "christopher" or name_input.lower() == "chris thompson":
        print("You can be more adventurous than that! \n")
        return input_player_name()
    elif name_input.strip() == "":
        print("Every space captain needs a name! \n")
        return input_player_name()
    else:
        return name_input


def select_player_class(player):
    """Print class description and return class after being passed to confirm_player_class().

    :precondition: user enters input when prompted
    :postcondition: print numbered list of class options [(1, 'Dreadnought'), (2, 'Sapper'), (3, 'Ghost'),
                    (4, 'Cherub')]
    :postcondition: print class description
    :postcondition: pass user input to confirm_player_class()
    :return: class after being passed to confirm_player_class()
    """
    class_choices = list(enumerate(["Dreadnought", "Sapper", "Ghost", "Cherub"], start=1))
    print("Select a spaceship: \n", class_choices)
    choice = input()
    if choice == "1":
        print("A Phoenix Engine™ allows for this ship to repair itself after its hull integrity has been completely "
              "breached for the first time.")
        if confirm_player_class("Dreadnought", player):
            warrior_ship(player)
    elif choice == "2":
        print("Destroy enemy ships to steal their energy and charge up your Quasar Cannon™ for a devastating attack.")
        if confirm_player_class("Sapper", player):
            magician_ship(player)
    elif choice == "3":
        print("A stealthy ship covered in SlipStream™ camouflage technology for easier evasion from enemies.")
        if confirm_player_class("Ghost", player):
            thief_ship(player)
    elif choice == "4":
        print("QuickFix™ Protocols allows this ship to repair itself during combat.")
        if confirm_player_class("Cherub", player):
            priest_ship(player)
    else:
        print("That is not a valid choice! \n")
        select_player_class(player)
    return player

def confirm_player_class(class_name, player):
    """Return class_name or call select_player_class, depending on user input.

    :param class_name: any string
    :precondition: class_name is any string representing the selected player class
    :precondition: user enters input when prompted
    :postcondition: print f"Do you pilot a {class_name}?"
    :postcondition: print a numbered list of options [(1, 'Yes'), (2, 'No')]
    :postcondition: return class_name if input is "1"
    :postcondition: call select_player_class() if input is "2"
    :postcondition: print "That is not a valid choice" if input is neither "1" or "2" and recall confirm_player_class()
    :return: class_name if input is "1", select_player_class() if input is "2"
    """
    print(f"Do you pilot a {class_name}?")
    print(list(enumerate(["Yes", "No"], start=1)))

    choice = input()
    if choice == "1":
        return True
    elif choice == "2":
        return select_player_class(player)
    else:
        print("That is not a valid choice! \n")
        confirm_player_class(class_name, player)


def warrior_ship(player):
    player["ship"] = "Warrior"
    player["player_class"] = "Dreadnought"
    player["player_class_special_action"] = resurrect(player)
    player["special_action_counter"] = 1
    player["damage"] = 20
    player["damage_multiplier"] = 1.3
    player["flee_chance_multiplier"] = 1
    return player


def magician_ship(player):
    player["ship"] = "Magician"
    player["player_class"] = "Sapper"
    player["player_class_special_action"] = magic_blast(player)
    player["special_action_counter"] = 1
    player["damage"] = 20
    player["damage_multiplier"] = .7
    player["flee_chance_multiplier"] = 1
    return player


def thief_ship(player):
    player["ship"] = "Thief"
    player["player_class"] = "Ghost"
    player["player_class_special_action"] = multi_attack(player)
    player["damage"] = 20
    player["damage_multiplier"] = 1
    player["flee_chance_multiplier"] = 5
    return player


def priest_ship(player):
    player["ship"] = "Priest"
    player["player_class"] = "Cherub"
    player["player_class_special_action"] = heal_spell(player)
    player["damage"] = 20
    player["damage_multiplier"] = 1
    player["flee_chance_multiplier"] = 1
    player["health_restored"] = 1.3
    return player


def resurrect(player):
    if player["special_action_counter"] == 1:
        if player["hp"] >= 0:
            player["special_action_counter"] = 0
            print("Your undying will allowed you to survive the attack and restored your health to 50!")
            player["hp"] = 50
            return player
        else:
            print("Your passive will allow you to survive a critical attack.")
    else:
        print("Your passive have already been used. You will not revive if your hp hits 0.")


def magic_blast(player):
    if player["special_action_counter"] == 1:
        player["special_action_counter"] = 0
        return player["damage"] * player["level"] * 2
    else:
        print("You have already used your special move!")


def multi_attack(player):
    split_attack = int(round(player["damage"] / 5))
    return split_attack * 5 * player["level"] * 1.2


def heal_spell(player):
    amount_healed = player["level"] * 10
    player["health"] += amount_healed
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
    print(f"You are Captain {player['name']}.")
    print(f"{player['name']} pilots a {player['player_class']}, which has the special ability "
          f"{player['player_class_special_action']}.")
    print(f"Your {player['player_class']} can take {player['health']} more points of damage.")
    print(f"Your {player['player_class']} is level {player['level']}.")
    print(f"You have {player['exp']} scrap, {500 - int(player['exp'])} scrap away from a ship upgrade.\n")


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
    print("Please enter a number corresponding to the direction you wish to move in.")
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
    if direction == 1 and y_coordinate != 0:
        return True
    elif direction == 2 and x_coordinate != 24:
        return True
    elif direction == 3 and y_coordinate != 24:
        return True
    elif direction == 4 and x_coordinate != 0:
        return True
    else:
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


def regen_health(player_health):
    """Add REGEN_VALUE to current_health if current_health <= MAX_PLAYER_HEALTH, else return MAX_PLAYER_HEALTH.

    :param player_health: any integer
    :precondition: player_health is any integer
    :postcondition: add REGEN_VALUE to player_health if player_health <= MAX_PLAYER_HEALTH after adding REGEN_VALUE
    :postcondition: make player_health = MAX_PLAYER_HEALTH if adding REGEN_VALUE to player_health would make it >
                    MAX_PLAYER_HEALTH
    :return: player_health plus REGEN_VALUE if player_health <= MAX_PLAYER_HEALTH, else MAX_PLAYER_HEALTH

    >>> regen_health(-1)
    You regained 4 health points!
    3
    >>> regen_health(14)
    You regained 4 health points!
    18
    >>> regen_health(19)
    You regained all of your health!
    20
    >>> regen_health(20)
    20
    """
    if player_health <= (MAX_PLAYER_HEALTH[0] - REGEN_VALUE[0]):
        print(f"You regained {REGEN_VALUE[0]} health points!")
        return player_health + REGEN_VALUE[0]
    elif MAX_PLAYER_HEALTH[0] > player_health > (MAX_PLAYER_HEALTH[0] - REGEN_VALUE[0]):
        print("You regained all of your health!")
        return MAX_PLAYER_HEALTH[0]
    else:
        return player_health


def backstab(player_health):
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
            print(f"The enemy shot you for {backstab_damage} damage as you fled!")
            return player_health
        else:
            player_death()
    else:
        print("You successfully escape back into darkness of space.")
        return player_health


def combat_initiative_roll():  # put enemy_name as a parameter maybe; could have different names for diff enemy types
    """Roll to see if player or foe attacks first.

    :precondition: params must be met
    :postcondition: rolls to check if foe attacks first then returns player
    :return: player if foe goes first otherwise nothing
    """
    player_roll = random.randint(1, 100)
    enemy_roll = random.randint(1, 100)
    enemy = "enemy_name"
    if player_roll == enemy_roll:  # checks for draws
        print(f'Draw! You both rolled a {player_roll}. Rerolling....\n')
        combat_initiative_roll()
    if player_roll > enemy_roll:  # checks if player attacks first
        print(f'You rolled a {player_roll} and {enemy} rolled a {enemy_roll}. You will attack first.\n')
        return True
    elif player_roll < enemy_roll:  # checks if foe attacks first
        print(f'You rolled a {player_roll} and {enemy} rolled {enemy_roll}. {enemy} will attack first.\n')
        return False


def combat_player_attack(enemy_health):
    """Return enemy's health value after being attacked by player.

        :param enemy_health: a positive integer
        :precondition: enemy_health is any positive integer
        :postcondition: subtract a random integer between [1, MAX_PLAYER_DAMAGE] from enemy_health
        :postcondition: return enemy_health
        :return: enemy_health

        no doctest, this uses random values
        """
    player_damage = random.randint(1, MAX_PLAYER_DAMAGE[0])
    print(f"You did {player_damage} damage to the enemy ship!\n")
    enemy_health -= player_damage
    time.sleep(1)
    return enemy_health


def combat_enemy_attack(player_health):
    """Return player's health value after being attacked by enemy.

        :param player_health: a positive integer
        :precondition: player_health is any positive integer
        :postcondition: subtract a random integer between [1, MAX_ENEMY_DAMAGE] from player_health
        :postcondition: return player_health
        :return: player_health

        no doctest, this uses random values
        """
    time.sleep(1)
    enemy_damage = random.randint(1, MAX_ENEMY_DAMAGE[0])
    player_health -= enemy_damage
    print(f"The enemy ship did {enemy_damage} damage to you!\n")
    time.sleep(1)
    return player_health


def combat_enemy_flee():
    """20 percent chance that enemy will flee from combat.

    :return:
    """
    enemy_flee_chance = random.randint(1, 5)
    if enemy_flee_chance == 1:
        return True
    else:
        return False


def combat_choice():
    """Present menu of combat options.

    """
    options = list(enumerate(["Normal Attack", "Special Ability", "Flee"], start=1))
    print("You are engaged in a space battle. What will you do next?\n", options)
    return input()


def combat_duel(player):
    """Return player's health value after enemy_health or player_health reaches 0.

    :param player: a dictionary
    :precondition: player must contain keys "level", "health", and "exp"
    :postcondition: take turns subtracting a random integer between [1, MAX_PLAYER_DAMAGE] from enemy_health and a
                    random integer [1, MAX_ENEMY_DAMAGE] from player_health until player["health"] or enemy_health == 0
    :postcondition: return player["health"] value after enemy_health or player["health"] == 0
    :return: player["health"] after enemy_health or player["health"] reaches 0

    no doctest, this uses random values
    """
    enemy_health = MAX_ENEMY_HEALTH[0]
    initiative = combat_initiative_roll()

    if not initiative:
        player["health"] = combat_enemy_attack(player["health"])

    while player["health"] > 0 and enemy_health > 0:
        print(f"Your ship can take {player['health']} more points of damage.")
        combat_round_player_choice = combat_choice()
        if combat_round_player_choice == "1":
            enemy_health = combat_player_attack(enemy_health)
        elif combat_round_player_choice == "2":
            print("Special abilities are not available yet, check back later!\n")
            continue
        elif combat_round_player_choice == "3":
            player["health"] = backstab(player["health"])
            break
        elif combat_round_player_choice != "1" or combat_round_player_choice != "2" or combat_round_player_choice != \
                "3":
            print("That is not a valid choice!")
            continue
        if enemy_health > 0:
            enemy_flee_chance = combat_enemy_flee()
            if enemy_flee_chance:
                enemy_health = 99999
                break
            elif not enemy_flee_chance:
                player["health"] = combat_enemy_attack(player["health"])

    if enemy_health <= 0:
        enemy_death()
        gain_experience_points(player)
        time.sleep(1)
    elif player["health"] <= 0:
        player_death()
    elif enemy_health == 99999:
        print("The enemy escaped!")
        time.sleep(1)
        return player["health"]
    else:
        return player["health"]


def gain_experience_points(player):
    """Add experience points for player if not max level.

    :param player: must be a dictionary
    :precondition: dictionary must contain keys "exp", "level", "player_class" and "race"
    :postcondition: rolls for experience gain then check
    :return: player if player is not at the max level

    no doctest, this uses random values
    """
    if player["level"] == 3:
        print(f"You are already at the max level of 3!\n You did not gain any experience from the battle.")
    else:
        experience_gained = random.randint(50, 150)
        player["exp"] += experience_gained
        print(f"You won the battle! You gained {experience_gained} experience points.")
        level_system(player)
        return player


def level_system(player):
    """Level up the player if they reach a certain amount of experience points.

    :param player: must be a dictionary
    :precondition: dictionary must contain keys "exp", "level", "player_class" and "race"
    :postcondition: calculate if experience requirement met then increases level by 1 and sets experience to 0
    :return: player

    >>> level_system({"level": 1, "experience": 250, "race": "warrior", "player_class": "Pawn"})
    {'level': 1, 'experience': 250, 'race': 'warrior', 'class': 'Pawn'}
    >>> level_system({"level": 2, "experience": 299, "race": "bandit", "player_class": "Jester"})
    {'level': 2, 'experience': 299, 'race': 'bandit', 'class': 'Jester'}
    >>> level_system({"level": 1, "experience": 320, "race": "mage", "player_class": "Pawn"})
    You gained a level! You are now level 2 and ascended to a Rook.
    {'level': 2, 'experience': 0, 'race': 'mage', 'class': 'Rook'}
    >>> level_system({"level": 2, "experience": 300, "race": "archer", "player_class": "Pawn"})
    You gained a level! You are now level 3 and ascended to a King.
    {'level': 3, 'experience': 0, 'race': 'archer', 'class': 'King'}
    """
    if player["exp"] >= 300:
        player["level"] += 1
        player["exp"] = 0
        class_upgrade(player)
        print(f"You gained a level! You are now level {player['level']} and your ship has been upgrade to a"
              f" {player['player_class']}.")
    return player


def class_upgrade(player):
    classes = {'Warrior': {1: "Dreadnought", 2: "Knight", 3: "Queen"},
               'Magician': {1: "Sapper", 2: "Rook", 3: "Bishop"},
               'Thief': {1: "Ghost", 2: "Hunter", 3: "King"},
               'Priest': {1: "Cherub", 2: "Jester", 3: "Castle"}
               }

    player["player_class"] = classes[player["ship"]][player["level"]]  # finds class based on ship and level

    return player


def spawn_enemy():
    """20 percent chance to return True, else False.

    :postcondition: generate a random integer between [1, 5]
    :postcondition: if integer is 1 return True
    :postcondition: if integer is not 1 return false
    :return: True if integer is 1, else False

    no doctest, this uses random values
    """
    spawn_chance = random.randint(1, 5)
    if spawn_chance == 1:
        print("You were spotted by a militia ship!")
        return True
    else:
        return False


def game():
    """
    Drive the main gameplay loop as long as goal_achieved is False
    """
    story_introduction()
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
                        combat_duel(player)
                    else:
                        player['health'] = regen_health(player['health'])
                game_board = game_board_coordinates(player['x-coordinate'], player['y-coordinate'])
                display_game_board(player['x-coordinate'], player['y-coordinate'], game_board)
            else:
                print("That's not a valid move!")
        elif main_menu_selection == "2":
            check_player_statistics(player)
        elif main_menu_selection == "3":
            print("You have abandoned ship! Sector Six has stopped another group of would-be thieves...")
            exit()
        else:
            print("That is not a valid choice!\n")


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
