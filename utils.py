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

def get_executed_only(operations, quantity=5):
    result = []

    for operation in operations:
        if operation['state'] == 'EXECUTED':
            result.append(operation)
        if len(result) == quantity:
            break

    return result

def hide_requisites(requisites):
    requisites_parts = requisites.split()
    number = requisites_parts[-1]
    if requisites.lower().startswith("счет"):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    requisites_parts[-1] = hided_number
    hided_requisites = ' '.join(requisites_parts)
    return hided_requisites


def formate_for_output(operation):
    # line 1
    line_1_elements = []
    datetime_info = operation['date']
    date = datetime_info[:10]
    date_splitted = date.split('-')
    formated_date = '.'.join(reversed(date_splitted))
    line_1_elements.append(formated_date)
    line_1_elements.append(operation['description'])

    # line 2
    line_2_elements = []
    from_info = operation.get('from')
    to_info = operation.get('to')
    if from_info:
        line_2_elements.append(hide_requisites(from_info))
    else:
        line_2_elements.append('Наличный взнос')
    line_2_elements.append(hide_requisites(to_info))

    # line 3
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    return (f"{' '.join(line_1_elements)}\n"
            f"{' -> '.join(line_2_elements)}\n"
            f"{amount} {currency}")
