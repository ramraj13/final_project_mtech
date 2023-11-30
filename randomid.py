import random


def generate_random_number_with_seed(process_number):
    seed = process_number  #Use the process number as the seed
    random.seed(seed)
    random_number = random.randint(1,65335)  #Change the range as needed
    return random_number