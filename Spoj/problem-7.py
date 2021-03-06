/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
*/

def is_prime(n):
    #if n < 2: return False
    #if n == 2: return True
    #if n & 1: return False
    for i in range(3,int(n**.5)+1,2):
        if not n%i:
            return False
    return True
def prime_list(n):
    primes = [2,3,5,7,11,13]
    i = max(primes) + 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i+=2
    return primes
print max(prime_list(10001))
