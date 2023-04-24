'''
Basic computer with different methods for playing Othello and turn-taking
'''

from Board import OthelloBoard
import random
import copy

class OthelloComputer:

    def __init__(self) -> None:
        pass

    # Picks a random legal move to play
    def naive(self, board: OthelloBoard, piece) -> tuple[int]:
        moves = board.get_legal_moves(piece)
        return random.choice(moves) if moves else None
    

    # Uses a greedy approach, picks move with highest gain at each turn
    def simple(self, board: OthelloBoard, piece) -> tuple[int]:
        moves = board.get_legal_moves(piece)
        if not moves:
            return None

        move_scores = []

        for move in moves:
            curr_board = copy.deepcopy(board)
            curr_board.play(*move, piece)

            move_scores.append(curr_board.norm_raw_score())
        
        if piece == 'X':
            extrema = max(move_scores)
        else:
            extrema = min(move_scores)

        return moves[move_scores.index(extrema)]