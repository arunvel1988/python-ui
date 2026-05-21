attempt = 1
max_attempts = 3

while attempt <= max_attempts:

    print("Connection Attempt", attempt)

    if attempt == 3:
        print("Device Connected Successfully")

    else:
        print("Connection Failed")

    attempt = attempt + 1
