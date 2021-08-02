def transform(data):
    """round the price to 2 decimal places"""
    data['price'] = round(data.price, 2)
    return data