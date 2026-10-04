def process_data(data_list):
    """
    Takes a list of string values, converts them to integers, and returns their sum.
    """
    total = 0
    for item in data_list:
        try:
            total += int(item)
        except ValueError:
            continue
    return total
