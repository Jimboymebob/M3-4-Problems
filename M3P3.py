last_name = input("Enter student last name: ")
midterm = float(input("Enter midterm score: "))
final_exam = float(input("Enter final exam score: "))

# Calculation: 40% Midterm, 60% Final
total_points = (midterm * 0.40) + (final_exam * 0.60)

print(f"Student: {last_name}")
print(f"Total Exam Points: {total_points:.2f}")
