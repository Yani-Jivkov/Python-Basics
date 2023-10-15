n = int(input())
total_sum = 0
max_number = float('-inf')

for i in range(n):
    num = int(input())
    total_sum += num

    if num > max_number:
        max_number = num

if max_number == (total_sum - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (total_sum - max_number))
    print("No")
    print(f"Diff = {diff}")
