from faker import Faker
import random

fake = Faker()

# 랜덤 이름과 핸드폰 번호 생성
def generate_employee_data(num_employees):
    employees = []
    for _ in range(num_employees):
        name = fake.name()
        phone_no = fake.phone_number()
        employees.append((name, phone_no))
    return employees

# 예를 들어 10명의 랜덤 직원 데이터를 생성
employee_data = generate_employee_data(1000)





# 생성된 데이터 출력
for name, phone_no in employee_data:
    print(f"Name: {name}, Phone Number: {phone_no}")
