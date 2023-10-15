from sys import maxsize

max_num = maxsize

while True:
    text = input()
    if text == 'Stop':
        print(max_num)
        break

    num = int(text)
    if max_num > num:
        max_num = num