import math

# file

# with open("sample.txt", mode="r") as hamlet:
#     words = list()
#     with open("hamlet_copy.txt", mode="w") as hamlet_copy:
#         for lines in hamlet.readlines():
#             words += lines.upper().strip().split(" ")
#         print(len(words))
#
#         unique_words = set(words)
#         for w in sorted(unique_words):
#             hamlet_copy.write(w)
#             hamlet_copy.write("\n")
#         print(len(unique_words))
#
# total_c = 0
# for u_w in sorted(unique_words):
#     if u_w.lower()[0] == "c".lower():
#         total_c += 1
#
# print(total_c)

# prime number

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

print(len(total_prime))
