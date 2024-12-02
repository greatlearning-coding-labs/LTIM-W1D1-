def celsius_to_fahrenheit(celsius):
    # remove the pass keyword and write your code
    pass    

def fahrenheit_to_celsius(fahrenheit):
    # remove the pass keyword and write your code
    pass

# dont modify following lines of code
def main():
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:
        choice = input("Enter choice (1/2): ")

        if choice in ['1', '2']:
            try:
                if choice == '1':
                    celsius = float(input("Enter temperature in Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"{celsius} °C = {fahrenheit} °F")
                elif choice == '2':
                    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit} °F = {celsius} °C")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            print("Invalid choice! Please select a valid conversion type.")

        # Ask if the user wants to perform another conversion
        next_conversion = input("Do you want to perform another conversion? (yes/no): ")
        if next_conversion.lower() != 'yes':
            break

if __name__ == "__main__":
    main()