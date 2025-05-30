def check_age():
    try:
        # Prompt user for input
        age = int(input("Enter your age: "))
        
        # Check if age is negative
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        print(f"Your age is valid: {age}")
    
    except ValueError as e:
        # Handle invalid input or negative age
        print(f"Invalid input: {e}")

# Call the function
check_age()