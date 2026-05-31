def calculate_split_bill(total_bill, number_of_people, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    
    grand_total = total_bill + tip_amount
    
    share_per_person = grand_total / number_of_people
    
    return share_per_person

result = calculate_split_bill(300000, 4, 10)

print("The amount paid by one person :", result)