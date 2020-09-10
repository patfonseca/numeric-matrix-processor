n = input()
list_numbers = []
for char in enumerate(n):
    list_numbers.append(int(n[char]))
moving_average = []
for char in range(len(n) - 1):
    moving_average.append((list_numbers[char] + list_numbers[char + 1]) / 2)
print(moving_average)