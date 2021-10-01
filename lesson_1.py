# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in numbers:
#     print(number, end=", ")
# max_iter = len(numbers)
# print(max_iter)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for item in matrix:
#     for number in item:
#         print(number, end=", ")
# employees = [{'name': 'Sara', 'age': 25, 'is_married': True, 'deportment': 'HR'},
#              {'name': 'Alex', 'age': 30, 'is_married': True, 'deporment': 'Call center'},
#              {'name': 'Brandon', 'age': 30, 'height': 175, 'is_married': False, 'deportment': 'Taxi driver'}]

# employee = []
# max_age = 0
# def creat_employees():
employees = [{'name': 'Sara', 'age': 25, 'is_married': True, 'deportment': 'HR'},
                 {'name': 'Alex', 'age': 30, 'is_married': True, 'deporment': 'Call center'},
                 {'name': 'Brandon', 'age': 30, 'height': 175, 'is_married': False, 'deportment': 'Taxi driver'}]
    # return employees

# creat_employees()

# def find_eldest_employees(employees: list):
#     max_age = 0
#     eldest_employees_dict = {}
#
#     for employee in employees:
#         if employee['age'] >= max_age:
#             max_age = employee['age']
#
#         if eldest_employees_dict.get(max_age, None) is None:
#             eldest_employees_dict[max_age] = [employee['name']]
#         else:
#             eldest_employees_dict[max_age].append(employee['name'])
#
#     return eldest_employees_dict[max_age]
# # Main of of app
# eldest_employees = find_eldest_employees(employees)
# print(eldest_employees)



max_age = 0
name = None
# eldest_empl = []
employee_dict = {}

for employee in employees:
    if employee['age'] >= max_age:
        max_age = employee['age']

print(max_age)

#     if employee_dict.get(employee['age']) is None:
#         employee_dict[employee['age']] = [employee['name']]
#     else:
#         employee_dict[employee['age']].append(employee['name'])
#
# print(employee_dict[max_age])



