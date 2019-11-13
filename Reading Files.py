
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():

print(employee_file.read())
print(employee_file.read())
employee_file.close()

print(employee_file.read())