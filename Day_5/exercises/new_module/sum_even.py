
def sum_even_list(num_list: list) -> int:
    return sum([i for i in num_list if num_list %2 == 0])