def format_address(street, city, province, postal_code):
    postal_code_str = str(postal_code)
    
    formatted = "Street: " + street + ", City: " + city + ", " + province + " (" + postal_code_str + ")"
    
    return formatted

my_address = format_address("Main Street No. 5", "Jeddah", "Central Region", 12345)

print(my_address)