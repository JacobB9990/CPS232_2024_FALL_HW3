2. (35 pts) Given `k` sorted lists, please design an algorithm as efficient as possible to merge these sorted list into a single sorted list. The total number of elements in all given lists is `n`. And please analyze the running time of your algorithm. (Hint: Better than `O(n log n)`)

Answer:

Creating an algortithm which satisfies these conditions and is faster than O(n log n) is tricky. The intuite approach of adding all the lements from 'k' sorted lists into another list and then sorting has a runnng time of O(n log n). So to beat that we implemented a min heap structure. First we have to import heapq so we can utilize some of its functions. We then create a min heap with the first elements from each list (for lists sorted in ascending order). And pop out the min element (always the head of a heap) and insert into a seperate array which will be our complete sorted list. After pushing the min element we insert the next element from the list where the previous poopped element came from (if list is empty then nothing happens). And we repeat this cycle until the min heap is empty. 

Running time:

We argue that the running time of the algorithm above is O(n log k). The time complexity of inserting the elements into the min heap is O(log k) and this done for each element which would be O(n). So altogether the running time of the algorthm should be O(n log k), which faster than O(n log n) asssuming that the lists contain more than one element in each (in that case n and k would be equal). 
