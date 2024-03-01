length = int(input())
width = int(input())
height = int(input())
percent = float(input())
obem = (length * width * height) / 1000
liters_needet = obem * (1 - (percent / 100 ))

print(liters_needet)
