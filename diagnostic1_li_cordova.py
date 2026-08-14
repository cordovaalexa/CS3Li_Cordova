def calculate_checkout(cart_total, shipping_speed):

    cart_total = []
    shipping = []
    shipping_speed = []

    input("What is your cart total and shipping speed?")

    if shipping_speed == "express": 
        shipping == 15
    print("Shipping is 15")

    elif shipping_speed == "overnight": 
    shipping == 25
    print("Shipping is 25")

    elif shipping_speed == "standard": 
    cart_total >= 100
    print("Cart total is greater than or equal to 100, therefore shipping is free")

    elif shipping_speed == "standard":
    cart_total < 100
    print("Shipping is 10")

    else shipping == 0
    print("ERROR")

    sum(cart_total + shipping)
    return

print("Your total is (sum). Please provide payment")
