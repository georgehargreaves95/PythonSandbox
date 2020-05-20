print("Welcome to PyCalc! Functions available: convert_celsius, convert_fahrenheit, calc_trapezoid_area")


def convert_celsius():
    print("Convert celsius to fahrenheit")
    celsius = float(input("Enter the celsius value: "))
    fahrenheit = (celsius - 32) * 100 / 180
    print("Fahrenheit value: ", fahrenheit)
    return


def convert_fahrenheit():
    print("Convert fahrenheit to celsius")
    fahrenheit = float(input("Enter the fahrenheit value: "))
    celsius = (fahrenheit * 180 / 100) + 32
    print("Celsius value: ", celsius)
    return


def calc_trapezoid_area():
    print("Calculate the area of a trapezoid")
    height = float(input("Enter the height: "))
    top_length = float(input("Enter the length of the top base: "))
    bottom_length = float(input("Enter the length of the bottom base: "))
    area = (top_length + bottom_length) * height * 0.5
    print("Trapezoid Area: ", area)
    return
