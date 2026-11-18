#1. Input Shopping Items and Discount

# List of items with their name, price per unit, and quantity
shopping_items = [
    {"item": "Apple", "price": 1.20, "quantity": 5},
    {"item": "Milk", "price": 3.50, "quantity": 1},
    {"item": "Bread", "price": 2.75, "quantity": 2},
    {"item": "Cheese", "price": 7.99, "quantity": 1}
]

# Discount percentage (e.g., 10% discount)
discount_percentage = 0.10

# Tax rate (e.g., 8% sales tax)
sales_tax_rate = 0.08

print("Shopping Items:")
for item_data in shopping_items:
    print(f"  - {item_data['item']}: {item_data['quantity']} x ${item_data['price']:.2f}")
print(f"Discount: {discount_percentage * 100}%")
print(f"Sales Tax: {sales_tax_rate * 100}%")


# 2. Calculate the Shopping Bill

item_totals = []
subtotal_before_discount = 0.0

for item_data in shopping_items:
    total_for_item = item_data['price'] * item_data['quantity']
    item_totals.append({"item": item_data['item'], "total": total_for_item})
    subtotal_before_discount += total_for_item

# Apply discount
discount_amount = subtotal_before_discount * discount_percentage
subtotal_after_discount = subtotal_before_discount - discount_amount

# Apply sales tax
tax_on_bill = subtotal_after_discount * sales_tax_rate

# Final total
final_bill_total = subtotal_after_discount + tax_on_bill

print(f"Subtotal before discount: ${subtotal_before_discount:.2f}")
print(f"Discount amount ({discount_percentage*100}%): ${discount_amount:.2f}")
print(f"Subtotal after discount: ${subtotal_after_discount:.2f}")
print(f"Tax amount ({sales_tax_rate*100}%): ${tax_on_bill:.2f}")

# 3. Display the Shopping Bill

print("\n--- Your Shopping Bill ---")
print("--------------------------")
for item_data in shopping_items:
    print(f"{item_data['item']:<15} {item_data['quantity']:>3} x ${item_data['price']:.2f} = ${(item_data['price'] * item_data['quantity']):.2f}")
print("--------------------------")
print(f"Subtotal:                 ${subtotal_before_discount:.2f}")
print(f"Discount ({discount_percentage * 100}%):         -${discount_amount:.2f}")
print(f"Subtotal (after discount): ${subtotal_after_discount:.2f}")
print(f"Sales Tax ({sales_tax_rate * 100}%):             +${tax_on_bill:.2f}")
print("--------------------------")
print(f"Total Amount Due:         ${final_bill_total:.2f}")
print("--------------------------")