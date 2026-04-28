import json

data = """{
  "users": [
    {
      "id": 1,
      "name": "Ali",
      "orders": [
        {"id": 101, "price": 100},
        {"id": 102, "price": 150}
      ]
    },
    {
      "id": 2,
      "name": "Vali",
      "orders": []
    }
  ]
}"""
d_data = json.loads(data)
def calculate_total_spent(data: dict) -> list:
    new_data = []
    for user in data["users"]:
        total = sum(order["price"] for order in user["orders"])      
        new_data.append({
            "id": user["id"],
            "name": user["name"],
            "total_spent": total
        })
    return new_data
print(calculate_total_spent(d_data))