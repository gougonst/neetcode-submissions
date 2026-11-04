class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Define graph
        graph: Dict[Set[int]] = collections.defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        def findLeaves(graph: Dict[Set[int]]) -> List[int]:
            leaves = []
            for node, neighbors in graph.items():
                # Using smaller or equal rather than equal to 1 here because
                #  a leaf can have no any neighbors
                if len(neighbors) <= 1:
                    leaves.append(node)
            return leaves

        def isAllLeaves(graph: Dict[Set[int]]) -> bool:
            for node, neighbors in graph.items():
                # Using bigger than 1 here because a leaf can have no any neighbors or
                #  exactly 1 neighbor
                if len(neighbors) > 1:
                    return False
            return True

        # Find leaves at each level
        # Whether all nodes in graph are leaves
        # Yes: They are roots
        # No: Delete leaves and continue next loop
        while not isAllLeaves(graph):
            # The question guarantee that it'll always find something
            leaves = findLeaves(graph)
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                del graph[leaf]

        return [node for node in graph.keys()]