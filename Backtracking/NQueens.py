class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print("\n")

    def is_place_safe(self, row_index, col_index):
        # checks horizontally
        for j in range(self.n):
            if self.board[row_index][j] == 1:
                return False

        # top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):
            if j < 0:
                break
            if self.board[i][j] == 1:
                return False
            j -= 1

        # top right to bottom left
        j = col_index
        for i in range(row_index, self.n):
            if j < 0:
                break
            if self.board[i][j] == 1:
                return False
            j -= 1

        return True

    def solve(self, col_index):
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_place_safe(row_index, col_index):
                self.board[row_index][col_index] = 1

                if self.solve(col_index + 1):
                    return True
                
                self.board[row_index][col_index] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is not solution for the problem!")


queens = NQueens(4)
queens.solve_NQueens()
