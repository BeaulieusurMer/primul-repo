def celsius_to_fahrenheit(celsius):
    """
    Converteste temperatura din grade Celsius in grade Fahrenheit.

    Formula: F = (C × 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def main():
    print("=== Convertor Celsius -> Fahrenheit ===\n")

    try:
        # Citeste temperatura in Celsius de la utilizator
        celsius = float(input("Introdu temperatura in grade Celsius: "))

        # Converteste in Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)

        # Afiseaza rezultatul
        print(f"\n{celsius}°C = {fahrenheit}°F")

    except ValueError:
        print("Eroare! Te rog introdu un numar valid.")


if __name__ == "__main__":
    main()
