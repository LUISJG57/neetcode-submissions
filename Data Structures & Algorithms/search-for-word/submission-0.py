class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or r>= rows or c < 0 or c >= cols or word[i] != board[r][c] or board[r][c] == "#":
                return False
            board[r][c] = "#"
            res = False
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    res = True
                    break
            board[r][c] = word[i]
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
