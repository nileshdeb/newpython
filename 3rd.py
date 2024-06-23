
while True:
    print("Enter 1 to convert Celsius to Fahrenheit")
    print("Enter 2 to convert Fahrenheit to Celsius")
    choice = input("Enter your choice: ")
    if choice == '1':
        c = float(input("Enter the temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit")
    elif choice == '2':
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f} degrees Fahrenheit is equal to {c} degrees Celsius")
    else:
        print("Invalid choice. Please enter 1 or 2.")
