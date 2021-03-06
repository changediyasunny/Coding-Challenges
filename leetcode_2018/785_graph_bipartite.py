"""
785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent
subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which
the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't
contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

Time Complexity: O(N+E) where N is the number of nodes in the graph, and E is the number of edges.
We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.

Space Complexity: O(N), the space used to store the color
"""

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = 1 - color[node]
                        elif color[nei] == color[node]:
                            return False
        return True

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        def dfs(pos):
            for k in graph[pos]:
                if k in color:
                    if color[k] == color[pos]:
                        return False
                else:
                    color[k] = 1-color[pos]
                    if not dfs(k):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
