# SortNumbers
arr = [3, 1, 2, 2, 3, 1, 1, 3, 2, 4, 0, 5, 7, 6, 8, 9, 1, 0, 4, 6, 5]
print(arr)

counts = [0] * 10  # Initialize counts for 10 possible values (0-9)

# Counting number elements
for el in arr:
    counts[el] += 1

index = 0
for i, count in enumerate(counts):
    while count > 0:
        arr[index] = i
        count -= 1
        index += 1


print(arr)
# print(obj)
