def check_discount(total_price, ticket_quantity, coupon_code):
    if coupon_code == "NONTONSERU" and ticket_quantity >= 2:
        return total_price - 15000
    else:
        return total_price
    
final_price_1 = check_discount(50000, 2, "NONTONSERU")
print("Price after discount (first case):", final_price_1)

final_price_2 = check_discount(50000, 2, "nontonseru")
print("Price without discount (second case due to letters)", final_price_2)