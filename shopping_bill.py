# Input: prices of 3 items and tax percentage
item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
tax_percentage = float(input("Enter the tax percentage: "))

# Function to calculate total cost including tax
def calculate_total_with_tax(item1, item2, item3, tax_percentage):
    subtotal = item1 + item2 + item3
    tax_amount = subtotal * (tax_percentage / 100)
    total_cost = subtotal + tax_amount
    return total_cost

# Call the function and display the result
total = calculate_total_with_tax(item1, item2, item3, tax_percentage)
print("Total cost including tax:", round(total, 2))
