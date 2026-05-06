# Let's put all our code here

'''
CSC 255 OC1 - Group Assignment
Sudoku Solver
'''

'''
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

def checkValidMove()            #Avi


def printPuzzle()               #Thuy

def checkifPuzzleComplete()     #Thuy

def checkEmptyCells(puzzle):
    """
    Scan the board and return a list of (row, col) tuples for every cell
    whose value is 0 (i.e. still empty).

    Example return value: [(0, 2), (0, 3), (0, 5), ...]
    """
    empty_cells = []

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                empty_cells.append((row, col))

    return empty_cells           #Sebastian

def solveBacktracking(puzzle, index=0):
    """
    Solve the Sudoku puzzle using recursive backtracking.

    On the first call, two boards are built from the puzzle:
      • base_board  – static copy, never modified, used to identify fixed cells
      • work_board  – working copy that gets filled and backtracked on

    Subsequent recursive calls pass the boards forward via default-arg mutation.
    Returns the solved work_board if a solution exists, or None otherwise.
    """
    # ── First call only: build the two boards and the empty cell list ────────
    if index == 0:
        solveBacktracking.base_board = [row[:] for row in puzzle]
        solveBacktracking.work_board = [row[:] for row in puzzle]
        solveBacktracking.empty_cells = checkEmptyCells(solveBacktracking.work_board)

    base_board  = solveBacktracking.base_board
    work_board  = solveBacktracking.work_board
    empty_cells = solveBacktracking.empty_cells

    # ── Base case: all empty cells filled ────────────────────────────────────
    if index == len(empty_cells):
        return work_board

    row, col = empty_cells[index]

    # Safety check: skip pre-filled cells from the original puzzle
    if base_board[row][col] != 0:
        return solveBacktracking(puzzle, index + 1)

    # ── Try each candidate, recurse, backtrack on failure ────────────────────
    for num in candidateNumbers(work_board, row, col):
        work_board[row][col] = num

        if solveBacktracking(puzzle, index + 1):
            return work_board

        work_board[row][col] = 0  # backtrack         #Sebastian

def candidateNumbers(puzzle, row, col):
    """
    Return a list of numbers (1–9) that are legal candidates for the cell
    at (row, col) by eliminating every value already present in the same
    row, column, and 3×3 quadrant.

    Uses checkValidMove to confirm each remaining candidate is truly valid
    before including it in the result.
    """
    candidates = []

    for num in range(1, 10):
        # Collect values seen in the same row, column, and quadrant
        row_values  = set(puzzle[row])
        col_values  = set(puzzle[r][col] for r in range(9))
        box_row     = (row // 3) * 3
        box_col     = (col // 3) * 3
        quad_values = set(
            puzzle[r][c]
            for r in range(box_row, box_row + 3)
            for c in range(box_col, box_col + 3)
        )

        # A number is a candidate only if it doesn't appear in any of those sets
        if num not in row_values and num not in col_values and num not in quad_values:
            # Double-check with checkValidMove for full validation
            if checkValidMove(puzzle, row, col, num):
                candidates.append(num)

    return candidates          #Sebastian

def generateStartingBoard()      #Avi



'''
