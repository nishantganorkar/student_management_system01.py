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

     #view student
    elif choice == "2":
        if not student:
            print("No Student Found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)


     #check result
    elif choice == "3":
        name = input("Enter student name :")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"marks is {marks}\nPASS")
            else:
                print(f"marks is {marks}\nFAIL")

        else:
            print("Student not Found!")


    #exit
    elif choice == "4":
        print("Exiting....")
        break

    else:
        print("In Valid Input...")
