product_details = {}

while True:
    product_input = input("Enter product name (or 'done' to finish): ").lower()
    if product_input == "done":
        break
    product_price = int(input("Enter price: "))
    product_details[product_input] = product_price

total_cost = sum(product_details.values())

print(f"Total Cost: ${total_cost}")