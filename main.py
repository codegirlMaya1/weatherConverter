def get_temperature():
    return input("Please enter the temperature in Fahrenheit: ")

def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return None

def display_temperature(fahrenheit):
    celsius = convert_to_celsius(fahrenheit)
    if celsius is not None:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

def main():
    try:
        fahrenheit = get_temperature()
        display_temperature(fahrenheit)
    finally:
        print("Thank you for using the weather forecast application!")

if __name__ == "__main__":
    main()