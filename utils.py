import json


def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def sort_operations_by_date(operations):
    valid_operations = []
    for operation in operations:
        if operation.get('date'):
            valid_operations.append(operation)

    result = sorted(valid_operations, key=lambda operation: operation['date'], reverse=True)
    return result
