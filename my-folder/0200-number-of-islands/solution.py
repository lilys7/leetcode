class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        visited = set()
        # iterate bfs
        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                r,c = queue.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    
                    row = dr + r
                    col = dc + c
                    if row in range(rows) and col in range(cols) and grid[row][col] == '1' and (row,col) not in visited:
                        visited.add((row,col))
                        queue.append((row,col))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    bfs(row, col)
                    numIslands += 1
        return numIslands


        
