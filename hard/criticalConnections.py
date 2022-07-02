class Solution(object):
    
    def cycles(self, node, parent, graph, colors, pars, cycleNodes):
	
	# this means the node is completely visited
	if colors[node] == 2:
	    return

	# this node has been visited, cycle is detected
	if colors[node] == 1:
	    curr = parent
	    cycleNodes.append((node, parent))

	    # backtrack until you reach node again...
	    while curr != node:
	    	par = pars[curr]
		cycleNodes.append((curr, par))
		curr = par
	    
	    return


	colors[node] = 1
        pars[node] = parent
        for adj in graph[node]:
	    # we dont want to go back
	    if pars[node] != adj:
                self.cycles(adj, node, graph, colors, pars, cycleNodes)
	
	# finished visiting this node
	colors[node] = 2
	    

        
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        critical = []
        
        colors = [0] * n

	pars = [0] * n

	cycleNodes = []

        graph = []
	for i in range(n):
	    graph.append([])

	solution = []

        for connection in connections:
            node1, node2 = connection[0], connection[1]
	    graph[node1].append(node2)
	    graph[node2].append(node1)

        self.cycles(0, -1, graph, colors, pars, cycleNodes)

	print(cycleNodes)
	for edge in cycleNodes:
	    x1, y1 = edge
	    for conn in connections:
	        x2, y2 = conn[0], conn[1]
		if (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2):
		    connections.remove(conn)

	print(connections)



sol = Solution()

sol.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3], [3, 4], [4, 5], [5, 3]])

