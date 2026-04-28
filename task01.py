import json


json_data = """[
  {"id": 1, "name": "Ali", "age": 17, "is_student": true},
  {"id": 2, "name": "Vali", "age": 22, "is_student": false},
  {"id": 3, "name": "Hasan", "age": 19, "is_student": true}
]"""

def get_student_stats(data: str) -> dict:
    person = json.loads(data)
    
    students = [n for n in person if n['is_student'] is True]
    
    if not students:
        return {"count": 0, "average_age": 0.0}
    
    total_age = sum(s.get('age', 0) for s in students)
    count = len(students)
    average_age = total_age / count
    
    return {
        "count": count,
        "average_age": average_age
    }

print(get_student_stats(json_data))
