arr = [4, 4, 8, 9, 4,12, 9 , 11, 13, 7, 10]
class MinHeap:

    def __init__(self) -> None:
        pass

    def helper_push(self, curr):
        if curr == 0:
            return
        parent = (curr - 1) // 2 
        if arr[curr] >= arr[parent]:
            return
        temp = arr[parent]
        arr[parent] = arr[curr]
        arr[curr] = temp
        self.helper_push(parent)
    
    def helper_extract(self, curr):
        fst_ind = (curr * 2) + 1
        snd_ind = (curr) * 2 + 2
        
        temp_curr = -1
        min_res = 0
        if fst_ind  >= len(arr) and snd_ind >= len(arr):
            return
        elif fst_ind < len(arr)  and snd_ind >= len(arr):
            min_res = fst_ind
        else:
            if arr[fst_ind] <= arr[snd_ind]:
                min_res = arr[fst_ind]
                temp_curr = fst_ind
            else:
                min_res = arr[snd_ind]
                temp_curr = snd_ind
        if min_res >= arr[curr]:
            return
        temp = arr[curr]
        arr[curr] = min_res
        arr[temp_curr] = temp
      

        self.helper_extract(temp_curr)




        

    
    def heapify(self, val ):
        pass
    def heappush(self, val):
        arr.append(val)
        self.helper_push(len(arr) - 1)
    
    def heappop(self):
        pop_val = arr.pop()
        print(pop_val)
        arr[0] = pop_val
        print(arr)
        self.helper_extract(0)



if __name__ == '__main__':
    heap = MinHeap()
    heap.heappush(5)
    print(arr)
    heap.heappush(3)
    print(arr)
    heap.heappop()
    print(arr)


