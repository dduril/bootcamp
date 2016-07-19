# -----------------------------------------------
# Python Examples
#
# Generators
# -----------------------------------------------

def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while True:
        if is_prime(n): yield n
        n += 1

print("Prime Numbers")
for n in primes():
    if n > 100: break
    print(n)
print("Done")