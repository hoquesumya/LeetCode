cycle, visited = set(), set()
        order = {char: [] for word in words for char in word}
        res = []
    
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            j = 0
            found = False
            while j < min_len:
                if word1[j] != word2[j]:
                    c = ord(word2[j]) - ord("a")
                    order[word1[j]].append(word2[j])
                    found = True
                    break
                j += 1

            if len(word1) != min_len and not found:
                return ""
        def dfs(char):
            if char in cycle: #check if the node is in the path
                return False
            cycle.add(char)
            if char in visited:
                return True
            for adj in order[char]:
                if not dfs(adj):
                    return False
            visited.add(char)
            cycle.remove(char)
            res.append(char)
            return True
        for key in order:
            if key not in visited:
                if not dfs(key):
                    return ""
        res.reverse()
        return "".join(res)


