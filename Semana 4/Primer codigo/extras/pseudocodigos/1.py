def price_with_discount():
    product_price = int(input("What's the price of the product? \n"))

    if product_price < 100:
        discount = product_price * 0.02
    else:
        discount = product_price * 0.1

    final_price = product_price - discount

    print(f"The final price with the discount is: {final_price}")


price_with_discount()
