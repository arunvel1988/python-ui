

day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the week")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Mid-week day")

print("---------------------------------")

# Example 2: Match with integers
num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")

print("---------------------------------")

# Example 3: Matching multiple patterns
command = "delete"

match command:
    case "start" | "run":
        print("Program is starting")
    case "stop" | "end":
        print("Program is stopping")
    case "delete":
        print("Program will be deleted")
    case _:
        print("Unknown command")

print("---------------------------------")

# Example 4: Match with conditions (guards)
marks = 82

match marks:
    case m if m >= 90:
        print("Grade: A+")
    case m if m >= 75:
        print("Grade: A")
    case m if m >= 60:
        print("Grade: B")
    case m if m >= 50:
        print("Grade: C")
    case _:
        print("Failed")

