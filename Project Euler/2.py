# Even Fibonacci numbers
previous, number, i, sum = 0, 1, 0, 0
while number < 4000000:
    i = number; number += previous; previous = i
    if number % 2 == 0: sum += number
print(sum)