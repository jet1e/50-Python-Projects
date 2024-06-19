# Temperature converter
# Converts celsius, farenheit and kelvin

def c_to_f(n):
    return (n*(9/5)+32)

def f_to_c(n):
    return ((n-32)*(5/9))

def c_to_k(n):
    return (n+273.15)

def k_to_c(n):
    return (n-273.15)

def f_to_k(n):
    return (((n-32)*(5/9))+273.15)

def k_to_f(n):
    return (((n-273.15)*(9/5))+32)

def main():
    while True:
        print("(1) Celsius to Farenheit")
        print("(2) Celsius to Kelvin")
        print("(3) Farenheit to Celsius")
        print("(4) Farenheit to Kelvin")
        print("(5) Kelvin to Celsius")
        print("(6) Kelvin to Farenheit")
        print("(0) Exit")

        try:
            choice = int(input("Enter a option number: "))
            if choice == 0:
                break
            elif (choice < 0) or (choice > 6):
                print("Not a correct choice")
            else:
                number = float(input("Enter a number to be converted: "))
                if choice == 1:
                    print(f"{number}C = {c_to_f(number)}°F")
                elif choice == 2:
                    print(f"{number}C = {c_to_k(number)}°K")
                elif choice == 3:
                    print(f"{number}F = {f_to_c(number)}°C")
                elif choice == 4:
                    print(f"{number}F = {f_to_k(number)}°K")
                elif choice == 5:
                    print(f"{number}K = {k_to_c(number)}°C")
                elif choice == 6:
                    print(f"{number}K = {k_to_f(number)}°F")
        except ValueError:
            print("Not a number")

main()