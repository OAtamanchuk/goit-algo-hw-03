import random

def get_numbers_ticket(min, max, quantity):
    if (
        not (1 <= min <= 1000) or
        not (1 <= max <= 1000) or
        min >= max or
        not (1 <= quantity <= (max - min + 1))
    ):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)
   
try:
    min_value = int(input("Enter the minimum number: "))
    max_value = int(input("Enter the maximum number: "))
    quantity_value = int(input("Enter the quantity of numbers: "))
    lottery_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
    print("Ваші лотерейні числа:", lottery_numbers)
except ValueError:
    print("Invalid input. Please enter valid integers for min, max, and quantity.")
    

