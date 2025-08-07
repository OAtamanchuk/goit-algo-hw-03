import random

def get_numbers_ticket(min, max, quantity):
    if (
        not (1 <= min <= 1000)
        or not (1 <= max <= 1000)
        or min >= max
        or not (min <= quantity <= max - min + 1)
    ):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 117, 10)
print("Ваші лотерейні числа:", lottery_numbers)

