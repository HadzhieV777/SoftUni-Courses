# 09. Company Users
data = input()
company_users = {}

while not data == "End":
    company, employee_id = data.split(" -> ")

    if company not in company_users:
        company_users[company] = []
    if employee_id not in company_users[company]:
        company_users[company].append(employee_id)

    data = input()

for company, employee_ids in sorted(company_users.items(), key=lambda x: x[0]):
    print(company)
    for e_id in employee_ids:
        print(f'-- {e_id}')