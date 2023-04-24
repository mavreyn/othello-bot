'''
Board class to represent the game state and make moves
'''

ALL_DIRECTIONS = {(0, 1),
                  (0, -1),
                  (1, 1),
                  (1, 0),
                  (1, -1),
                  (-1, -1),
                  (-1, 0),
                  (-1, 1)}

class OthelloBoard:
    # Game state and moveable directions
    _size = 8
    _game_state = None

    def __init__(self, size=8):
        # Make board given size
        self._size = size if size % 2 == 0 else (size - 1)
        self._game_state = [['.']*size for _ in range(size)]

        # Place 4 tokens in the center of the board
        board_center = self._size//2

        self.place(board_center, board_center, 'O')
        self.place(board_center + 1, board_center + 1, 'O')
        self.place(board_center, board_center + 1, 'X')
        self.place(board_center + 1, board_center, 'X')
    

    # Display the board state on screen with or without hints for legal moves
    def display(self, show_legal=None) -> None:
        legal_moves = self.get_legal_moves(show_legal)

        print()
        print(''.join(str((i+1) % 10) + ' ' for i in range(self._size)))

        for j in range(self._size):
            for i in range(self._size):
                piece = '●' if (i+1, j+1) in legal_moves else self._game_state[j][i]
                print(piece, end=' ')

            print(str(j+1))
        
        print()


    # Getter and setters
    def get(self, x, y):
        if x < 1 or y < 1 or x > self._size or y > self._size:
            return None
        else:
            return self._game_state[y-1][x-1]

    def place(self, x, y, piece):
        # Add to board and locations
        self._game_state[y-1][x-1] = piece

    
    # Import and Export board state
    def imp(self, state):
        self._game_state = state

    def exp(self):
        return self._game_state
    
    def opp(self, piece) -> str:
        return 'O' if piece == 'X' else 'X'


    # Count how many of a piece are on the board
    def count(self, piece):
        num = 0
        for x in range(self._size):
            for y in range(self._size):
                if self.get(x+1, y+1) == piece:
                    num += 1

        return num

    
    # Scoring function normalizes difference between piece amounts
    def norm_raw_score(self):
        xsc = self.count('X')
        ysc = self.count('O')

        return (xsc - ysc)/(xsc + ysc)
    

    # Returns distance to same piece encapsulating opp pieces in specified dir
    def _dist_to_bound(self, x, y, piece, direction):
        i = 0
        opp = self.opp(piece)

        while True:
            i += 1
            x += direction[0]
            y += direction[1]

            nxt = self.get(x, y)
            if nxt != opp:
                if nxt == piece and i != 1:
                    return i
                return None


    # Gets legal flipping directions and distances to other piece
    def _get_legal_dirs_and_dists(self, x, y, piece):
        if self.get(x, y) == '.':
            return {(direction, dist) for direction in ALL_DIRECTIONS if (dist := self._dist_to_bound(x, y, piece, direction))}
        else:
            return None

    # Play a move on the board, returns if the play is successful
    def play(self, x, y, piece):
        legal_dirs_and_dists = self._get_legal_dirs_and_dists(x, y, piece)

        if not legal_dirs_and_dists:
            return False
        else:
            # Replace all spaces in dir line with piece
            self.place(x, y, piece)
            for direction, dist in legal_dirs_and_dists:
                for i in range(1, dist):
                    self.place(i*direction[0]+x, i*direction[1]+y, piece)
            
            return True


    # Gets all legal moves (using brute force for now, rather expensive)
    def get_legal_moves(self, piece):
        return [(x+1, y+1) for x in range(self._size)
                           for y in range(self._size) if self._get_legal_dirs_and_dists(x+1, y+1, piece)]


    # Sums the scores currently on the board
    def print_scores(self) -> None:
        xsc = self.count('X')
        osc = self.count('O')

        print('X:', xsc)
        print('O:', osc)

        if xsc > osc:
            print('X Wins!')
        elif xsc < osc:
            print('O Wins!')
        elif xsc == osc:
            print('Tie Game!')

