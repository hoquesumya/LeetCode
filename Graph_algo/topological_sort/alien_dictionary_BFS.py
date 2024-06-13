order = {}
        inDegree = {}

        for word in words:
            for c in word:
                inDegree[ord(c) - ord("a")] = 0
                order[c] = []
        print(inDegree)
        print(order)


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
                    inDegree[c] += 1
                    found = True
                    break
                j += 1
            if len(word1) != min_len and not found:
                return ""
        print(order)
        list_of_words = []
        queue = collections.deque()

        for i in inDegree:
            if inDegree[i] == 0:
                cha = chr(ord("a") + i)
                print("char", i)
                queue.append(cha)
        visited = 0
        while queue:
            c = queue.popleft()
            list_of_words.append(c)
            visited += 1
            for adj in order[c]:
                adj_indx = ord(adj) - ord('a')
                inDegree[adj_indx] -= 1
                if inDegree[adj_indx] == 0:
                    queue.append(adj)
            print(queue)
        if visited != len(inDegree):
            return ""
        else:
            return "".join(list_of_words)
