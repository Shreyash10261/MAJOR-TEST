def process_data(data_list):
    """
    Takes a list of string values, converts them to integers, and returns their sum.
    """
    total = 0
    for item in data_list:
        # Intentional Bug: Fails with ValueError if item cannot be cast to int (e.g. "N/A" or "")
        total += int(item)
    return total
