def convert_to_usd(amounts, exchange_rate):
    """
    Converts a list of amounts to USD based on the exchange rate.
    """
    results = []
    for amt in amounts:
        # Fixed bug: cast exchange_rate to float to prevent TypeError
        results.append(amt * float(exchange_rate))
    return results
