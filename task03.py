def is_valid_user(user: dict) -> bool:
    name_valid = len(user.get("name", "").strip()) > 0
    email_valid = "@" in user.get("email", "")
    age_valid = user.get("age", 0) > 0
    
    return name_valid and email_valid and age_valid

def split_users(data: list) -> dict:
    result = {
        "valid_users": [],
        "invalid_users": []
    }
    
    for user in data:
        if is_valid_user(user):
            result["valid_users"].append(user)
        else:
            result["invalid_users"].append(user)
            
    return result

users_data = [
    {"name": "Ali", "email": "ali@example.com", "age": 20},
    {"name": "", "email": "invalid-email", "age": -5},
    {"name": "Vali", "email": "vali@example.com", "age": 25}
]

# Natija
print(split_users(users_data))
