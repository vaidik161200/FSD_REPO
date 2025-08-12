correct_password = "python123"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")