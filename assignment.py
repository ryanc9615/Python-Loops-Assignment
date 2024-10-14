all_products = False
product_details = []

while not all_products:
    product_input = input("Enter product name (or 'done' to finish): ").lower()
    
    if product_input != "done":
        product_price = input("Enter price: ")
        product_details.append(product_price)
    else:
        all_products = True

for string in range(0, len(product_details)):
    product_details[string]= int(product_details[string])

total_cost = sum(product_details)
print(f"Total cost: ${total_cost}")