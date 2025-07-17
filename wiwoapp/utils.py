
def generate_order_id():
    # Generate a unique 10-character alphanumeric string for order ID
    import random
    import string
    characters = string.ascii_uppercase + string.digits
    order_id = ''.join(random.choice(characters) for _ in range(15))
    return order_id
