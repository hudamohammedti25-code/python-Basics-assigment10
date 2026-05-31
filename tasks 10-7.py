def create_username(full_name, birth_year):
    first_name = full_name.split()[0].lower()
    year_str = str(birth_year)[-2:]
    return first_name + year_str

username = create_username("Huda Mohammed Jameel", 2006)
print("The new username is:", username)