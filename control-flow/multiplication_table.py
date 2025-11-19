user_number = int(input("Enter a number to see its multiplication table: "))


for number in  range(1,10):
    result = number * user_number
    print(f"{user_number} * {number} = {result}" )