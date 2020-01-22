N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

while(len(make_divisors(N)) != 2):
    if N % 2 == 0:
        N += 1
    else:
        N += 2

print(N)