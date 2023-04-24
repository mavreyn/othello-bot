'''
Going to try to actually do this
Making a bot and interface to play Othello
It would be super cool to have a windowed version of this

Maverick Reynolds
12-02-2022

'''

from Board import OthelloBoard
from Computer import OthelloComputer
import matplotlib.pyplot as plt
import time
import re
import blessed


# Global Variables
Main_Board = OthelloBoard()
Curr_Turn = 'X'
Pass_Count = 0
Board_Scores = [0]
Terminal = blessed.Terminal()


def play_game():
    global Main_Board
    global Curr_Turn
    global Pass_Count
    global Board_Scores
    global Terminal

    # Simple interface
    sz = input('Board size (8) > ')
    sz = int(sz) if sz else 8
    Main_Board = OthelloBoard(sz)

    num_players = input('Players (0/1/2) > ')
    num_players = int(num_players) if num_players else 0
    ocptr = OthelloComputer()

    if num_players == 0:
        pause_time = input('Pause time (s) > ')
        t = float(pause_time) if pause_time else 0

    terminal_home()
    Main_Board.display(show_legal=Curr_Turn)

    # Start turn cycle
    while Main_Board.count('.') > 0 and Pass_Count < 2:
        Pass_Count = 0
        if num_players == 2:
            player_turn()
        elif num_players == 1:
            player_turn()
            time.sleep(1)
            computer_turn(ocptr.simple, 'O')
        else:
            computer_turn(ocptr.naive, 'X')
            time.sleep(t)

            computer_turn(ocptr.simple, 'O')
            time.sleep(t)

        Board_Scores.append(Main_Board.norm_raw_score())

    # Print Scores and reset
    print('\n'*2)
    Main_Board.print_scores()
    print_score_plot()
    input()


# Passes the current turn and displays the board
def pass_turn(success=True):
    global Curr_Turn
    global Pass_Count

    Curr_Turn = 'O' if Curr_Turn == 'X' else 'X'
    terminal_home()
    Main_Board.display(show_legal=Curr_Turn)
    
    if success:
        Pass_Count = 0
    else:
        Pass_Count += 1


# Provide menu for player and passes accordingly
def player_turn():
    legal_moves = Main_Board.get_legal_moves(Curr_Turn)

    if not legal_moves:
        pass_turn(False)

    x, y = None, None
    while (x, y) not in legal_moves:
        ln = input('Play for ' + Curr_Turn + ' > ')
        coords = re.search('^(\d{1,2})\s(\d{1,2})$', ln)
        x, y = int(coords.group(1)), int(coords.group(2))

    pass_turn(Main_Board.play(x, y, Curr_Turn))


# Let computer take its turn, passes accordingly
def computer_turn(move_method, piece):
    curr_score = Main_Board.norm_raw_score()
    resp = move_method(Main_Board, piece)
    if resp:
        Main_Board.play(*resp, piece)

    print(f'Computer {piece}: ', resp, ' '*10)
    print(f'Gain: {round(Main_Board.norm_raw_score() - curr_score, 3)}')

    pass_turn(success=resp)


# Show plot using matplotlib
def print_score_plot():
    plt.plot(list(range(len(Board_Scores))), Board_Scores)
    plt.title('Board Evaluation')
    plt.xlabel('Move Number')
    plt.ylabel('Normalized Raw Score')
    plt.ylim(-1.1, 1.1)
    plt.grid()
    plt.show()

# Bring Blessed to home position
def terminal_home():
    print(Terminal.move_yx(4, 0))



def main():
    print('Welcome to Othello!')
    print(Terminal.move_yx(1, 0))
    with Terminal.hidden_cursor():
        play_game()


if __name__ == '__main__':
    main()

