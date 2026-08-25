from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
        
        # Calculations using imported functions
        sq = square(num)
        even_status = is_even(int(num)) if num.is_integer() else "N/A (Decimal)"
        fah = celsius_to_fahrenheit(num)
        
        # Display Results
        print(f"\n--- Results for {num} ---")
        print(f"Square: {sq}")
        print(f"Is Even: {even_status}")
        print(f"Fahrenheit equivalent: {fah:.2f}°F")
        
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
