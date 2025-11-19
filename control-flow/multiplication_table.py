user_number = int(input("Enter a number to see its multiplication table: "))

numbers= 1,2,3,4,5,6,7,8,9,10
print(numbers)

for number in  numbers:
    result = number * user_number
    print(f"{user_number} * {number} = {result}" )