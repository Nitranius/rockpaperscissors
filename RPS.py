def main():
    pick_player1 = input("ROCK PAPER SCISSORS    ->")
    clear_console1 = clear_console(pick_player1)
    pick_player2 = input("ROCK PAPER SCISSORS    ->")
    clear_console_2 = clear_console2(pick_player2)
    player1_picked = player1pick(f"Player 1 has picked {pick_player1}!!!")
    player2_picked = player2pick(f"Player 2 has picked {pick_player2}!!!")
    winner_1o3 = winner_first(player1_picked, player2_picked)

def player1pick(pick_player1):
    print(f"{pick_player1}")
    return pick_player1


def clear_console(pick_player1):
    if pick_player1  != "ROCK PAPER SCISSORS    ->":
        import os
        os.system("clear")

def clear_console2(pick_player2):
    if pick_player2  != "ROCK PAPER SCISSORS    ->":
        import os
        os.system("clear")

def player2pick(pick_player2):
    print(f"{pick_player2}")
    return pick_player2

def winner_first(player1_picked, player2_picked):
    replace_player2 = player2_picked.replace("2","1")
    replaced_end_message = player1_picked.replace("Player 1 has picked","")
    if player1_picked.lower() == replace_player2.lower():
        print(f"Both players picked {replaced_end_message.upper()} it's a draw!!!")

main()