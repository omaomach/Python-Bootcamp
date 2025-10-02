def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    return len(password) >= 8

def validate_phone(phone):
    return phone.startswith("+254") and len(phone) == 13

users = [
    {"email": "joash@iball.ke", "password": "secure123", "phone": "+254123456789"},
    {"email": "invalid", "password": "123", "phone": "0712345678"}
]

for user in users:
    print(f"Validating: {user['email']}")
    print(f" Email valid: {validate_email(user['email'])}")
    print(f" Password valid: {validate_password(user['password'])}")
    print(f" Phone valid: {validate_phone(user['phone'])}")
    print()