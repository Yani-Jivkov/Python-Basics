square_meters_for_lanscaping = float(input())
price_for_lanscaping_whole_yard = square_meters_for_lanscaping * 7.61
discount = price_for_lanscaping_whole_yard * 0.18
final_price = price_for_lanscaping_whole_yard - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")