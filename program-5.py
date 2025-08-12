# Function to calculate the square of a number
def calculate_square(number):
    return number ** 2
num = float(input("Enter a number to calculate its square: "))
print(f"The square of {num} is {calculate_square(num)}.")