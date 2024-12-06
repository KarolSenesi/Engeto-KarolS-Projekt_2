"""
KarolS-Projekt_2: Druhý projekt do Engeto Online Python Akademie - Tic-tac-toe

author: Karol Seneši
email: senesi.charles@seznam.cz
discord: KarolS. (immaculate_gull_26453)
akademie: python-24-4-2024
"""
# Pozdrav uživateli a výpis pravidel hry. Tento i následující bloky začínající
# "def" jsou definované funkce, které si pak hra volá
def print_welcome_message():
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
    print("-" * 40)

# Inicializace hracího pole (boardu)
def initialize_board():
    return [str(i) for i in range(1, 10)]

# Zobrazení hracího pole. Pro lepší přehlednost pro hráče je oproti zadání
# layout upravený do podoby numerické klávesnice. Pozice je pak po zvolení
# X, nebo 0 podle hráče místo původního čísla
def display_board(board):
    print("+---+---+---+")
    for i in [6, 3, 0]:  
        print(f"| {board[i]} | {board[i + 1]} | {board[i + 2]} |")
        print("+---+---+---+")
    print("=" * 40)

# Ověření, zda je zadaná pozice číslo od 1 do 9. Tato kontrola a chybová
# hláška pokrývají jak požadavek na zadání čísla jen z hracího pole (bod č.6),
# tak požadavek na nemožnost zadání jiného vstupu, než je číslo (bod č.7). 
# Není tedy nutné zadávat každou kontrolu zvlášť.
def is_valid_number(move):
    return move.isdigit() and 1 <= int(move) <= 9

# Ověření, zda je zvolená pozice volná
def is_position_free(board, move):
    return board[int(move) - 1] not in ["X", "O"]

# Ověření vítěze hry
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2],  # Horizontal
        [3, 4, 5],  # Horizontal
        [6, 7, 8],  # Horizontal
        [0, 3, 6],  # Vertical
        [1, 4, 7],  # Vertical
        [2, 5, 8],  # Vertical
        [0, 4, 8],  # Diagonal
        [2, 4, 6],  # Diagonal
    ]
    return any(all(board[i] == player for i in combo) 
                for combo in win_combinations
                )

# Ověření, zda nezbývá žádné volné hrací pole
def is_board_full(board):
    return all(space in ["X", "O"] for space in board)

# Hlavní funkce spuštění hry
def tic_tac_toe():
    print_welcome_message()
    board = initialize_board()
    display_board(board)

    current_player = "O"

    while True:
        move = input(
            f"Player {current_player} | Please enter your move number: "
        ).strip()

        if not is_valid_number(move):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        if not is_position_free(board, move):
            print(f"Position {move} is already taken! Please choose another.")
            continue

        move = int(move) - 1
        board[move] = current_player
        display_board(board)

        if check_winner(board, current_player):
            print(f"Congratulations, the player {current_player} WON!")
            break

        if is_board_full(board):
            print("It's a tie! No more moves left.")
            break

        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    tic_tac_toe()