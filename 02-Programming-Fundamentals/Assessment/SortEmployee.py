def sort_employees(employees, sort_by):
    key_indices = {
        "name": 0,
        "age": 1,
        "salary": 2
    }
    
    index = key_indices[sort_by]
    return sorted(employees, key=lambda employee: employee[index])
