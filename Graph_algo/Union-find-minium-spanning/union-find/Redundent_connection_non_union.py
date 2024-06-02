import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        edge_ver_dict = collections.defaultdict(list)

        def find_path(u, v):

            if u == v:
                return True
            visited.add(u)

            for i in edge_ver_dict[u]:
                if i not in visited:
                    res = find_path(i, v)
                    if res:
                        return True
            return False
        for u, v in edges:
            visited = set()
            if find_path(u, v):
                return [u, v]
            else:
                edge_ver_dict[u].append(v)
                edge_ver_dict[v].append(u)
        return None

           
        

