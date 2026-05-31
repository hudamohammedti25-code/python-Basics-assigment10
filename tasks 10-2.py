def calculate_overtime_salary(base_salary, total_hours_worked):
    if total_hours_worked > 40:
        overtime_hours = total_hours_worked - 40
        overtime_pay = overtime_hours * 50000
        return base_salary + overtime_pay
    else:
        return base_salary
    

salary_with_overtime = calculate_overtime_salary(200000, 45)
print("First employee salary (plus overtime pay):", salary_with_overtime)

regular_salary = calculate_overtime_salary(200000, 38)
print("The salary of the second employee (excluding overtime):", regular_salary)