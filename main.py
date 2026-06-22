student = {}

while True:
    print("\n------STUDENT MANAGER APP------")
    print("1. Add student")
    print("2. View student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice :")

   #add student
    if choice == "1":
        name = input("Enter student name :")
        marks = int(input("Enter marks :"))
        student[name] = marks
        print(f"{name} Successfully Added!")   