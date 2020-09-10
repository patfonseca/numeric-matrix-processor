def range_sum(numbers, start, end):
    sum_ = 0
    for n in numbers:
        if int(start) <= int(n) <= int(end):
            sum_ += int(n)
    return sum_

input_numbers = input().split()
a_b = input().split()
print(range_sum(input_numbers, a_b[0], a_b[1]))