"""
Your student number: Austin He, Caleb Verma
Your student numbers: A00882336, A01257874
"""
import random
import time
import doctest
import itertools

# Constants enclosed in tuples (yes, it looks weird)
MAX_PLAYER_HEALTH = (20,)
MAX_ENEMY_HEALTH = (10,)
REGEN_VALUE = (4,)
MAX_PLAYER_DAMAGE = (20,)
MAX_ENEMY_DAMAGE = (10,)
MAX_SHIV_DAMAGE = (4,)
STARTING_X_COORDINATE = (0,)
STARTING_Y_COORDINATE = (0,)


def check_if_goal_attained(x_coordinate, y_coordinate):
    """Return True if x_coordinate and y_coordinate are both 4, else return False.

    :param x_coordinate: any integer
    :param y_coordinate: any integer
    :precondition: x_coordinate is any integer
    :precondition: y_coordinate is any integer
    :postcondition: return True if x_coordinate and y_coordinate are both 4
    :postcondition: return False if x_coordinate or y_coordinate is not 4
    :return: True if x_coordinate and y_coordinate are both 4, else False

    >>> check_if_goal_attained(4, 4)
    True
    >>> check_if_goal_attained(2, 3)
    False
    >>> check_if_goal_attained(4, 0)
    False
    >>> check_if_goal_attained(0, 4)
    False
    """
    if x_coordinate == 4 and y_coordinate == 4:
        return True
    else:
        return False


def make_player():
    """Return a dictionary representing the player's maximum health health, their starting x-coordinate, and
       their starting y-coordinate.

    :postcondition: Return a dictionary representing the player's maximum health, their starting x-coordinate, and
                    their starting y-coordinate
    :return: a dictionary representing the player's current health, x-coordinate, and y-coordinate

    >>> make_player()
    {'health': 20, 'x-coordinate': 0, 'y-coordinate': 0}
    """
    return {"health": MAX_PLAYER_HEALTH[0], "x-coordinate": STARTING_X_COORDINATE[0], "y-coordinate":
            STARTING_Y_COORDINATE[0]}


def show_map():
    """Print out a 4x4 map of the board.

    :postcondition: generate and prints a board
    :return: prints a map of the game
    >>> show_map()
    [0, 0] [0, 1] [0, 2] [0, 3] [0, 4]
    [1, 0] [1, 1] [1, 2] [1, 3] [1, 4]
    [2, 0] [2, 1] [2, 2] [2, 3] [2, 4]
    [3, 0] [3, 1] [3, 2] [3, 3] [3, 4]
    [4, 0] [4, 1] [4, 2] [4, 3] [4, 4]
    """
    for row in range(5):
        for column in range(5):
            print("[" + str(row) + ", " +
                  str(column) + "]", end=' ')
        print()


def story_introduction():
    """Print the introductory story text.

    :postcondition: print the introductory story text and the map
    """
    pass


def story_ending():
    """Print the ending story text.

    :postcondition: print the ending story text
    """
    pass


def player_death_text():
    """Print text describing player death.

    postcondition: print text describing player death
    """
    pass


def enemy_death_text():
    """Print text describing enemy death.

    postcondition: print text describing enemy death
    """
    pass


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
    :postcondition: return True if direction is 2 and current x_coordinate is not 4
    :postcondition: return True if direction is 3 and current y_coordinate is not 4
    :postcondition: return True if direction is 4 and current x_coordinate is not 0
    :postcondition: return False if any of the above postconditions were not satisfied
    :return: True if direction was a valid move, else False

    >>> validate_move(1, 3, 0)
    False
    >>> validate_move(1, 2, 3)
    True
    >>> validate_move(2, 3, 0)
    True
    >>> validate_move(2, 4, 0)
    False
    >>> validate_move(3, 2, 0)
    True
    >>> validate_move(3, 2, 4)
    False
    >>> validate_move(4, 1, 4)
    True
    >>> validate_move(4, 0, 4)
    False
    """
    if direction == 1 and y_coordinate != 0:
        return True
    elif direction == 2 and x_coordinate != 4:
        return True
    elif direction == 3 and y_coordinate != 4:
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
            print(f"The guard stabs you in the back for {backstab_damage} damage as you flee!")
            return player_health
        else:
            player_death_text()
            exit()
    else:
        print("You successfully escape back into the shadows.")
        return player_health


def combat_initiative_roll():  # put enemy_name as a parameter maybe; could have different names for diff enemy types
    """Roll to see if character or foe attacks first.

    :precondition: params must be met
    :postcondition: rolls to check if foe attacks first then returns character
    :return: character if foe goes first otherwise nothing
    """
    player_roll = random.randint(1, 100)
    enemy_roll = random.randint(1, 100)
    enemy = "enemy_name"
    # why use a while loop instead of an if statement?
    while player_roll == enemy_roll:  # checks for draws
        print(f'Draw! You both rolled a {player_roll}. Rerolling....')
        combat_initiative_roll()
    if player_roll > enemy_roll:  # checks if player attacks first
        print(f'You rolled a {player_roll} and {enemy} rolled a {enemy_roll}. You will attack first.')
        return True
    elif player_roll < enemy_roll:  # checks if foe attacks first
        print(f'You rolled a {player_roll} and {enemy} rolled {enemy_roll}. {enemy} will attack first.')
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
    time.sleep(1)
    player_damage = random.randint(1, MAX_PLAYER_DAMAGE[0])
    print(f"You did {player_damage} damage to the guard!")
    enemy_health -= player_damage
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
    print(f"The guard did {enemy_damage} damage to you!")
    return player_health


def gain_experience_points():
    """Return player's health value after being attacked by enemy.

    :param
    :precondition:
    :postcondition:
    :return:
    """

    """ Your gain_experience function was part of the combat_round function; could you redesign to make it a stand alone 
        function that returns exp gain? Then we can add it to character[exp]. Maybe even make level_up another function.
    
    character["experience"] += 100  # gains 100 experience for each foe killed.
    print(f'\nYou won the battle! You gained 100 experience.'
          f' You now have a total of {character["experience"]} experience points.')
    if character["experience"] % 500 == 0:  # levels up user every 500 experience points
        character["level"] += 1
        print(f'You have leveled up! You are now level {character["level"]} and can deal an extra 2 damage.')
    return character
    """


def combat_duel(player_health):
    """Return player's health value after enemy_health or player_health reaches 0.

    :param player_health: a positive integer
    :precondition: player_health is any positive integer
    :postcondition: take turns subtracting a random integer between [1, MAX_PLAYER_DAMAGE] from enemy_health and a
                    random integer [1, MAX_ENEMY_DAMAGE] from player_health until player_health or enemy_health == 0
    :postcondition: return player_health value after enemy_health or player_health == 0
    :return: player_health after enemy_health or player_health reaches 0

    no doctest, this uses random values
    """
    enemy_health = MAX_ENEMY_HEALTH[0]
    initiative = combat_initiative_roll()

    if initiative:
        while player_health > 0 and enemy_health > 0:
            enemy_health = combat_player_attack(enemy_health)
            if enemy_health > 0:
                player_health = combat_enemy_attack(player_health)
    elif not initiative:
        while player_health > 0 and enemy_health > 0:
            player_health = combat_enemy_attack(player_health)
            if enemy_health > 0:
                enemy_health = combat_player_attack(enemy_health)

    if enemy_health <= 0:
        enemy_death_text()
        return player_health
    else:
        player_death_text()
        exit()


def combat_choice(player_health):
    """Call combat_duel() or backstab(), or recall combat_choice, depending on player choice.

    :param player_health: any integer
    :precondition: player_health is any integer
    :postcondition: display a list of combat choices
    :postcondition: convert input to integer
    :postcondition: if input is 1, call combat_duel(player_health)
    :postcondition: if input is 2, call backstab(player_health)
    :postcondition: if input is neither 1 or 2, recall combat_choice()
    :return: combat_duel(player_health) if input == 1; backstab(player_health) if input == 2; combat_choice() is input
             != 1 or input != 2

    no doctest, this accepts user input
    """
    options = list(enumerate(["Fight", "Flee"], start=1))
    print("Enter 1 to engage in combat, or enter 2 if you try to flee.\n", options)
    choice = input()
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            return combat_duel(player_health)
        elif choice == 2:
            return backstab(player_health)
        else:
            print("That is not a valid choice!")
            return combat_choice(player_health)
    else:
        print("That is not a valid choice!")
        return combat_choice(player_health)


def spawn_enemy():
    """40 percent chance to return True, else False.

    :postcondition: generate a random integer between [1, 5]
    :postcondition: if integer is 1 or 2, return True
    :postcondition: if integer is not 1 or 2, return false
    :return: True if integer is 1 or 2, else False

    no doctest, this uses random values
    """
    spawn_chance = random.randint(1, 5)
    if spawn_chance == 1 or spawn_chance == 2:
        print("You were spotted by a guard!")
        return True
    else:
        return False


def game():
    """
    Drive the main gameplay loop as long as goal_achieved is False
    """
    player = make_player()
    achieved_goal = False
    story_introduction()

    while not achieved_goal:
        print(f"You are currently at ({player['x-coordinate']}, {player['y-coordinate']}).")
        print(f"You have {player['health']} health points remaining.\n")
        direction = cardinal_direction()
        valid_move = validate_move(direction, player['x-coordinate'], player['y-coordinate'])
        if valid_move:
            player['x-coordinate'] = move_x_axis(direction, player['x-coordinate'])
            player['y-coordinate'] = move_y_axis(direction, player['y-coordinate'])
            achieved_goal = check_if_goal_attained(player['x-coordinate'], player['y-coordinate'])
            if not achieved_goal:
                enemy_encounter = spawn_enemy()
                if enemy_encounter:
                    player['health'] = combat_choice(player['health'])
                else:
                    player['health'] = regen_health(player['health'])
        else:
            print("That's not a valid move!")
    story_ending()


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
