temperature = float(input("Enter the temperature in °C: "))

if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 25:
    print("Warm")
else:
    print("Hot")