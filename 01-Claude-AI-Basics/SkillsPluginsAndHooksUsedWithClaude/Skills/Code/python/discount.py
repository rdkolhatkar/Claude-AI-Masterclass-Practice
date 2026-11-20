def get_discount(user_type, amount):
    if user_type == "premium":
        discount = amount * 0.2
    elif user_type == "regular":
        discount = amount * 0.1
    return amount - discount
