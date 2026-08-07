from typing import List


def sort_words(words: List[str]) -> List[str]:
    result = words.copy()

    # bubble sort implementation
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if len(result[j]) < len(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


def sort_numbers(numbers: List[int]) -> List[int]:
    result = numbers.copy()

    # bubble sort implementation
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if abs(result[j]) > abs(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
