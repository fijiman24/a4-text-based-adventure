"""
Game logic for the Coordinate Game.
"""
curr_coords = [0, 0]
goal_corrds = (10, 10)


def game(direction=None):
    """
    Update game state based on user input.
    """
    global curr_coords
    error_message = None
    game_over = False
    if direction is not None:
        if direction in ["north", "east", "south", "west"]:
            if direction == "north":
                curr_coords[0] += 1
            elif direction == "east":
                curr_coords[1] += 1
            elif direction == "south":
                curr_coords[0] -= 1
            elif direction == "west":
                curr_coords[1] -= 1
        else:
            error_message = "Invalid direction. Please try again."
    if curr_coords == list(goal_corrds):
        print("Congratulations! You have reached the goal.")
        game_over = True
    return curr_coords, goal_corrds, error_message, game_over
