class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        self.graph = collections.defaultdict(list)
        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])
        return [self.dfs(query[0], query[1]) for query in queries]
    
    # start -> end ?
    @functools.lru_cache
    def dfs(self, start, end):
        if start == end:
            return True
        return any(self.dfs(nxt, end) for nxt in self.graph[start])
