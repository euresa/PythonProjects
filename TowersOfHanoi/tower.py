"""
Towers of Hanoi Game
Author: Sam Eure
Date: June 8, 2021
"""


# Game Parameters
NUMBER_OF_BLOCKS = 5
NUMBER_OF_TOWERS = 3



# Functions
def initialize_game():
    initialize_grid()
    calculate_string_length()
    create_letters_and_blocks()
    find_possible_moves()


def find_possible_moves():
    global possible_moves
    possible_moves = []
    for start in letter_to_blocks.keys():
        for end in letter_to_blocks:
            if start != end:
                possible_moves.append(start + end)


def calculate_string_length():
    global string_length
    string_length = NUMBER_OF_BLOCKS * 2 + 2


def initialize_grid():
    display_width = NUMBER_OF_TOWERS
    display_height = NUMBER_OF_BLOCKS + 2  # Extra row on top and bottom
    global grid
    grid = [list("." * display_width) for row in range(display_height)]


def create_letters_and_blocks():
    global letter_to_blocks
    letter_to_blocks = {}
    for i in range(NUMBER_OF_TOWERS):
        letter_to_blocks[get_letter_from_index(i)] = []
    first_pole = get_letter_from_index(0)
    letter_to_blocks[first_pole] = list(range(NUMBER_OF_BLOCKS, 0, -1))


def get_letter_from_index(i):
    return chr(i + 65)


def place_blocks():
    for i in range(NUMBER_OF_TOWERS):
        letter = get_letter_from_index(i)
        blocks = letter_to_blocks[letter]
        for block in blocks:
            block_string = get_block_string(block)


def add_letter_to_grid(i):
    letter = get_letter_from_index(i)
    letter_string = create_letter_string(letter)
    grid[-1][i] = letter_string


def create_letter_string(letter):
    border_string = " " * NUMBER_OF_BLOCKS
    return "".join([border_string, " ", letter, border_string])


def populate_grid():
    for i in range(NUMBER_OF_TOWERS):
        add_letter_to_grid(i)
        stack_blocks_on_letter(i)


def stack_blocks_on_letter(i):
    letter = get_letter_from_index(i)
    blocks = letter_to_blocks[letter]
    for j, block in enumerate(blocks):
        block_string = get_block_string(block)
        grid[-2 - j][i] = block_string
    rows_without_blocks = NUMBER_OF_BLOCKS - len(blocks) + 1
    for row in range(rows_without_blocks):

        grid[row][i] = " " * NUMBER_OF_BLOCKS + "||" + " " * NUMBER_OF_BLOCKS


def get_block_string(block):
    border_str = " " * (NUMBER_OF_BLOCKS - block)
    block_str = "@" * block
    return "".join([border_str, block_str, "_", str(block), block_str, border_str])


def show_grid():
    for row in grid:
        print("".join(row))


def display():
    populate_grid()
    show_grid()


def make_next_move():
    valid_moves = [m for m in possible_moves if check_if_move_is_valid(m)]
    print("Enter Move:")
    proposed_move = input("> ").upper()
    while proposed_move not in valid_moves:
        print("Invalid move entered. Please enter a valid move, or type quit.")
        print("Valid Moves:", valid_moves)
        proposed_move = input("> ").upper()
        if proposed_move == "QUIT":
            return(False)
    make_move(proposed_move)
    return(True)


def check_if_move_is_valid(proposed_move):
    if proposed_move not in possible_moves:
        return False
    start_blocks = letter_to_blocks[proposed_move[0]]
    end_blocks = letter_to_blocks[proposed_move[1]]

    if len(start_blocks) == 0:
        return False
    elif len(end_blocks) == 0:
        return True
    elif start_blocks[-1] > end_blocks[-1]:
        return False
    else:
        return True


def make_move(proposed_move):
    start_blocks = letter_to_blocks[proposed_move[0]]
    end_blocks = letter_to_blocks[proposed_move[1]]
    block_to_move = start_blocks.pop()
    end_blocks.append(block_to_move)


def player_has_won():
    for letter in letter_to_blocks:
        if letter != get_letter_from_index(0):
            if len(letter_to_blocks[letter]) == NUMBER_OF_BLOCKS:
                print("Congratulations")
                return True
    return False


def main():
    print(
        f"""
    {'='*65}
    Welcome to Towes of Hanoi!

    {chr(10012)} Objective: Move the pyramid of levels from one pole to another
    without placing any larger blocks on top of smaller blocks.
    """
    )

    # Game Set-Up
    initialize_game()

    # Game Play
    game_active = True
    while game_active:
        display()
        game_active = make_next_move()
        if player_has_won():
            display()
            break
        

    # Farewell Message
    print("Thanks for playing!")


# Begin program if run directly
if __name__ == '__main__':
    main()