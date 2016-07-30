# Largest prime factor
N = 600851475143
i = 2
while N != 1:
    if N % i == 0: N = N // i
    else: i += 1
print(i)