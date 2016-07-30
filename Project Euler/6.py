# Sum Square Difference
N = 100
sum1, sum2 = 0, 0
for i in range(N + 1):
    sum1 += i**2
    sum2 += i
difference = sum2**2 - sum1
print(difference)