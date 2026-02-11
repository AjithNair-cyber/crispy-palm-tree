import math

def process_data(data_list):
    print(f"Processing {len(data_list)} items...")
    
    # Fix logic error: Change 'is' to '==' for value comparison
    threshold = 256
    if len(data_list) == threshold:
        print("Threshold reached!")

    for item in data_list:
        # Add type checks to ensure 'item' is not 0 and is a number before performing division and square root operations.
        if isinstance(item, (int, float)) and item != 0:
            result = 100 / item
            print(f"Square root: {math.sqrt(item)}")
        else:
            print(f"Invalid item encountered: {item}")

# Uncomment the line below to test a build failure
# if True print("This will break the parser") 

if __name__ == "__main__":
    # Test cases to trigger the errors:
    # 'a' will trigger a TypeError
    # 0 will trigger a ZeroDivisionError
    my_data = [10, 20, 0, "40"] 
    
    process_data(my_data)