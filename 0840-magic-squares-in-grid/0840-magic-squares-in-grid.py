
class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):

                # Check center element
                if grid[i+1][j+1] != 5:
                    continue

                # Extract 3x3 subgrid
                nums = [
                    grid[i][j:j+3],
                    grid[i+1][j:j+3],
                    grid[i+2][j:j+3]
                ]

                # Check numbers from 1 to 9
                if sorted(sum(nums, [])) != list(range(1, 10)):
                    continue

                # Check rows
                if any(sum(row) != 15 for row in nums):
                    continue

                # Check columns
                if any(sum(nums[r][c] for r in range(3)) != 15
                       for c in range(3)):
                    continue

                # Check diagonals
                if sum(nums[k][k] for k in range(3)) != 15:
                    continue

                if sum(nums[k][2-k] for k in range(3)) != 15:
                    continue

                count += 1

        return count
