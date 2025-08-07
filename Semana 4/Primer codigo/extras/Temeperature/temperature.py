def temperature_converter():
    celsius = float(input("Enter your celsius grades: \n"))

    fahrenheit = (9 / 5) * celsius + 32
    kelvin = celsius + 273.15

    print(f"Fahrenheit: {fahrenheit}")
    print(f"Kelvin: {kelvin}")


temperature_converter()
