# Python Code For Testing

def calculate_total(price, tax_rate):
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return price + (price * tax_rate)

points = 0

# Assuming items is a dictionary containing item names and their prices
items = {'apple': 0.5, 'banana': 0.3}

for item, price in items.items():
    try:
        total = calculate_total(price, 0.1)
        points += int(total)  # Assuming we want to add the total as points
    except (ValueError, TypeError) as e:
        print(f"Error processing {item}: {e}")

message = f"Total points earned: {points}"
print(message)