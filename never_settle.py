data = {
    "academy": {
        "departments": {
            "web": {
                "students": [
                    {"name": "Ali", "age": 20, "skills": ["HTML", "CSS", "JS"]},
                    {"name": "Joy", "age": 22, "skills": ["Python", "Django"]}
                ],
                "active": True
            },
            "blockchain": {
                "students": [
                    {"name": "Musa", "age": 21, "skills": ["Solidity", "Rust"]},
                    {"name": "Zara", "age": 23, "skills": []}
                ],
                "active": False
            }
        },
        "location": {
            "city": "Jos",
            "country": "Nigeria",
            "meta": {
                "zone": "North-Central",
                "elevation": 1217
            }
        }
    }
}


print(data['academy']['departments']['web']['students'][1])

print(" ")
print("expected output is: '{"name": "Joy", "age": 22, "skills": ["Python", "Django"]}' ")
