#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program converts Celsius to Fahrenheit with user input


def celsius_to_fahrenheit(celsius):
    # This function converts Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def main():
    # This function gets user input and calls the conversion function
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("{:.2f}°C is equal to {:.2f}°F".format(celsius, fahrenheit))
    except ValueError:
        print("Enter a decimal number.")


if __name__ == "__main__":
    main()
