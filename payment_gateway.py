def process_batch_payments(transaction_ids):
    """
    Processes a batch of payments. We assume the transaction IDs are formatted as "region-id".
    Extracts the region code from each ID.
    """
    processed_regions = []
    for t_id in transaction_ids:
        if "-" in t_id:
            parts = t_id.split("-")
            region = parts[0]
            processed_regions.append(region)
    return processed_regions
