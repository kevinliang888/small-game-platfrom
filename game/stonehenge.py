"""
stonehenge game module
"""

from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    Represent the StonehengeGame system

    is_p1_turn: whether it is p1 turn to start to play the game
    current_state: Current state of the game
    """

    current_state: "StonehengeState"

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the stonehengeGame by is_p1_turn and size of board.
        """
        size = int(input("Enter the size length of the board: "))
        self.current_state = StonehengeState(is_p1_turn, size,
                                             self.create_basic_board(size))

    def create_basic_board(self, size: int) -> list:
        """
        Create the basic board for the game.
        """
        board = []
        if size == 1:
            board = [['@', 'A', 'B'], ['@', 'C'], ['@', 'A'],
                     ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']]
        elif size == 2:
            board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],
                     ['@', 'A', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],
                     ['@', 'F', 'C'], ['@', 'G', 'D', 'A'], ['@', 'E', 'B']]
        elif size == 3:
            board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                     ['@', 'F', 'G', 'H', 'I'], ['@', 'J', 'K', 'L'],
                     ['@', 'A', 'C', 'F'], ['@', 'B', 'D', 'G', 'J'],
                     ['@', 'E', 'H', 'K'], ['@', 'I', 'L'], ['@', 'J', 'F'],
                     ['@', 'K', 'G', 'C'], ['@', 'L', 'H', 'D', 'A'],
                     ['@', 'I', 'E', 'B']]
        elif size == 4:
            board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                     ['@', 'F', 'G', 'H', 'I'], ['@', 'J', 'K', 'L', 'M', 'N'],
                     ['@', 'O', 'P', 'Q', 'R'], ['@', 'A', 'C', 'F', 'J'],
                     ['@', 'B', 'D', 'G', 'K', 'O'], ['@', 'E', 'H', 'L', 'P'],
                     ['@', 'I', 'M', 'Q'], ['@', 'N', 'R'], ['@', 'O', 'J'],
                     ['@', 'P', 'K', 'F'], ['@', 'Q', 'L', 'G', 'C'],
                     ['@', 'R', 'M', 'H', 'D', 'A'], ['@', 'N', 'I', 'E', 'B']]
        elif size == 5:
            board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                     ['@', 'F', 'G', 'H', 'I'], ['@', 'J', 'K', 'L', 'M', 'N'],
                     ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                     ['@', 'U', 'V', 'W', 'X', 'Y'],
                     ['@', 'A', 'C', 'F', 'J', 'O'],
                     ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                     ['@', 'E', 'H', 'L', 'Q', 'V'], ['@', 'I', 'M', 'R', 'W'],
                     ['@', 'N', 'S', 'X'], ['@', 'T', 'Y'],
                     ['@', 'U', 'O'], ['@', 'V', 'P', 'J'],
                     ['@', 'W', 'Q', 'K', 'F'], ['@', 'X', 'R', 'L', 'G', 'C'],
                     ['@', 'Y', 'S', 'M' 'H', 'D', 'A'],
                     ['@', 'T', 'N', 'I', 'E', 'B']]
        return board

    def __str__(self) -> str:
        return "Welcome to the game SubtractSquare !!"

    def get_instructions(self) -> str:
        """
        Return the instruction of the game StonehengeGame.
        """
        s = "1. Players take turns claiming cells (in the diagram:" \
         "circles labelled with a capital letter).\n2. When a player" \
         " captures at least half of the cells in a ley-line " \
         "(in the diagram: hexagons with a line connecting it to cells)," \
         "then the player captures that ley-line.\n3. The first player" \
         "to capture at least half of the ley-lines is the winner.\n" \
         "4. A ley-line, once claimed, cannot be taken by the other player."
        return s

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return True if current_state implies that the game is over. Otherwise,
        return False.

        >>> from unittest.mock import patch
        >>> with patch('builtins.input', return_value=str(1)):\
game = StonehengeGame(True)
        >>> current_state = game.current_state
        >>> current_state = current_state.make_move(game.str_to_move("A"))
        >>> game.is_over(current_state)
        True

        >>> with patch('builtins.input', return_value=str(5)):\
game = StonehengeGame(True)
        >>> game.current_state = StonehengeState(True, 5, [['2', '2', '1'], ['2', '2', '1', '2'],\
        ['1', '1', '2', '1', '2'], ['1', '1', '2', '1', '2', '1'], \
        ['2', '2', '1', '2', '1', '2' ,'T'],\
        ['@', '1', '2', 'W', 'X', 'Y'], ['2', '2', '2', '1', '1', '2'], \
        ['1', '1', '1', '2', '2', '1', '1'],\
        ['2', '2', '1', '1', '2', '2'], ['2', '2', '2', '1', 'W'], \
        ['@', '1', '2', 'X'], ['@', 'T', 'Y'],\
        ['2', '1', '2'], ['1', '2', '1', '1'], ['2', 'W', '2', '2', '1'],\
         ['@', 'X', '1', '1', '2', '2'],\
        ['2', 'Y', '2', '2', '1', '1', '2'],\
         ['@', 'T', '1', '2', '2', '1']])
        >>> game.is_over(game.current_state)
        True
        >>> game.is_winner('p2')
        True
        """
        count_row = len(state.current_board)
        count_mark1 = state.count_mark1()
        count_mark2 = state.count_mark2()
        return count_mark1 >= count_row / 2 or count_mark2 >= count_row / 2

    def is_winner(self, player: str) -> bool:
        """
        Return True if player is the winner.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """
        Return the move string directly.
        """
        return string.strip()


class StonehengeState(GameState):
    """
    Represent the current state of the game StonehengeGame.

    is_p1_turn: whether it is p1 turn to play the game
    """
    size: int
    current_board: list

    def __init__(self, is_p1_turn: bool, size: int,
                 current_board: list) -> None:
        """
        Initialize this game state by is_p1_turn, the size of board and
        current_board.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state.p1_turn
        True
        >>> state.size
        1
        >>> state.current_board
        [['@', 'A', 'B'], ['@', 'C'],\
 ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']]

        """
        GameState.__init__(self, is_p1_turn)
        self.size = size
        self.current_board = current_board

    def __str__(self) -> str:
        """
        Return the board of the StonehengeState.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> print(state)
              @   @
             /   /
        @ - A - B
             \\ / \\
          @ - C   @
               \\
                @

        >>> board = [['1', '1', '2'], ['@', 'C', 'D', 'E'], ['1', '1', 'G'],\
                     ['1', '1', 'C'], ['@', '2', 'D', '1'], ['@', 'E', 'G'],\
                     ['1', '1', 'C'], ['@', 'G', 'D', '1'], ['@', 'E', '2']]
        >>> state = StonehengeState(False, 2, board)
        >>> print(state)
                1   @
               /   /
          1 - 1 - 2   @
             / \\ / \\ /
        @ - C - D - E
             \\ / \\ / \\
          1 - 1 - G   @
               \\   \\
                1   @
        """
        s = ''
        board = self.current_board
        if self.size == 1:
            s = """\
      {5}   {6}
     /   /
{0} - {1} - {2}
     \\ / \\
  {3} - {4}   {8}
       \\
        {7}""".format(board[0][0], board[0][1], board[0][2], board[1][0],
                      board[1][1], board[2][0], board[3][0], board[4][0],
                      board[5][0])
        elif self.size == 2:
            s = """\
        {10}   {11}
       /   /
  {0} - {1} - {2}   {12}
     / \\ / \\ /
{3} - {4} - {5} - {6}
     \\ / \\ / \\
  {7} - {8} - {9}   {15}
       \\   \\
        {13}   {14}""".format(board[0][0], board[0][1], board[0][2],
                              board[1][0], board[1][1], board[1][2],
                              board[1][3], board[2][0], board[2][1],
                              board[2][2], board[3][0], board[4][0],
                              board[5][0], board[6][0], board[7][0],
                              board[8][0])
        elif self.size == 3:
            s = """\
          {16}   {17}
         /   /      
    {0} - {1} - {2}   {18}
       / \\ / \\ /
  {3} - {4} - {5} - {6}   {19}
     / \\ / \\ / \\ /
{7} - {8} - {9} - {10} - {11}
     \\ / \\ / \\ / \\
  {12} - {13} - {14} - {15}   {23}
       \\   \\   \\
        {20}   {21}   {22}""".format(board[0][0], board[0][1], board[0][2],
                                     board[1][0], board[1][1], board[1][2],
                                     board[1][3], board[2][0], board[2][1],
                                     board[2][2], board[2][3], board[2][4],
                                     board[3][0], board[3][1], board[3][2],
                                     board[3][3], board[4][0], board[5][0],
                                     board[6][0], board[7][0], board[8][0],
                                     board[9][0], board[10][0], board[11][0])
        elif self.size == 4:
            s = """\
            {23}   {24}
           /   /
      {0} - {1} - {2}   {25}
         / \\ / \\ /
    {3} - {4} - {5} - {6}   {26}
       / \\ / \\ / \\ /
  {7} - {8} - {9} - {10} - {11}   {27}
     / \\ / \\ / \\ / \\ /
{12} - {13} - {14} - {15} - {16} - {17}
     \\ / \\ / \\ / \\ / \\
  {18} - {19} - {20} - {21} - {22}   {32}
       \\   \\   \\   \\
        {28}   {29}   {30}   {31}"""\
    .format(board[0][0], board[0][1], board[0][2],
            board[1][0], board[1][1], board[1][2], board[1][3],
            board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
            board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
            board[3][5],
            board[4][0], board[4][1], board[4][2], board[4][3], board[4][4],
            board[5][0], board[6][0], board[7][0], board[8][0], board[9][0],
            board[10][0], board[11][0], board[12][0], board[13][0],
            board[14][0])
        elif self.size == 5:
            s = """\
              {31}   {32}
             /   /
        {0} - {1} - {2}   {33}
           / \\ / \\ /
      {3} - {4} - {5} - {6}   {34}
         / \\ / \\ / \\ /
    {7} - {8} - {9} - {10} - {11}   {35}
       / \\ / \\ / \\ / \\ /
  {12} - {13} - {14} - {15} - {16} - {17}   {36}
     / \\ / \\ / \\ / \\ / \\ /
{18} - {19} - {20} - {21} - {22} - {23} - {24}
     \\ / \\ / \\ / \\ / \\ / \\
  {25} - {26} - {27} - {28} - {29} - {30}   {42}
       \\   \\   \\   \\   \\
        {37}   {38}   {39}   {40}   {41}""" \
    .format(board[0][0], board[0][1], board[0][2],
            board[1][0], board[1][1], board[1][2], board[1][3],
            board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
            board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
            board[3][5],
            board[4][0], board[4][1], board[4][2], board[4][3], board[4][4],
            board[4][5], board[4][6],
            board[5][0], board[5][1], board[5][2], board[5][3], board[5][4],
            board[5][5],
            board[6][0], board[7][0], board[8][0], board[9][0],
            board[10][0], board[11][0], board[12][0], board[13][0],
            board[14][0], board[15][0], board[16][0], board[17][0])
        return s

    def __repr__(self) -> str:
        """
        Represent the StonehengeState by showing the current player, size of
        board as well as current board.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state
        P1's Turn: True
        Size of board: 1
        Current board:
              @   @
             /   /
        @ - A - B
             \\ / \\
          @ - C   @
               \\
                @
        >>> board = [['1', '1', '2'], ['@', 'C', 'D', 'E'], ['1', '1', 'G'],\
                     ['1', '1', 'C'], ['@', '2', 'D', '1'], ['@', 'E', 'G'],\
                     ['1', '1', 'C'], ['@', 'G', 'D', '1'], ['@', 'E', '2']]
        >>> state = StonehengeState(False, 2, board)
        >>> state
        P1's Turn: False
        Size of board: 2
        Current board:
                1   @
               /   /
          1 - 1 - 2   @
             / \\ / \\ /
        @ - C - D - E
             \\ / \\ / \\
          1 - 1 - G   @
               \\   \\
                1   @
        """
        return "P1's Turn: {}\nSize of board: {}\nCurrent board:\n{}"\
            .format(self.p1_turn, self.size, str(self))

    def get_possible_moves(self) -> list:
        """
        return a list which includes all the possible moves in current state.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state.get_possible_moves()
        ['A', 'B', 'C']

        >>> state = state.make_move('B')
        >>> state.get_possible_moves()
        []

        >>> state2 = StonehengeState(True, 5, [['2', '2', '1'], ['2', '2', '1', '2'],\
        ['1', '1', '2', '1', '2'], ['1', '1', '2', '1', '2', '1'], \
        ['2', '2', '1', '2', '1', '2' ,'T'],\
        ['@', '1', '2', 'W', 'X', 'Y'], ['2', '2', '2', '1', '1', '2'], \
        ['1', '1', '1', '2', '2', '1', '1'],\
        ['2', '2', '1', '1', '2', '2'], ['2', '2', '2', '1', 'W'], \
        ['@', '1', '2', 'X'], ['@', 'T', 'Y'],\
        ['2', '1', '2'], ['1', '2', '1', '1'], ['2', 'W', '2', '2', '1'],\
         ['@', 'X', '1', '1', '2', '2'],\
        ['2', 'Y', '2', '2', '1', '1', '2'],\
         ['@', 'T', '1', '2', '2', '1']])
        >>> state3 = StonehengeState(True, 5, [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],\
        ['@', 'F', 'G', 'H', 'I'], ['@', 'J', 'K', 'L', 'M', 'N'], \
        ['@', 'O', 'P', 'Q', 'R', 'S' ,'T'],\
        ['@', 'U', 'V', 'W', 'X', 'Y'], ['@', 'A', 'C', 'F', 'J', 'O'], \
        ['@', 'B', 'D', 'G', 'K', 'P', 'U'],\
        ['@', 'E', 'H', 'L', 'Q', 'V'], ['@', 'I', 'M', 'R', 'W'], \
        ['@', 'N', 'S', 'X'], ['@', 'T', 'Y'],\
        ['@', 'U', 'O'], ['@', 'V', 'P', 'J'], ['@', 'W', 'Q', 'K', 'F'],\
         ['@', 'X', 'R', 'L', 'G', 'C'],\
        ['@', 'Y', 'S', 'M', 'H', 'D', 'A'],\
         ['@', 'T', 'N', 'I', 'E', 'B']])

        """
        if self.count_mark1() >= len(self.current_board) / 2 or \
self.count_mark2() >= len(self.current_board) / 2:
            return []
        possible_move = []
        for row in self.current_board:
            for item in row:
                if item not in '@12' and item not in possible_move:
                    possible_move.append(item)
        return possible_move

    def make_move(self, move: str) -> "StonehengeState":
        """
        Return the new state of StonehengeGame after making move from move.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> new_state = state.make_move('A')
        >>> new_state.p1_turn
        False
        >>> new_state.get_possible_moves()
        []
        >>> state.p1_turn
        True
        >>> state.get_possible_moves()
        ['A', 'B', 'C']

        >>> board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],\
                     ['@', 'A', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],\
                     ['@', 'F', 'C'], ['@', 'G', 'D', 'A'], ['@', 'E', 'B']]
        >>> state = StonehengeState(False, 2, board)
        >>> new_state = state.make_move('A')
        >>> new_state.current_board
        [['2', '2', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],\
 ['2', '2', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],\
 ['@', 'F', 'C'], ['@', 'G', 'D', '2'], ['@', 'E', 'B']]
        """
        new_board = []
        for r in self.current_board:
            new_board.append(r[:])
        if self.p1_turn:
            mark = '1'
        else:
            mark = '2'
        for row in new_board:
            count = 0
            for i in range(len(row)):
                if row[i] == move:
                    row[i] = mark
                    count += 1
                elif row[i] == mark:
                    count += 1
            if row[0] == '@' and count >= (len(row) - 1)/2:
                row[0] = mark
        return StonehengeState(not self.p1_turn, self.size, new_board)

    def count_mark1(self) -> int:
        """
        Return the number of rows which are occupied by 1.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state.count_mark1()
        0
        >>> new_state = state.make_move('A')
        >>> new_state.count_mark1()
        3
        """
        count_mark1 = 0
        for row in self.current_board:
            if row[0] == '1':
                count_mark1 += 1
        return count_mark1

    def count_mark2(self) -> int:
        """
        Return the number of rows which are occupied by 2.

        >>> state = StonehengeState(False, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state.count_mark2()
        0
        >>> new_state = state.make_move('B')
        >>> new_state.count_mark2()
        3
        """
        count_mark2 = 0
        for row in self.current_board:
            if row[0] == '2':
                count_mark2 += 1
        return count_mark2

    def count1_in_a_row(self, row: list) -> int:
        """
        Return number of 1 in one of a row. This method works for any row of
        any board.

        >>> board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],\
                     ['@', 'A', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],\
                     ['@', 'F', 'C'], ['@', 'G', 'D', 'A'], ['@', 'E', 'B']]
        >>> state = StonehengeState(True, 2, board)
        >>> state.count1_in_a_row(['@', 'A', 'B'])
        0
        >>> state.count1_in_a_row(['2', '2', '1'])
        1
        >>> state.count1_in_a_row(['1', 'A', '1'])
        2
        >>> state.count1_in_a_row(['1', '1', '1', '1'])
        4
        """
        count1 = 0
        for item in row:
            if item == '1':
                count1 += 1
        return count1

    def count2_in_a_row(self, row: list):
        """
        Return number of 2 in one of a row. This method works for any row of
        any board.

        >>> board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],\
                     ['@', 'A', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],\
                     ['@', 'F', 'C'], ['@', 'G', 'D', 'A'], ['@', 'E', 'B']]
        >>> state = StonehengeState(True, 2, board)
        >>> state.count2_in_a_row(['@', 'A', 'B'])
        0
        >>> state.count2_in_a_row(['1', '1', '2'])
        1
        >>> state.count2_in_a_row(['2', 'A', '2'])
        2
        >>> state.count2_in_a_row(['2', '2', '2', '2'])
        4
        """
        count2 = 0
        for item in row:
            if item == '2':
                count2 += 1
        return count2

    def rough_outcome(self) -> float:
        """
        Return 1 if there is even one move that can lead to the
        current player winning. Return -1 if the other player
        is able to win immediately no matter what move we make.
        Otherwise, return 0.

        >>> state = StonehengeState(True, 1, [['@', 'A', 'B'], ['@', 'C'],\
        ['@', 'A'], ['@', 'B', 'C'], ['@', 'C', 'A'], ['@', 'B']])
        >>> state.rough_outcome()
        1

        >>> board = [['1', '1', '2'], ['@', 'C', 'D', 'E'], ['1', '1', 'G'],\
                     ['1', '1', 'C'], ['@', '2', 'D', '1'], ['@', 'E', 'G'],\
                     ['1', '1', 'C'], ['@', 'G', 'D', '1'], ['@', 'E', '2']]
        >>> state = StonehengeState(False, 2, board)
        >>> state.rough_outcome()
        -1

        >>> board = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G'],\
                     ['@', 'A', 'C'], ['@', 'B', 'D', 'F'], ['@', 'E', 'G'],\
                     ['@', 'F', 'C'], ['@', 'G', 'D', 'A'], ['@', 'E', 'B']]
        >>> state = StonehengeState(True, 2, board)
        >>> state.rough_outcome()
        0
        """
        row = len(self.current_board)
        outcome = []
        for move in self.get_possible_moves():
            new_state = self.make_move(move)
            count_mark1 = new_state.count_mark1()
            count_mark2 = self.count_mark2()
            if count_mark1 >= row / 2 or count_mark2 >= row / 2:
                return self.WIN
            else:
                new_list = [new_state.make_move(new_move).count_mark1()
                            >= row / 2 or
                            new_state.make_move(new_move).count_mark2()
                            >= row / 2
                            for new_move in new_state.get_possible_moves()]
                outcome.append(any(new_list))
        if all(outcome):
            return self.LOSE
        return self.DRAW


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
