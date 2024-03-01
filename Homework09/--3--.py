big_num = int(input())
all_num = 0

while True:
    num = int(input())
    all_num += num

    if all_num >= big_num:
        print(all_num)
        break