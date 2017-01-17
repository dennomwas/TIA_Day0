#A working function to generate prime numbers from 0 to n with asymptotic analysis in your public Github repo

#A Prime Number can be divided evenly only by 1, or itself. And it must be a whole number greater than 1.

def prime_numbers(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the max number of Prime numbers to print : "))

for primes in range(2, num + 1):
    if prime_numbers(primes):
        print (primes),




	





	

	



