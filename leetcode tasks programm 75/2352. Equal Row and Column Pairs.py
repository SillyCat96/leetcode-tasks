from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        
          # Step 1: Count the frequency of each row
        # Use tuples for rows so they are hashable (can be used in Counter)
        row_counts = Counter()
        for r in range(n):
            row_counts[tuple(grid[r])] += 1
        
        # Step 2: Extract each column and check its frequency among the rows
        equal_pairs_count = 0
        for c in range(n): # Iterate through each column index
            current_col = []
            for r in range(n): # Collect elements of the current column
                current_col.append(grid[r][c])
            
            # Convert the column to a tuple to look it up in row_counts
            equal_pairs_count += row_counts[tuple(current_col)]
            
        return equal_pairs_count
        