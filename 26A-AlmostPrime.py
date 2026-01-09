
# 09/01/2026. Understood the problem by own and solved the problem by own.

n = int(input().strip())

# Empirical evidence for prime number
def prime(n):
    if n <= 1:
        return False
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False

# Prime factorizations
def factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            if divisor not in factors:
                factors.append(divisor)
            n /= divisor
        divisor = divisor + 1
    
    return factors
    
almost_factor = 0
almost_factor_condition = 0
for i in range(1,n+1):
    num_factors = factors(i)
    for num_factor in num_factors:
        if prime(num_factor):
            almost_factor_condition += 1
    
    if almost_factor_condition == 2:
        almost_factor += 1
    
    almost_factor_condition = 0

print(almost_factor)

