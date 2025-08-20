# Creating a dictionary for 3 students
student1 = {
    "name": "Musab",
    "age": 15,
    "hobis": ["Coding", "Basketball", "Astrophysics"],
    "adress": {
        "city": "İstanbul",
    }
}

student2 = {
    "name": "Ayşe",
    "age": 16,
    "hobis": ["Reading a book", "Swimming"],
    "adress": {
        "city": "Ankara",
    }
}

student3 = {
    "name": "Emir",
    "age": 15,
    "hobis": ["Chess", "Football"],
    "adress": {
        "city": "İzmir",
    }
}

# Adding the students to a list
students = [student1, student2, student3]

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    
    print("Hobis:")
    for hobi in student["hobis"]:
        print("   -", hobi)
    
    print("Adress:")
    for key, value in student["adress"].items():
        print("   ", key.capitalize() + ":", value)
    
    print()  # A space between the students
