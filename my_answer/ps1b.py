#!usr/bin/python3.4
# Problem Set 1 
# Name: xin zhong
# Collaborators: 
# Time: 16:20~17:17  
#
##############Problem 2####################
# 连续素数的乘积（包含2）随着素数n的增大越来越接近与e**n（e的n次方）
# 对数的发明是为了解决大数乘积的问题，把大数的乘除转换为加减
# 本程序计算素数的对数之和与最大素数n的比值，测试要取多个n值进行测试
# 随着n的增加比值应该接近与1
#
from math import *

prime_number = []
log_number = []
is_prime = True
n = 2
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
            log_number.append(log(n, e))
            prime_number.append(n)

    if len(log_number) >= 1000:
        break
    n += 1
    is_prime = True

def ratio(count):
    #count means the number of primes
    log_sum = 0
    for i in range(count):
        log_sum += log_number[i]
    print("="*60)
    print(log_sum)
    print(prime_number[count - 1])
    print(log_sum / prime_number[count - 1])

count = [1,2,3,4,5,6,7,8,9,10,100,200,300,400,500,600,700,800,900,1000]
print("The ratio of sum of logarithms and n:")
for i in count:
    ratio(i)
