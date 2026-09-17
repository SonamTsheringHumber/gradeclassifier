mark= input("Enter your mark: ")
try:
    mark = float(mark)
    if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
    elif mark >= 80:
        print(f"Your mark is {mark}: Grade A")
    elif mark >= 60:
        print(f"Your mark is {mark}: Grade B")
    else:
        print(f"Your mark is {mark}: Grade C")

except ValueError:
    print("Invalid input. Please enter a mark in number.")

