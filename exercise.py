usernames = ['CArLos','Juan','Mario','Admin','maria','Jhon']
new_users = ['carlos','Maria','oscar','JHOn']

current_users = [user.lower() for user in usernames]



for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorrry but the name: {new_user.title()}, is already exist")
    else:
        print(f"welcome: {new_user.title()}.")
print("End")


ordinal_numbers = [var1 for var1 in range(1,10)]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"El numero es: {ordinal_number}st.")
    elif ordinal_number == 2:
        print(f"El numero es: {ordinal_number}nd.")
    elif ordinal_number == 3:
        print(f"El numero es: {ordinal_number}rd.")
    else:
        print(f"El numero es: {ordinal_number}th.")


