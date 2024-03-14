list_of_numbers = []
print("Please enter some integers. The program will stop when you enter a non-integer")

check = True
while check:
    ask = input()
    if ask.isnumeric():
        list_of_numbers.append(int(ask))
    else:
        check = False

mininum = min(list_of_numbers)
maximum = max(list_of_numbers)
print(list_of_numbers)
print(f'The smallest number is: {mininum}, and the largest number is {maximum}')