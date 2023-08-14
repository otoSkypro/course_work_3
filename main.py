import os

from utils import load_operations, sort_operations_by_date, get_executed_only, formate_for_output

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
FILENAME = 'operations.json'
OPERATIONS_FILE_PATH = os.path.join(ROOT_PATH, FILENAME)

def main():
    all_operations = load_operations(OPERATIONS_FILE_PATH)
    sorted_operations = sort_operations_by_date(all_operations)
    executed_operations = get_executed_only(sorted_operations)

    for operation in executed_operations:
        print(formate_for_output(operation))
        print()


if __name__ == '__main__':
    main()