from math import pow

num = int(input())

for i in range(0, num + 1, 2):
    print(int(pow(2, i)))
