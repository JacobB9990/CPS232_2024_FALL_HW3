import random


def create_arry(length: int = 0) -> list[int]:  # Creates an array of unique random integers
    arry: set[int] = set() # Using a set for uniqueness
    while len(arry) < length:
        rand = random.randint(1, length * 10)
        arry.add(rand) 

    return list(arry) # Convert back to a list


def partition(arr: list[int], l: int, r: int) -> int:  # Partitions the array around a pivot element
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i] = arr[j]
            arr[j] = arr[i]
            i += 1

    arr[i] = arr[r]
    arr[r] = arr[i]
    return i


def kthSmallestIterative(arr: list[int], l: int, r: int, k: int) -> int | None:  # Iteratively finds the k-th smallest element in the array
    while l <= r:
        index = partition(arr, l, r)

        if index - l == k - 1:  # Found the k-th smallest element
            return arr[index]
        elif index - l > k - 1:  # Search in the left part
            r = index - 1
        else:  # Search in the right part
            k -= index - l + 1
            l = index + 1

    print("Index out of bound")
    return None


# Example
n: int = int(input("Length of list (int value): "))
random_arry: list[int] = create_arry(n)
k: int = int(input("Which k-th element would you like? (int value) "))
result = kthSmallestIterative(random_arry, 0, n - 1, k)
if result is not None:
    print(f"The {k}-th smallest element is: {result}")
