import random


def generateRandomList(num_range: int, list_length: int) -> list:
    random_list: list = random.sample(range(num_range), list_length)
    print(f"The randomly generated list looks like: {random_list}")
    return random_list


def findSmallest(arr: list[int]) -> int:
    smallest: int = arr[0]
    smallest_index: int = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: list[int]):
    newArr: list = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    print(f"The sorted list: {newArr}")
    return newArr


selectionSort(generateRandomList(100, 20))
