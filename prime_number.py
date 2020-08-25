import math

number = int(input("Give a range: "))


def is_prime(num):
    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True


total_prime = []
 
for i in range(1, number + 1):
    if i != 1:
        if is_prime(i):
            print(i)
            total_prime.append(i)

print(f"Total prime : {len(total_prime)}")
