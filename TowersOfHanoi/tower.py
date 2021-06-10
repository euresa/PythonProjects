"""
Towers of Hanoi Game, by Sam Eure, eure.samuel@gmail.com
A basic stacking puzzle. (June 8, 2021)
"""


# Game Parameters
NUMBER_OF_BLOCKS = 5  # More blocks -> more challenging
NUMBER_OF_TOWERS = 3


# Functions
def initialize_game():
    """Creates a configuration of the game with respect to the number
    of poles in the game, block in the game, and their initial placements on
    the first tower. Also determined what constitute possible moves given
    the number of poles in the game.
    """

    initialize_grid()
    create_letters_and_blocks()
    find_possible_moves()


def find_possible_moves():
    """Determines possible moves from one tower to another (i.e. pairs of towers)
    Saves these moves as a global variable for other functions to access.
    """

    global possible_moves
    possible_moves = []
    # Find all pairs of poles
    for start in letter_to_blocks.keys():
        for end in letter_to_blocks.keys():
            if start != end:
                possible_moves.append(start + end)


def initialize_grid():
    """Creates a grid where the string characters of blocks and poles can be stores
    before printing them out as a single string.
    Creates a global list variable 'grid' for other functions to reference.
    """

    display_height = NUMBER_OF_BLOCKS + 2  # +2 for an extra space on the top and bottom
    global grid
    grid = [list(" " * NUMBER_OF_TOWERS) for row in range(display_height)]


def create_letters_and_blocks():
    """Holds the core configuration of the game.
    Maps the identifier (i.e. A, B, C, ...) of each pole to the blocks on the pole.
    Creates the global dictionary variable 'letter_to_blocks' for other functions to access.
    """

    global letter_to_blocks
    letter_to_blocks = {}
    for i in range(NUMBER_OF_TOWERS):
        letter_to_blocks[get_letter_from_index(i)] = []
    # Begin the game with all the blocks on the first pole
    first_pole = get_letter_from_index(0)
    # Reverse the order of blocks so the last/smallest block can be popped off later
    letter_to_blocks[first_pole] = list(range(NUMBER_OF_BLOCKS, 0, -1))


def get_letter_from_index(i):
    """Returns 'A' for 1, 'B' for 2, 'C' for 3, ... etc."""

    return chr(i + 65)


def add_letter_to_grid(i):
    """Populates the bottom of the grid with letters A, B, C, ... etc."""

    letter = get_letter_from_index(i)
    letter_string = create_letter_string(letter)
    grid[-1][i] = letter_string


def create_letter_string(letter):
    """Ensures that the letters are padded with enough white space
    in order to properly print them out underneath the towers."""

    border_string = " " * NUMBER_OF_BLOCKS
    return "".join([border_string, " ", letter, border_string])


def populate_grid():
    """Populates the grid of characters with strings of letter, blocks, and poles"""

    for i in range(NUMBER_OF_TOWERS):
        add_letter_to_grid(i)
        stack_blocks_on_letter(i)


def stack_blocks_on_letter(i):
    """Populates the grid with the blocks currently on the i_th tower."""

    letter = get_letter_from_index(i)
    # Obtain the list of blocks for the i_th tower
    blocks = letter_to_blocks[letter]
    for j, block in enumerate(blocks):
        block_string = get_block_string(block)
        # Stack blocks in reverse order so that vacant blocks are replaced by poles
        grid[-2 - j][
            i
        ] = block_string  # -2 so that we skip over the string letter under the pole

    rows_without_blocks = (
        NUMBER_OF_BLOCKS - len(blocks) + 1
    )  # +1 to always have the top row showing pole
    for row in range(rows_without_blocks):
        grid[row][i] = " " * NUMBER_OF_BLOCKS + "||" + " " * NUMBER_OF_BLOCKS


def get_block_string(block):
    """Creates the strings representing the block and
    ensures the blocks are padded with sufficient white space
    to properly print them as a pyramid on top of the letters.
    """

    border_str = " " * (NUMBER_OF_BLOCKS - block)
    block_str = "@" * block
    return "".join([border_str, block_str, "_", str(block), block_str, border_str])


def show_grid():
    """Prints the contents of the grid."""

    for row in grid:
        print("".join(row))


def display():
    """Organize the current configuration of blocks and towers on a grid and print this grid."""

    populate_grid()
    show_grid()


def make_next_move():
    """Obtains the next move from the player. Returns True if the player is
    continuing to play the game and returns False if the player wishes to quit.
    """

    # Proactively obtains the list of valid moves from the player
    valid_moves = [m for m in possible_moves if check_if_move_is_valid(m)]
    print("Enter Move: (e.g. AB, BC, CA, etc.)")
    proposed_move = input("> ").upper()
    while (
        proposed_move not in valid_moves
    ):  # Continue to ask for moves until the player provides a valid move.
        print("Invalid move entered. Please enter a valid move or type quit.")
        print("Valid Moves:", valid_moves)
        proposed_move = input("> ").upper()
        if proposed_move == "QUIT":
            return False

    # Configure the blocks to represent the desired move from the player
    make_move(proposed_move)
    return True


def check_if_move_is_valid(proposed_move):
    """Ensures the player has provided a valid move given the rules of the game.
    Returns True for a valid move and False for an invalid move.
    """

    if proposed_move not in possible_moves:
        return False
    start_blocks = letter_to_blocks[proposed_move[0]]
    end_blocks = letter_to_blocks[proposed_move[1]]

    # The tower a block is being taken from must have a block available to move.
    if len(start_blocks) == 0:
        return False
    # Any block may be placed on an empty tower
    elif len(end_blocks) == 0:
        return True
    # Ensure the block being moved from the first tower isn't larger than the top block on the second tower.
    elif start_blocks[-1] > end_blocks[-1]:
        return False
    else:
        return True


def make_move(proposed_move):
    """Configures letter_to_blocks to reflect the proposed move."""

    start_blocks = letter_to_blocks[proposed_move[0]]
    end_blocks = letter_to_blocks[proposed_move[1]]
    block_to_move = start_blocks.pop()
    end_blocks.append(block_to_move)


def player_has_won():
    """Checks to see if all the blocks are on a different tower from the initial tower.
    Returns True and prints a message if the player has won. Otherwise, it returns False.
    """

    for letter in letter_to_blocks:
        if letter != get_letter_from_index(0):
            if len(letter_to_blocks[letter]) == NUMBER_OF_BLOCKS:
                print((chr(127882) + chr(127881)) * 15)  # A fancy banner
                print("Congratulations!")
                return True
    return False


def main():
    """Runs a single game of Towers of Hanoi."""

    POINT = chr(10012)  # Cool bullet point for the game initialization
    print(
        f"""
{'='*65}
    Welcome to Towers of Hanoi!

{POINT} Objective: Move the pyramid of blocks from one pole to another.

Rules: 
{POINT} You must move one block at a time
{POINT} Larger blocks may not be placed on top of smaller blocks
    """
    )

    # Game Set-Up
    initialize_game()

    # Game Play
    game_active = True
    while game_active:  # Make a new move on each iteration of the loop
        # Show the current configuration of blocks to the player
        display()
        # Obtain the next move from the user, including quitting the game
        game_active = make_next_move()
        # Check if the current configuration of blocks signifies victory
        if player_has_won():
            display()
            break

    # Farewell Message
    print("Thanks for playing!")


# Begin program if run directly
if __name__ == "__main__":
    main()
