import random

def get_numbers_ticket(min, max, quantity):
    # quantity < 1 - обмежує 
    if quantity < 1 or min < 1 or max > 1000 or (max-min)+1 < quantity: 
        return []
    
    set_numbers = set()
    while len(set_numbers) < quantity:
        set_numbers.add(random.randint(min, max))

    list_numbers = list(set_numbers)
    list_numbers.sort()
    return list_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)