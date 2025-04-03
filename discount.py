price= 1000
discount_percent= 10

if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
else:
    final_price = price

print(f"The final price after applying the discount is: {final_price}")

print("product price=.....")
print("discount percent=.....")

discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

print(final_price)