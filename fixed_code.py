def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # FIXED: divide by len(numbers), not len(numbers) + 1


def largest(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:  # FIXED: use > to track the maximum, not <
            max_value = n
    return max_value


data = [3, 8, 2, 10, 5]
print("Average:", average(data))  # FIXED: close the print() call with a missing parenthesis
print("Largest:", largest(data))
