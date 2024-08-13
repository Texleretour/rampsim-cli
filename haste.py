HASTE_PER_PERCENTAGE = 170

def calculate_haste_percent(haste_rating):
    # TODO: Implement diminishing returns
    
    return round(haste_rating / HASTE_PER_PERCENTAGE, 1)