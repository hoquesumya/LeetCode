class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        implemetyning kuskal's algorithm
        """
        edges_cost = []
        cost = 0

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges_cost.append([i, j, dist])

        edges_cost = sorted(edges_cost, key=lambda x: x[2])

        parent = [i for i in range (len(edges_cost)+1)] # [0] parant 0
        rank = [1] * (len(edges_cost) +1)

        def find(n):
            '''
            if n == parent[n]:
                return n
            else:
                return find(parent[n])
            
            '''
            p = parent[n] #get the parent of n
    
            while p != parent[p]:  #get the gradparent of n
                #path compression
                parent[p]= parent[parent[p]] #set grandparent = grandparent parent
                p = parent[p] #great great gradparent
            return p
            

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            else:
                if rank[p1] >= rank[p2]:
                    rank[p1] += rank[p2]
                    parent[p2] = p1
                else:
                    rank[p2] += rank[p1]
                    parent[p1] = p2
            return True

        for n1, n2, edge_cost in edges_cost:
            if union(n1, n2):
                cost += edge_cost
        print(parent)
        return cost





