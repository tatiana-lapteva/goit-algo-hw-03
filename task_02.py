""" generate the list of certain number of unique random digits whithin provided range"""



import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    win_tickets = []
    all_tickets = [] 
    if isinstance(min, int) and min >=1 and \
        isinstance(max, int) and max <=1000 and \
            isinstance(quantity, int) and quantity <=max:
        all_tickets.extend((range(min, max)))
        all_tickets.append(max)
        random.shuffle(all_tickets)
        win_tickets = random.sample(all_tickets, k=quantity)
        return win_tickets
            
    else:
        return win_tickets
    
lottery_numbers = get_numbers_ticket(1, 49, 50)
print("Ваші лотерейні числа:", lottery_numbers)