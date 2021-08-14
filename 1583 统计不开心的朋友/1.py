class Solution:
    def unhappyFriends(self, n: int, preferences, pairs ) -> int:
        # store rank matrix, descending. thus 0 > 1
        idx_matrix = [[0 for i in range(n)] for i in range(n)]
        for idx_x, prefer_list in enumerate(preferences):
            for rank, idx_y in enumerate(prefer_list):
                idx_matrix[idx_x][idx_y] = rank 
        # get match list
        match = [0] * n
        for pair in pairs:
            x, y = pair[0], pair[1]
            match[x] = y  
            match[y] = x
        
        count = 0
        for x, y in enumerate(match):
            rank_y = idx_matrix[x][y] # find the y-th rank in matrix
            for i in range(n):
                if i != x and idx_matrix[x][i] < rank_y: # find the closer u in x. Ensure x not inside(or 999 in the top)
                    u = i
                    v = match[i] # find the corresponding v for u 
                    if idx_matrix[u][v] > idx_matrix[u][x]: # if uv > ux, means ux is more closer
                        count += 1
                        break # important, else will count more than 1
                else:
                    continue
        return count 
            
sol = Solution()
print(sol.unhappyFriends(
    4,
    [[1,3,2],[2,3,0],[1,0,3],[1,0,2]],
    [[2,1],[3,0]]
))
            

            
