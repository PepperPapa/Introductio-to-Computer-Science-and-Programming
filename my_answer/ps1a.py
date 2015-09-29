#!usr/bin/python3.4
# Problem Set 1 
# Name: xin zhong
# Collaborators: 
# Time: 14:43~15.17  
#
##############Problem 1####################
#打印1000个素数（不打印2）
# store prime numbers
prime_number = []
is_prime = True
n = 3
while True:
    # prime number must be odd number
    if n % 2 != 0:
        # check whether n can be divisible by other numbers one by one
        i = 3
        while i < n:
            if n % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print("%s is prime number." % n)
            prime_number.append(n)

    if len(prime_number) >= 1000:
        break
    n += 1
    is_prime = True

for n in prime_number:
    print(n, end=' ')

