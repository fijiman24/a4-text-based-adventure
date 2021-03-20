def make_player():
    """Return a dictionary representing the player's maximum health health, their starting x-coordinate, their starting
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
            "name": "test",
            "exp": 0,
            "level": 1,
            "player_race": "placeholder_class",
            "player_class": "placeholder_class",
            "player_class_special_action": "placeholder_class_special_action",
            "damage_multiplier": 1,
            "flee_chance_multiplier": 1
            }

def select_player_class(player):
    class_choices = list(enumerate(["Careless Adventurer", "Corrupt Official", "Petty Thief", "Vengeful Barbarian"],
                                   start=1))
    print("Select a class: ")
    print(class_choices)
    choice = input()
    if choice == "1":
        # print the backstory of class 1
        if confirm_player_class("Careless Adventurer", player):
            warrior_ship(player)
    elif choice == "2":
        # print the backstory of class 1
        if confirm_player_class("Corrupt Official", player):
            magician_ship(player)
    elif choice == "3":
        # print the backstory of class 1
        if confirm_player_class("Petty Thief", player):
            thief_ship(player)
    elif choice == "4":
        # print the backstory of class 1
        if confirm_player_class("Vengeful Barbarian", player):
            priest_ship(player)
    else:
        print("That is not a valid choice! \n")
        select_player_class()
    return player


def confirm_player_class(class_name, player):
    print(f"Do you want to be a {class_name}?")
    print(list(enumerate(["Yes", "No"], start=1)))

    choice = input()
    if choice == "1":
        return True
    elif choice == "2":
        select_player_class(player)
    else:
        print("That is not a valid choice! \n")
        confirm_player_class(class_name, player)


def thief_ship(player):
    player["ship"] = "Thief"
    player["class"] = "Banshee"
    player["player_class_special_action"] = multi_attack(player)
    player["damage"] = 20
    player["damage_multiplier"] = 1
    player["flee_chance_multiplier"] = 5

    return player


def magician_ship(player):
    player["ship"] = "Magician"
    player["class"] = ""
    player["player_class_special_action"] = magic_blast(player)
    player["special_action_counter"] = 1
    player["damage"] = 20
    player["damage_multiplier"] = .7
    player["flee_chance_multiplier"] = 1
    return player


def warrior_ship(player):
    player["ship"] = "Warrior"
    player["class"] = "Viking"
    player["player_class_special_action"] = resurrect(player)
    player["special_action_counter"] = 1
    player["damage"] = 20
    player["damage_multiplier"] = 1.3
    player["flee_chance_multiplier"] = 1
    return player


def priest_ship(player):
    player["ship"] = "Priest"
    player["class"] = "Archangel"
    player["player_class_special_action"] = heal_spell(player)
    player["damage"] = 20
    player["damage_multiplier"] = 1
    player["flee_chance_multiplier"] = 1
    player["health_restored"] = 1.3
    return player


def magic_blast(player):
    if player["special_action_counter"] == 1:
        player["special_action_counter"] = 0
        return player["damage"] * player["level"] * 2
    else:
        print("You have already used your special move!")


def heal_spell(player):
    amount_healed = player["level"] * 10
    player["hp"] += amount_healed
    return player


def multi_attack(player):
    split_attack = int(round(player["damage"] / 5))
    return split_attack * 5 * player["level"] * 1.2


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
