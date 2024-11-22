2. (35 pts) Given `k` sorted lists, please design an algorithm as efficient as possible to merge these sorted list into a single sorted list. The total number of elements in all given lists is `n`. And please analyze the running time of your algorithm. (Hint: Better than `O(n log n)`)

Answer
Creating an algortithm which satisfies these conditions and is faster than O(n logn) is tricky. The intuite approach of adding all the lements from 'k' sorted lists into another list and then sorting has a runnng time of O(n logn). So to beat that we implemented a min heap structure. First we have to import heapq so we can utilize some of its functions. We then create a min heap with the first elements from each list (they'll
