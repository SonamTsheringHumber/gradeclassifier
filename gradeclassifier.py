mark = input("Enter your mark: ")

try:
    mark = float(mark)

    if mark < 0 or mark > 100:
        print("Invalid mark. Enter a mark between 0 and 100.")
    elif mark >= 90:
        print(f"Your mark is {mark}: Grade A")
    elif mark >= 80:
        print(f"Your mark is {mark}: Grade B")
    elif mark >= 70:
        print(f"Your mark is {mark}: Grade C")
    elif mark >= 60:
        print(f"Your mark is {mark}: Grade D")
    elif mark >= 50:
        print(f"Your mark is {mark}: Grade E")
    else:
        print(f"Your mark is {mark}: Grade F (Fail)")

except ValueError:
    print("Invalid input. Enter a number between 0 and 100.")