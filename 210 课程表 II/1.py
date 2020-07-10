class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        edge_graph = collections.defaultdict(list)
        for pre_req in prerequisites:
            pre = pre_req[1]
            after = pre_req[0]
            indegree[after] +=1 
            edge_graph[pre].append(after)
        queue = collections.deque([u for u in range(numCourses) if indegree[u] == 0])
        result = [] # collect result
        while queue:
            now = queue.popleft()
            result.append(now)
            for vertex in edge_graph[now]:
                indegree[vertex] -= 1
                if indegree[vertex] == 0:
                    queue.append(vertex)
        
        if len(result) != numCourses:
            return []
        return result