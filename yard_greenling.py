square_meters = float(input())
square_meter_price = 7.61
greening_price = square_meters * square_meter_price
discount = greening_price * 0.18
final_price = greening_price - discount
print(f'The final price is:{final_price} lv.')
print(f'The discount is: {discount} lv.')