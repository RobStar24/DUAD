employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]


def order_by_department(employees):
    sorted_employees = {}

    for employee in employees:
        if employee["department"] in sorted_employees:
            sorted_employees[employee["department"]].append(employee)
        else:
            sorted_employees[employee["department"]] = [employee]

    return sorted_employees


print(order_by_department(employees))
