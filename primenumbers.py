#A working function to generate prime numbers from 0 to n with asymptotic analysis in your public Github repo

#A Prime Number can be divided evenly only by 1, or itself. And it must be a whole number greater than 1.

def prime_numbers(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


n = 50

for p in range(2, n+1):
    if prime_numbers(p):
        print (p),

print ("Done")
	





	

	



