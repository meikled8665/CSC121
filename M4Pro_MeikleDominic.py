#Dominic Meikle
#2/17/2026
#M4 Project
#desc


courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 508},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}

students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}

def menu():
    #prints menu
    print("-"*9,"MENU","-"*9)
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses And Tuition For Specific Student")
    print("4) Display Tuition For All Students")
    print("5) Display # Of Students And Tuition For All Students")
    print("6) Exit")
    print("-"*22,"\n")
    
    #gets a valid input from the user
    choice = int(input("Enter Option: "))
    
    return choice

def displayAll():
    print(f"{"Code":<10}{"Description":<31}{"Tuition"}")
    print("-"*60)
    
    #prints every classes information
    for key, value in courses.items():
        print(f"{key:<9} {value["desc"]:<30} ${value["tuition"]}")
        
    print("-"*60,"\n")

def lookup():
    code = input("Enter The Course Code: ")
    
    #checks if the class exists
    while courses.get(code) == None:
        print("Invalid Code. Re-enter")
        code = input("Enter The Course Code: ")
    
    #prints course info
    print(f"\nCourse Code: {code}")
    print(f"Course Description: {courses[code]["desc"]}")
    print(f"Course Tuition: ${courses[code]["tuition"]}\n")
    
def stuTuition():
    nameList = []
    for k in students:
        nameList.append(k)
    
    print("\n")
    for i in range(0, len(nameList)):
        print(f"{i + 1}) {nameList[i]}")
    
    choice = int(input("\nSelect Student: ")) - 1
    
    while choice < 0 and choice > len(nameList):
        print("Invalid Choice. Please Re-enter")
        choice = int(input("\nSelect Student: ")) - 1
    
    #gets student from user and looks up their information
    stuName = nameList[choice]
    stuTList = students[stuName]
    
    if stuName[-1] == 's':
        print(f"\n{stuName}' Courses And Tuition:")
    else:
        print(f"\n{stuName}'s Courses And Tuition:")
        
    print("-"*60)
        
    #prints the selected students tuition and classes
    totTuition = 0
    for i2 in stuTList:
        course = courses[i2]
        print(f"{i2:<9} {course["desc"]:<30} ${course["tuition"]:,.2f}")
        totTuition += course["tuition"]
        
    print("-"*60)
    
    print(f"{"Overall Total: ":<40} ${totTuition:,.2f}\n")
    
def allTuition():
    totTuition = 0
    
    print(f"{"\nStu Name:":<31} {"# Of Courses:":<15} {"Tuition:"}")
    
    print("-"*60)
    
    #prints every students tuition
    for k, v in students.items():
        stuTuition = 0
        
        for i in v:
            stuTuition += courses[i]["tuition"]
        
        totTuition += stuTuition
        print(f"{k:<30} {len(v):<15} ${stuTuition:,.2f}")
        
    print("-"*60)
    
    print(f"{"Overall Total:":<46} ${totTuition:,.2f}\n")
    
def StuPerCourse():
    print(f"\n{"Course Code:":<20} {"# Of Stu:":<20} {"Tuition Generated:"}")
    print("-"*60)
    
    #counts the amount of srudents in each class as well as their total tuition
    for course, info in courses.items():
        count = 0
        
        for classes in students.values():
            if course in classes:
                count += 1
        
        tuition = count * info["tuition"]
        
        print(f"{course:<20} {count:<20} ${tuition:,.2f}")
    print()
    
def main():
    choice = 0
    
    while choice != 6:
        #displays menu and gets users input
        choice = menu()
        
        #runs function for users selection
        match choice:
            case 1:
                displayAll()
            case 2:
                lookup()
            case 3:
                stuTuition()
            case 4:
                allTuition()
            case 5:
                StuPerCourse()
            case 6:
                break
            case _:
                print("Invalid Choice")
    
    print("\nClosing Program...")


#calls main function
if __name__ == "__main__":
    main()