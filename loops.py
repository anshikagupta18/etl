expense_food = [45,65,89,97,46]
expense_misc = [29,12,23,7,16]
total = 0
for expense in expense_food:
    total += expense

print("food expense is:", total)

for expense in expense_misc:
    total += expense

print("Misc expense is:", total)

expense_food = [45,65,89,97,46]
expense_misc = [29,12,23,7,16]
total = 0

def find_total(expenses):
    total = 0
    for expense in expense_food:
        total += expense
    return total



