total_amount = float(input("Enter the total amount received for the job: "))

# Split between you and two friends (3 people total)
individual_share = total_amount / 3

print(f"Each person receives: ${individual_share:.2f}")
