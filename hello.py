import math

def process_data(data_list):
    print(f"Processing {len(data_list)} items...")
    
    # 1. LOGIC ERROR: Using 'is' instead of '==' for value comparison
    # This might work for small integers but fail for larger ones/objects.
    threshold = 256
    if len(data_list) is threshold:
        print("Threshold reached!")

    for item in data_list:
        # 2. RUNTIME ERROR: ZeroDivisionError
        # This will crash the workflow if an item is 0.
        result = 100 / item
        
        # 3. RUNTIME ERROR: TypeError 
        # Attempting to use a string in a math function.
        print(f"Square root: {math.sqrt(item)}")

# 4. SYNTAX ERROR: Uncomment the line below to test a build failure
# if True print("This will break the parser") 

if __name__ == "__main__":
    # Test cases to trigger the errors:
    # 'a' will trigger a TypeError
    # 0 will trigger a ZeroDivisionError
    my_data = [10, 20, 0, "40"] 
    
    process_data(my_data)
