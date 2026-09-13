contacts = {
    'number': 4,
    'students':
        [{'name': 'John Doe', 'email': 'john.doe@example.com'},
         {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
         {'name': 'Bob Johnson', 'email': 'bob.johnson@example.com'},
         {'name': 'Alice Williams', 'email': 'alice.williams@example.com'}
        ]
}
print("Student emails: ")
for student in contacts['students']:
    print(student['email'])