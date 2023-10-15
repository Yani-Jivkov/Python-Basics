month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * nights
    apartment_price = 65 * nights
    if nights > 14:
        studio_price *= 0.7
        apartment_price *= 0.9
    elif nights > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20 * nights
    apartment_price = 68.70 * nights
    if nights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
elif month == "July" or month == "August":
    studio_price = 76 * nights
    apartment_price = 77 * nights
    if nights > 14:
        apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")