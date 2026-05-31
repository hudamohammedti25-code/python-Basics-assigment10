def calculate_loyalty_points(total_transaction, member_status):
    if member_status == False: 
        return 0
    
    points = total_transaction // 20000
    return points

points_non_member = calculate_loyalty_points(100000, False)
print("points non member", points_non_member)

points_member = calculate_loyalty_points(105000, True)
print("points_member", points_member)