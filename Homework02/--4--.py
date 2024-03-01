from math import floor

pages = int(input())
pages_for_hour = int(input())
days = int(input())
hours = pages / pages_for_hour
hours = hours / days

print(floor(hours))