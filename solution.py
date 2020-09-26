class Solution(object):
    def getMaximumGold(self, grid):
        self.most_gold = 0      # SELF PROPERTY SO MAY BE ADJUSTED FROM ANY LEVEL
        rows = len(grid)
        cols = len(grid[0])

        def find_path(i, j, total):
            # UPDATE GOLD PATH WITH NEW SPACE GOLD
            grid_gold = grid[i][j]
            self.most_gold = max(self.most_gold, total + grid_gold)

            # SET NEW SPACE GOLD TO ZERO (USED UP/BLOCK DIRECTION)
            grid[i][j] = 0

            # FOR ALL ADJACENT SPACES
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                # FOR ALL VALID RANGES/EXCLUDE ZERO SPACES
                if x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] != 0:
                    # SEND NEXT SPACE INFO AS WELL AS UPDATED TOTAL
                    find_path(x, y, total + grid_gold)

            # RETURN SPACE TO ORIGINAL VALUE
            grid[i][j] = grid_gold

        # START AT ALL SPACES THAT DON'T EQUAL ZERO
        # STARTING GOLD ALWAYS EQUALS ZERO
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    find_path(i, j, 0)

        return self.most_gold
