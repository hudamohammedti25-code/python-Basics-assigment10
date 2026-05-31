def is_passed(student_score, passing_score):
    if student_score >= passing_score:
        return True
    else:
        return False

result1 = is_passed(85, 60)
print("Is the first student successful?", result1)

result2 = is_passed(45, 60)
print("Is the second student successful?", result2)
