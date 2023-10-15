count_pens = int(input())
count_markers = int(input())
liters_preparation = int(input())
discount = int(input())
pens_price = count_pens * 5.8
markers_price = count_markers * 7.20
preparation_price = liters_preparation * 1.20
total = pens_price + markers_price + preparation_price
discount = total * (discount / 100)
total = total - discount
print(total)